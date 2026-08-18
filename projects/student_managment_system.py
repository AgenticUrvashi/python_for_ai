'''Features:

Student add karo
Student ki details dekho
Student search karo
Student delete karo
Marks calculate/display karo
Data file me save karo
Invalid input ke liye try-except

Concepts:
class, object, methods, list/dict, functions, file handling, error handling'''


print("=================================Project 1 — Student Management System=======================================")

students = {}

try:

    with open("students.txt","r") as file:
        for line in file:
            student_id, student_name = line.strip().split(":")
            students[student_id] = student_name

except FileNotFoundError:
    print("File nahi mili")

def save_students():
    with open("students.txt","w") as file:
        for student_id,student_name in students.items():
            file.write(student_id + ":" + student_name + "\n")

while True:
    print("=====menu=====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("6. Update Student")
    print("7. Add/Display Marks")

    try:
        choice = int(input("enter your choice: "))
    
    except ValueError as ve:
        print("Invalid input! Please enter a number", ve)

    else:

        if choice == 1:
            student_id = input("Enter student's ID: ")
            student_name = input("Enter student's name: ")

            students[student_id] = student_name,math_marks,physics_marks,chemi_marks

            save_students()
            print("Student added Successfully...!")

        elif choice == 2:
            print(students)

        elif choice == 3:
            student_id = input("enter student's id: ")
            if student_id in students:
                print("student found: ",students[student_id])
            else:
                print("not found...")
        elif choice == 4:
            student_id = input("enter student's id: ")
            if student_id in students:
                students.pop(student_id)

                save_students()           

                print("Student deleted")
            else:
                print("Student not found")

        elif choice == 5:
            print("GoodBye!")
            break

        elif choice == 6:
            student_id = input("enter student's ID: ")
            student_name = input("enter new name: ")

            if student_id in students:
                students[student_id] = student_name, math_marks, physics_marks, chemi_marks

                save_students()

                print("Student updated Successfully!")

            else:
                print("Student not found...")

        elif choice == 7:
            student_id = input("enter student's id: ")
            if student_id in students:
                try:
                    math_marks = int(input("enter Maths marks: "))
                    physics_marks = int(input("enter Physics marks: "))
                    chemi_marks = int(input("enter Chemistry marks: "))

                    total = math_marks + physics_marks + chemi_marks
                    print("Total : ",total)
                    percentage = total / 3
                    print("Percentage : ",percentage)

                except ValueError as ve:
                    print("Invalid marks!",ve)

            else:
                print("Student not found")

        else:
            print("Invalid input")

   
print("=================================End of exicution...!===================================")