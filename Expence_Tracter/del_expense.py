from load_expenses import load_expenses
from save_expenses import save_expences

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
