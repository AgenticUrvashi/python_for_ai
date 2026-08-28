from load_expenses import load_expenses

def view_expences():
    print("======= ALL EXPENSES =======")
    expenses = load_expenses()

    for expense in expenses:

        print(f"ID      : {expense["user_id"]}")
        print(f"TITLE   : {expense["user_title"]}")
        print(f"AMOUNT  : {expense["user_amount"]}")
        print(f"CATEGORY: {expense["user_catagery"]}")
        print(f"DATE    : {expense["user_date"]}\n")

