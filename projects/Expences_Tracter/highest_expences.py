from load_expences import load_expenses

def highest_expense():
    print("==== HIGHEST EXPENSE ====")
    expenses = load_expenses()
    if not expenses:
        print("NO expenses found!")
        return None

    def get_amount(e):
        try:
            return float(e.get("user_amount", 0))
        except (ValueError, TypeError):
            return 0.0

    high = max(expenses, key=get_amount)
    print(f"TITLE   : {high.get('user_title')}")
    print(f"AMOUNT  : {high.get('user_amount')}")
    print(f"CATEGORY: {high.get('user_catagery')}")
    print(f"DATE    : {high.get('user_date')}")
    return high
