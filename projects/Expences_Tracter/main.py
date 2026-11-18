"""
Expense Tracker Application
Modern Desktop App Interface + CLI Mode
Matching the custom pastel purple UI design.
"""

import sys
import os
import json
import subprocess
import threading
import time
import webbrowser
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR, "web")
DATA_FILE = os.path.join(BASE_DIR, "expence.json")

# Ensure BASE_DIR is on sys.path
sys.path.insert(0, BASE_DIR)

from load_expences import load_expenses
from save_expences import save_expences
from add_expences import add_expense
from view_expences import view_expences
from search_expences import search_expense
from delete_expences import delete_expense
from total_expences import total_expense
from highest_expences import highest_expense

HOST = "127.0.0.1"
PORT = 5055


def parse_month_index(date_str):
    """Returns 0 for Jan ... 11 for Dec, or -1 if not determinable."""
    if not date_str:
        return -1
    s = str(date_str).strip()
    try:
        if "-" in s:
            parts = s.split("-")
            if len(parts) >= 2:
                # e.g., 2026-11-18
                m = int(parts[1])
                if 1 <= m <= 12:
                    return m - 1
        elif "/" in s:
            parts = s.split("/")
            if len(parts) >= 2:
                # e.g., 28/08/2026
                m = int(parts[1])
                if 1 <= m <= 12:
                    return m - 1
    except Exception:
        pass
    return -1


def compute_analytics():
    """Computes totals, monthly distribution, and category breakdown."""
    expenses = load_expenses()

    total_income = 0.0
    total_expense = 0.0
    monthly_inc = [0.0] * 12
    monthly_exp = [0.0] * 12
    cat_breakdown = {}
    highest_exp = None

    for item in expenses:
        try:
            amt = float(item.get("user_amount", 0))
        except (ValueError, TypeError):
            continue

        tx_type = (item.get("type") or "Expense").strip().capitalize()
        m_idx = parse_month_index(item.get("user_date"))

        if tx_type == "Income":
            total_income += amt
            if 0 <= m_idx < 12:
                monthly_inc[m_idx] += amt
        else:
            total_expense += amt
            if 0 <= m_idx < 12:
                monthly_exp[m_idx] += amt

            cat = (item.get("user_catagery") or "Other").strip().capitalize()
            cat_breakdown[cat] = cat_breakdown.get(cat, 0.0) + amt

            if highest_exp is None or amt > float(highest_exp.get("user_amount", 0)):
                highest_exp = item

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "monthly_income": monthly_inc,
        "monthly_expense": monthly_exp,
        "category_breakdown": cat_breakdown,
        "highest_expense": highest_exp,
        "total_count": len(expenses)
    }


class ReusableHTTPServer(HTTPServer):
    allow_reuse_address = True


class ExpenseAppRequestHandler(SimpleHTTPRequestHandler):
    """Serves Web UI assets and handles REST API requests."""

    def log_message(self, format, *args):
        # Keep terminal log clean and legible
        sys.stdout.write(f"[ExpenseApp] {args[0]} -> {args[1]}\n")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self._serve_file(os.path.join(WEB_DIR, "index.html"), "text/html")
        elif path == "/style.css":
            self._serve_file(os.path.join(WEB_DIR, "style.css"), "text/css")
        elif path == "/app.js":
            self._serve_file(os.path.join(WEB_DIR, "app.js"), "application/javascript")
        elif path == "/api/transactions":
            expenses = load_expenses()
            self._send_json(expenses)
        elif path == "/api/analytics":
            data = compute_analytics()
            self._send_json(data)
        else:
            # Fallback static file check in WEB_DIR
            target = os.path.join(WEB_DIR, path.lstrip("/"))
            if os.path.exists(target) and os.path.isfile(target):
                self._serve_file(target, "application/octet-stream")
            else:
                self.send_error(404, "Not Found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        data = self._read_json_body()

        if path == "/api/transactions":
            expenses = load_expenses()
            new_id = str(data.get("user_id") or (len(expenses) + 1))
            new_item = {
                "user_id": new_id,
                "user_title": data.get("user_title", "Untitled"),
                "user_amount": float(data.get("user_amount", 0)),
                "user_catagery": data.get("user_catagery", "Other"),
                "user_date": data.get("user_date", time.strftime("%Y-%m-%d")),
                "type": data.get("type", "Expense")
            }
            expenses.append(new_item)
            save_expences(expenses)
            self._send_json({"success": True, "transaction": new_item})

        elif path == "/api/exit":
            self._send_json({"success": True, "message": "Server shutting down..."})
            def shutdown():
                time.sleep(0.5)
                os._exit(0)
            threading.Thread(target=shutdown, daemon=True).start()
        else:
            self.send_error(404, "Not Found")

    def do_PUT(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        data = self._read_json_body()

        if path == "/api/transactions":
            expenses = load_expenses()
            target_id = str(data.get("user_id"))
            found = False
            for idx, item in enumerate(expenses):
                if str(item.get("user_id")) == target_id:
                    expenses[idx] = {
                        "user_id": target_id,
                        "user_title": data.get("user_title", item.get("user_title")),
                        "user_amount": float(data.get("user_amount", item.get("user_amount", 0))),
                        "user_catagery": data.get("user_catagery", item.get("user_catagery")),
                        "user_date": data.get("user_date", item.get("user_date")),
                        "type": data.get("type", item.get("type", "Expense"))
                    }
                    found = True
                    break

            if found:
                save_expences(expenses)
                self._send_json({"success": True, "message": "Updated successfully"})
            else:
                self._send_json({"success": False, "message": "Transaction not found"}, 404)
        else:
            self.send_error(404, "Not Found")

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/api/transactions":
            target_id = params.get("id", [""])[0]
            expenses = load_expenses()
            initial_count = len(expenses)
            expenses = [e for e in expenses if str(e.get("user_id")) != target_id]

            if len(expenses) < initial_count:
                save_expences(expenses)
                self._send_json({"success": True, "message": f"Deleted transaction #{target_id}"})
            else:
                self._send_json({"success": False, "message": "Transaction not found"}, 404)
        else:
            self.send_error(404, "Not Found")

    def _read_json_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 0:
            try:
                body = self.rfile.read(content_length)
                return json.loads(body.decode("utf-8"))
            except Exception:
                pass
        return {}

    def _serve_file(self, filepath, content_type):
        try:
            with open(filepath, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", f"{content_type}; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Error reading file: {str(e)}")

    def _send_json(self, data, status=200):
        content = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(content)


def launch_desktop_window(url):
    """
    Attempts to launch Microsoft Edge or Google Chrome in standalone desktop window mode (--app).
    Falls back to system default browser if standalone mode is unavailable.
    """
    browser_candidates = [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
    ]

    for exe in browser_candidates:
        if os.path.exists(exe):
            try:
                # Launch as a dedicated frameless app window matching the screenshot!
                subprocess.Popen([exe, f"--app={url}"])
                return True
            except Exception:
                pass

    # Fallback to default browser
    webbrowser.open(url)
    return False


def start_app():
    """Starts the Expense Tracker GUI Application."""
    global PORT
    server_address = (HOST, PORT)
    httpd = None

    for p in [5055, 5056, 5057, 5000]:
        try:
            PORT = p
            server_address = (HOST, PORT)
            httpd = ReusableHTTPServer(server_address, ExpenseAppRequestHandler)
            break
        except OSError:
            continue

    if not httpd:
        print("Error: Could not bind to any port for Expense Tracker.")
        return

    app_url = f"http://{server_address[0]}:{server_address[1]}"
    print("=" * 70)
    print("👛 EXPENSE TRACKER - DESKTOP APPLICATION")
    print("✨ Plan • Track • Save ♡")
    print(f"🌐 Running live at: {app_url}")
    print("🚀 Standalone Desktop App window is launching...")
    print("=" * 70)

    # Launch desktop window after brief startup delay
    threading.Timer(0.8, lambda: launch_desktop_window(app_url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Expense Tracker. Goodbye! 💜")
        httpd.server_close()


def run_cli():
    """Original Interactive Terminal Menu Mode."""
    print("============================EXPENSE TRACKER=============================")
    while True:
        print("\n1. Add Expense")
        print("2. View Expense")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Total Expense")
        print("6. Highest Expense")
        print("7. Launch GUI App")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            expenses = load_expenses()
            new_item = add_expense()
            expenses.append(new_item)
            save_expences(expenses)
        elif choice == 2:
            view_expences()
        elif choice == 3:
            search_expense()
        elif choice == 4:
            delete_expense()
        elif choice == 5:
            total_expense()
        elif choice == 6:
            highest_expense()
        elif choice == 7:
            start_app()
            break
        elif choice == 8:
            print("THANK YOU 💜")
            break
        else:
            print("Invalid input...")
    print("=" * 75)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["--cli", "-c"]:
        run_cli()
    else:
        start_app()
