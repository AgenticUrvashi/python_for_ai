from load_expences import load_expenses

def add_expense():
    expenses = load_expenses()
    existing_ids = {str(e.get("user_id")) for e in expenses}

    while True:
        user_id = input("Enter ID: ").strip()
        if not user_id:
            print("ID cannot be empty!")
            continue
        if user_id in existing_ids:
            print("ID already exists!")
            continue
        break

    user_title = input("Enter title: ").strip()

    while True:
        try:
            user_amount = float(input("Enter amount: "))
            if user_amount < 0:
                print("Amount cannot be negative!")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric amount!")

    user_catagery = input("Enter category: ").strip()
    user_date = input("Enter date (DD/MM/YYYY): ").strip()

    expense = {
        "user_id": user_id,
        "user_title": user_title,
        "user_amount": user_amount,
        "user_catagery": user_catagery,
        "user_date": user_date,
        "type": "Expense"
    }
    print("Added successfully...")
    return expense
