from add_expenses import add_expense
from view_expences import view_expences
from search_expenses import search_expense
from del_expense import delete_expense
from total_expence import total_expense
from highest_expense import highest_expense

print("============================EXPENSE TRACKER=============================")

while True:

    print("\n1.Add Expense")
    print("2.View Expense")
    print("3.Search Expense")
    print("4.Delete Expense")
    print("5.Total Expense")
    print("6.Highest Expense")
    print("7.Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        add_expense()
        
    elif choice == 2:
        view_expences()

    elif choice == 3:
        search_expense()

    elif choice == 4:
        delete_expense()

    elif choice == 5:
        total_expense()

    elif choice == 6:
        highest_expense()

    elif choice == 7:
        print("THANK YOU")
        break
        
    else:
        print("Invalid input...")