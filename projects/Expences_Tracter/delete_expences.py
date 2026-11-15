from load_expences import load_expenses
from save_expences import save_expences

def delete_expense():
    expenses = load_expenses()
    search = input("Enter ID to delete: ").strip()

    initial_len = len(expenses)
    updated_expenses = [e for e in expenses if str(e.get("user_id")) != search]

    if len(updated_expenses) < initial_len:
        save_expences(updated_expenses)
        print("Deleted successfully...")
    else:
        print("Expense not found!")
