from load_expenses import load_expenses

def highest_expense():
    print("==== HIGHEST EXPENSE ====")
    expenses = load_expenses()
    
    if not expenses:
        print("NO expenses found!")
        return

    try:
        high = max(expenses, key=lambda expense:int(expense["user_amount"]))
    except ValueError:
        print("Please enter a valid amount!")
        return
    
    print(f"TITLE   : {high['user_title']}")
    print(f"AMOUNT  : {high['user_amount']}")
    print(f"CATEGORY: {high['user_catagery']}")
    print(f"DATE    : {high['user_date']}")

