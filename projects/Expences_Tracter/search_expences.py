from load_expences import load_expenses

def search_expense():
    expenses = load_expenses()
    search = input("Enter ID or Title for searching: ").strip().lower()
    found = False
    for expense in expenses:
        uid = str(expense.get("user_id", "")).lower()
        title = str(expense.get("user_title", "")).lower()
        cat = str(expense.get("user_catagery", "")).lower()
        if search in uid or search in title or search in cat:
            print("===== EXPENSE FOUND =====")
            print(f"ID      : {expense.get('user_id')}")
            print(f"TITLE   : {expense.get('user_title')}")
            print(f"AMOUNT  : {expense.get('user_amount')}")
            print(f"CATEGORY: {expense.get('user_catagery')}")
            print(f"DATE    : {expense.get('user_date')}\n")
            found = True
    if not found:
        print("Expense not found!")
