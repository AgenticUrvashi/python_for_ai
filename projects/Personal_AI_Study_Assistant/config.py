import os
from typing import Dict, List

# Locate environment files (current folder and workspace root)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, "..", ".."))

def _load_env_files():
    """Load variables from .env files into os.environ if not already set."""
    candidate_paths = [
        os.path.join(PROJECT_DIR, ".env"),
        os.path.join(WORKSPACE_ROOT, ".env")
    ]
    for env_path in candidate_paths:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                            continue
                        if "=" in line:
                            key, val = line.split("=", 1)
                            key = key.strip()
                            val = val.strip().strip('"').strip("'")
                            if key and key not in os.environ:
                                os.environ[key] = val
            except Exception:
                pass

_load_env_files()

APP_NAME = "StudySync Pro - Personal AI Study Assistant"
APP_VERSION = "3.0.0 (Pro Edition)"
HOST = "127.0.0.1"
PORT = 5000

# Groq API configuration
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODELS_URL = "https://api.groq.com/openai/v1/models"

# Read Groq API Key and clean model string
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "").strip()

raw_model = os.environ.get("GROQ_MODEL", "qwen/qwen3.8-27b").strip()
if raw_model.startswith("groq:"):
    raw_model = raw_model[len("groq:"):]
GROQ_DEFAULT_MODEL = raw_model or "qwen/qwen3.8-27b"

# Google Gemini fallback
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
GEMINI_DEFAULT_MODEL = "gemini-1.5-flash"

# Available Models for UI dropdown
AVAILABLE_MODELS = [
    {
        "id": "qwen/qwen3.8-27b",
        "name": "Qwen 3.8 27B (Ultra-Fast & High Accuracy - Recommended)",
        "provider": "Groq",
        "context": "32k",
        "badge": "Default"
    },
    {
        "id": "llama-3.3-70b-versatile",
        "name": "Llama 3.3 70B Versatile (Deep Academic Reasoning & Coding)",
        "provider": "Groq",
        "context": "128k",
        "badge": "Pro Reasoner"
    },
    {
        "id": "llama-3.1-8b-instant",
        "name": "Llama 3.1 8B Instant (Lightning-Fast Speed)",
        "provider": "Groq",
        "context": "128k",
        "badge": "Fast"
    }
]

# Study Personas / Modes
STUDY_MODES: Dict[str, Dict[str, str]] = {
    "explainer": {
        "title": "Concept Explainer",
        "icon": "🎓",
        "instruction": (
            "You are a master academic tutor. Explain concepts with crystal clarity, "
            "intuitive real-world analogies, step-by-step logic, bullet points, and visual ascii/markdown diagrams where helpful. "
            "Adopt an encouraging, pedagogical tone."
        )
    },
    "code": {
        "title": "Code & Debug Tutor",
        "icon": "💻",
        "instruction": (
            "You are a senior computer science educator and software engineer. "
            "Provide production-grade, well-commented code, break down the logic line-by-line, "
            "detail Time Complexity (Big-O) and Space Complexity, and mention edge cases or debugging pitfalls."
        )
    },
    "exam": {
        "title": "Exam High-Yield Notes",
        "icon": "📝",
        "instruction": (
            "You are an exam prep specialist. Format your output into high-yield revision notes: "
            "Key Definitions, Formula Reference Sheet, Memory Mnemonics, Differences/Comparisons Table, "
            "and Top 3 Probable Exam/Viva Questions."
        )
    },
    "math": {
        "title": "Step-by-Step Math Solver",
        "icon": "🧮",
        "instruction": (
            "You are a mathematics professor. Solve the problem with rigorous step-by-step derivations. "
            "State each formula or theorem applied, show intermediate algebraic calculations clearly, "
            "and state the final simplified answer in bold with verification."
        )
    }
}

# Strict prompt instruction for AI Guardrail
STUDY_ONLY_SYSTEM_PROMPT = (
    "You are StudySync Pro, a world-class personal AI Study Assistant. "
    "Your strict rule is: ONLY answer educational, academic, learning, coding, homework, science, mathematics, and exam-related questions. "
    "If the user asks ANY question not related to studies, academics, coding, or learning "
    "(such as movies, sports scores, celebrity gossip, casual flirting, politics, weather, recipes, non-academic chit-chat), "
    "you MUST politely refuse with: "
    "'Sorry! Main sirf study-related aur educational questions ke jawab de sakta hoon. Kripya apne subjects, concepts ya homework se juda sawaal poochhein. 📚' "
    "Never break character or answer non-study questions. Maintain rich formatting with Markdown, bold headers, code snippets, and clean math notations."
)

ALLOWED_TOPICS = [
    "Computer Science & Python",
    "Data Structures & Algorithms",
    "Mathematics & Statistics",
    "Physics & Chemistry",
    "Biology & Life Sciences",
    "English & Academic Writing",
    "Exam Preparation & Revision Notes",
    "General Science & Engineering"
]