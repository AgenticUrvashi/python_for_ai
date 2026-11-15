from load_expences import load_expenses

def total_expense():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            total += float(expense.get("user_amount", 0))
        except (ValueError, TypeError):
            continue
    print(f"TOTAL EXPENSE : {total} rupees")
    return total
