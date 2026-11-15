import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expence.json')

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            result = json.load(f)
            return result if isinstance(result, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Alias for backward compatibility
load_expences = load_expenses
