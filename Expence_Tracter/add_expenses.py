def add_expense():

    user_id = input("enter your id: ")
    user_title = input("enter title: ")

    while True:
        try:
            user_amount = int(input("enter amount: "))
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
