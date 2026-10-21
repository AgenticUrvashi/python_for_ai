"""
StudySync Pro - Personal AI Study Assistant (Pro Edition)
Main application server.
Launches the local web dashboard and serves the Groq-powered AI study engine APIs.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import json
import mimetypes
import threading
import urllib.parse
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

import config
from ai_engine import (
    analyze_document_content,
    generate_flashcards,
    generate_study_quiz,
    get_ai_response,
    test_groq_connection,
)
from topic_filter import is_study_related

WEB_DIR = os.path.join(BASE_DIR, "web")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

class StudySyncRequestHandler(SimpleHTTPRequestHandler):
    """Custom request handler serving static dashboard assets and REST APIs."""

    def log_message(self, format, *args):
        # Clean console log output
        sys.stdout.write(f"[StudySync Pro] {args[0]} -> {args[1]}\n")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # REST API: System Status & Active Model
        if path == "/api/status":
            self._send_json({
                "app_name": config.APP_NAME,
                "version": config.APP_VERSION,
                "groq_configured": bool(config.GROQ_API_KEY),
                "active_model": config.GROQ_DEFAULT_MODEL,
                "provider": "Groq Cloud"
            })
            return

        # REST API: Available Models
        if path == "/api/models":
            self._send_json({
                "models": config.AVAILABLE_MODELS,
                "default": config.GROQ_DEFAULT_MODEL,
                "personas": config.STUDY_MODES
            })
            return

        # REST API: Dynamic Quiz generation
        if path == "/api/quiz":
            params = urllib.parse.parse_qs(parsed.query)
            topic = params.get("topic", ["Machine Learning"])[0]
            difficulty = params.get("difficulty", ["Intermediate"])[0]
            count_str = params.get("count", ["4"])[0]
            model = params.get("model", [""])[0]
            try:
                count = int(count_str)
            except ValueError:
                count = 4
            questions = generate_study_quiz(topic=topic, difficulty=difficulty, count=count, model=model)
            self._send_json(questions)
            return

        # Static assets
        if path == "/" or path == "/index.html":
            self._serve_file(os.path.join(WEB_DIR, "index.html"), "text/html")
        elif path == "/style.css":
            self._serve_file(os.path.join(WEB_DIR, "style.css"), "text/css")
        elif path == "/app.js":
            self._serve_file(os.path.join(WEB_DIR, "app.js"), "application/javascript")
        elif path.startswith("/assets/"):
            asset_subpath = path[len("/assets/"):]
            file_path = os.path.join(ASSETS_DIR, asset_subpath)
            mime_type, _ = mimetypes.guess_type(file_path)
            self._serve_file(file_path, mime_type or "application/octet-stream")
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # Read JSON body safely
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        data = {}
        if body:
            try:
                data = json.loads(body.decode("utf-8"))
            except Exception:
                pass

        # REST API: AI Chat with Study Modes & Context Memory
        if path == "/api/chat":
            question = data.get("question", "")
            api_key = data.get("api_key", "")
            model = data.get("model", "")
            mode = data.get("mode", "explainer")
            history = data.get("history", [])

            response_data = get_ai_response(
                question=question,
                custom_api_key=api_key,
                model=model,
                mode=mode,
                conversation_history=history,
                return_details=True
            )
            self._send_json(response_data)
            return

        # REST API: Document & Notes Analysis
        elif path == "/api/documents/analyze":
            filename = data.get("filename", "study_notes.pdf")
            content = data.get("content", "")
            api_key = data.get("api_key", "")
            model = data.get("model", "")
            result = analyze_document_content(filename=filename, content=content, custom_api_key=api_key, model=model)
            self._send_json(result)
            return

        # REST API: Dynamic Flashcard Generation
        elif path == "/api/flashcards":
            topic = data.get("topic", "Data Structures")
            count = int(data.get("count", 5))
            api_key = data.get("api_key", "")
            model = data.get("model", "")
            cards = generate_flashcards(topic=topic, count=count, custom_api_key=api_key, model=model)
            self._send_json({"topic": topic, "flashcards": cards})
            return

        # REST API: Test Groq Connection
        elif path == "/api/test-groq":
            api_key = data.get("api_key", "")
            model = data.get("model", "")
            test_res = test_groq_connection(api_key=api_key, model=model)
            self._send_json(test_res)
            return

        self.send_error(404, "Endpoint Not Found")

    def _serve_file(self, file_path, content_type):
        if not os.path.exists(file_path):
            self.send_error(404, f"File {os.path.basename(file_path)} Not Found")
            return

        try:
            with open(file_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Server Error: {str(e)}")

    def _send_json(self, data):
        content = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(content)


def start_server():
    server_address = (config.HOST, config.PORT)
    try:
        httpd = HTTPServer(server_address, StudySyncRequestHandler)
    except OSError:
        # Port fallback if 5000 is occupied
        config.PORT = 5050
        server_address = (config.HOST, config.PORT)
        httpd = HTTPServer(server_address, StudySyncRequestHandler)

    url = f"http://{server_address[0]}:{server_address[1]}"
    print("=" * 70)
    print(f"🚀 {config.APP_NAME} v{config.APP_VERSION}")
    print(f"⚡ Powered by Groq: {config.GROQ_DEFAULT_MODEL}")
    print(f"🌐 Running live at: {url}")
    print("📚 Academic Guardrail Active: Answers ONLY educational/study queries.")
    print("✨ Press Ctrl + C to stop the assistant.")
    print("=" * 70)

    # Open web browser automatically
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down StudySync Pro. Goodbye!")
        httpd.server_close()


if __name__ == "__main__":
    start_server()
