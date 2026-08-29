from load_expenses import load_expenses


def add_expense():

    while True:
        user_id = input("enter your id: ")

        expences = load_expenses()

        for expense in expences:
            if expense["user_id"] == user_id:
                print("ID already exists!")
                break

        else:
            break

    user_title = input("enter title: ")

    while True:
        try:
            user_amount = int(input("enter amount: "))

            if user_amount < 0:
                print("Amount cannot be negative!")
                continue

            break
        
        except ValueError:
            print("Please enter a valid amount!")

    user_catagery = input("enter your categery: ")
    user_date = input("enter date: ")

    expences = {
    "user_id" : user_id,
    "user_title" : user_title,
    "user_amount" : user_amount,
    "user_catagery" : user_catagery,
    "user_date" : user_date
    }
    print("Added successfully...")
    return expences
