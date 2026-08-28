from load_expenses import load_expenses

def total_expense():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            total += int(expense["user_amount"])
        except ValueError:
            print("Please enter a valid amount!")
    print(f"TOTAL EXPENSE : {total} rupees")
