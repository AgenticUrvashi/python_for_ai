from load_expences import load_expenses

def view_expences():
    print("======= ALL EXPENSES =======")
    expenses = load_expenses()
    if not expenses:
        print("No expenses found!")
        return

    for expense in expenses:
        print(f"ID      : {expense.get('user_id')}")
        print(f"TITLE   : {expense.get('user_title')}")
        print(f"AMOUNT  : {expense.get('user_amount')}")
        print(f"CATEGORY: {expense.get('user_catagery')}")
        print(f"DATE    : {expense.get('user_date')}")
        print(f"TYPE    : {expense.get('type', 'Expense')}\n")
