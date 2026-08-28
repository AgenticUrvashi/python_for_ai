from load_expenses import load_expenses

def search_expense():
    expenses = load_expenses()
    search = input("enter your ID for searching: ")
    for expense in expenses:
        if expense["user_id"] == search:
            print("===== EXPENSE FOUND =====")
            print(f"ID      : {expense['user_id']}")
            print(f"TITLE   : {expense['user_title']}")
            print(f"AMOUNT  : {expense['user_amount']}")
            print(f"CATEGORY: {expense['user_catagery']}")
            print(f"DATE    : {expense['user_date']}")
            return

    print("Expense not found!")
