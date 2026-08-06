print("=========================== Grade ========================")

def get_grade(marks):
    if marks >= 90:
        return "A"
            
    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "E"

while True:

    choice = input("you want to check grade for list or single mode again: ")
    print( )

    if choice == "list":
        students = {}
        n = int(input("how many students: "))
        
        for i in range(n):
            name = input("enter student name: ")
            marks = int(input("enter marks(0 to 100): "))
            students[name] = marks
            print( )

        for name, marks in students.items():

            print(f"{name}: Grade {get_grade(marks)}")


    elif choice == "single":
        while True:

            name = input("enter student name: ")
            marks = int(input("enter students marks(0 to 100): "))

            print( )

            print(f"{name} : Grade {get_grade(marks)}")

            want_to_continue = input("Do you want to continue(y/n): ")
            if want_to_continue == "n":
                break

    else:
        print("Invalid input")
    print( )
    run_again = input("Do you want to choose mode again(yes or no): ")
    if run_again == "no":
            break

print("===============================================================================================================")