"""
Launcher script to run the Student Management System Streamlit Web App.
Usage:
    python projects/run_app.py
"""

import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_FILE = os.path.join(BASE_DIR, "projects", "student_app.py")

# Path to the virtual environment streamlit executable
STREAMLIT_EXE = os.path.join(BASE_DIR, ".venv_app", "Scripts", "streamlit.exe")

if not os.path.exists(STREAMLIT_EXE):
    # Fallback to python -m streamlit
    cmd = [sys.executable, "-m", "streamlit", "run", APP_FILE]
else:
    cmd = [STREAMLIT_EXE, "run", APP_FILE]

print(f"🚀 Launching Student Management Portal...\nRunning: {' '.join(cmd)}\n")
try:
    subprocess.run(cmd, check=True)
except KeyboardInterrupt:
    print("\n👋 App stopped by user.")
except Exception as e:
    print(f"Error launching app: {e}")
