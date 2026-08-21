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

# --------------------------------------------------------------------------------------------------------------------------------

print("=================================Project 1 — Student Management System=======================================")

students = {}

try:

    with open("students.txt","r") as file:
        for line in file:
            parts = line.strip().split(":")


            student_id = parts[0]
            student_name = parts[1]
            maths = parts[2]
            physics = parts[3]
            chemistry = parts[4]

            students[student_id] = {
                "name": student_name,
                "maths": None if maths == "None" else int(maths),
                "physics": None if physics == "None" else int(physics),
                "chemistry": None if chemistry == "None" else int(chemistry)
            }

except FileNotFoundError:
    print("File nahi mili")

def save_students():
    with open("students.txt","w") as file:
        for student_id, details in students.items():
            file.write(
                student_id + ":" +
                details["name"] + ":" +
                str(details["maths"]) + ":" +
                str(details["physics"]) + ":" +
                str(details["chemistry"]) + "\n"
            )

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

            students[student_id] = {
                "name" : student_name,
                "maths": None,
                "physics" : None,
                "chemistry" : None
            }

            save_students()
            print("Student added Successfully...!")

        elif choice == 2:
            for student_id,details in students.items():
                print("------------------------------")
                print("ID :", student_id)
                print("Name :", details["name"])
                print("Maths :", details["maths"])
                print("Physics :", details["physics"])
                print("Chemistry :", details["chemistry"])

                if details["maths"] is None:
                    print("no marks is available")

                else:
                    total = details["maths"] + details["physics"] + details["chemistry"]
                    percentage = total/3
                    print("Total : ",total)
                    print("Percentage :", percentage)


        elif choice == 3:
            student_id = input("enter student's id: ")
            if student_id in students:
                details = students[student_id]

                print("-----------------------------------")
                print("Student Found!")
                print("ID :", student_id)
                print("Name :", details["name"])
                print("Maths :", details["maths"])
                print("Physics :", details["physics"])
                print("Chemistry :", details["chemistry"])
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
                students[student_id]["name"] = student_name

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

                    students[student_id]["maths"] = math_marks
                    students[student_id]["physics"] = physics_marks
                    students[student_id]["chemistry"] = chemi_marks

                    total = math_marks + physics_marks + chemi_marks
                    print("Total : ",total)

                    percentage = total / 3
                    print("Percentage : ",percentage)

                    save_students()

                except ValueError as ve:
                    print("Invalid marks!",ve)

            else:
                print("Student not found")

        else:
            print("Invalid input")

   
print("=================================End of exicution...!===================================")