import json

def load_expenses():
    with open('Expence_Tracter/expence.json','r') as f:
        result = json.load(f)
        return result


def save_expences(data):
    with open('Expence_Tracter/expence.json','w') as f:
        result = json.dump(data ,f,indent=4)
        return result

def add_expense():
    expences = {
    "user_id" : input("enter your id: "),
    "user_title" : input("enter title: "),
    "user_amount" : input("enter amount: "),
    "user_catagery" : input("enter your categery: "),
    "user_date" : input("enter date: ")
    }
    print("Added successfully...")
    return expences
    

def view_expences():
    print("======= ALL EXPENSES =======")
    expenses = load_expenses()

    for expense in expenses:

        print(f"ID      : {expense["user_id"]}")
        print(f"TITLE   : {expense["user_title"]}")
        print(f"AMOUNT  : {expense["user_amount"]}")
        print(f"CATEGORY: {expense["user_catagery"]}")
        print(f"DATE    : {expense["user_date"]}\n")

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

def delete_expense():
    expenses = load_expenses()
    search = input("enter your ID for delete details: ")

    found = False

    for expense in expenses:
        if expense["user_id"] == search:
            expenses.remove(expense)
            found = True
            save_expences(expenses)
            print("Delete successfully...")
    if not found:
        print("Expense not found")

def total_expense():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        total += int(expense["user_amount"])
    print(f"TOTAL EXPENSE : {total} rupees")

def highest_expense():
    print("==== HIGHEST EXPENSE ====")
    expenses = load_expenses()
    high = max(expenses, key=lambda expense:int(expense["user_amount"]))
    print(f"TITLE   : {high['user_title']}")
    print(f"AMOUNT  : {high['user_amount']}")
    print(f"CATEGORY: {high['user_catagery']}")
    print(f"DATE    : {high['user_date']}")








# new_expense = add_expense()
# expenses.append(new_expense)
# save_expences(expenses)
# view_expences()
# search_expense()