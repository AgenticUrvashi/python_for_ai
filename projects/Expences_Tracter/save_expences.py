import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expence.json')

def save_expences(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except PermissionError:
        print("You don't have permission to write this file!")
        return False
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

# Alias
save_expenses = save_expences
