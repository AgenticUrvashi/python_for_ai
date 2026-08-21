# 🟢 Level 1 — Easy

# Q1. User se 2 numbers input lo aur divide karo.

# Agar user number ki jagah text dale → "Invalid input" print karo.
# Agar second number 0 ho → "Cannot divide by zero" print karo.

print("-------------------------Q1----------------------------")

try:
    a = int(input("enter number = "))
    b = int(input("enter any number = "))
    print(a/b)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

print("-------------------------Q2----------------------------")

# Q2
# User se age input lo.
# Requirements:
# Age ko int mein convert karo.
# Agar user "abc" ya koi text dale → Invalid age print ho.
# Agar age successfully input ho → Your age is: ... print ho.
# Hint: Sirf ValueError handle karna hai.

try:
    age = int(input("enter age: "))

except ValueError:
    print("Please enter a valid age")

else:
    print(f"your age is {age}")

print("----------------------------Q3---------------------------")

# Q3:Given:
# numbers = [10, 20, 30, 40, 50]
# User se index input lo aur element print karo.
# Handle 2 errors:
# User text dale → "Enter a valid number"
# Index list mein na ho → "Index not found"
# Example:Enter index: 2
# 30

try:
    numbers = [10, 20, 30, 40, 50]
    ind = int(input("enter index: "))
    print(numbers[ind])

except ValueError:
    print("Enter a valid number")

except IndexError:
    print("Index not found")

print("-------------------------Q4------------------------")

# 🟡 Level 2 — Medium

# Q4 — File Handling + Error Handling
# Ek file "students.txt" open karo aur uska content print karo.
# Requirements:
# File nahi mili → "File not found"
# File mil gayi → content print karo
# try-except use karo
# Hint: FileNotFoundError

try:
    with open("students.txt","r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

print("------------------------------Q5-------------------------------")

# Q5. Dictionary:
# Ye dictionary use karo:
# students = {
#     "101": "Riya",
#     "102": "Tina",
#     "103": "Anu"
# }
# User se student ID input lo aur naam print karo.
# Handle karo:
# Student ID exist nahi karti → "Student not found"
# Hint: KeyError
# Example: Enter student ID: 102
# Tina

try:
    students = {
        "101": "Riya",
        "102": "Tina",
        "103": "Anu"
    }

    student_id = input("enter student's ID: ")
    print(students[student_id])

except KeyError:
    print("Student not found")

print("------------------------------Q6----------------------------")

# 🔴 Level 3 — Tumhare Student Management Project jaisa
# Q6 — Marks Validation
# Ab thoda real project-level practice:
# User se 3 marks lo:
# Maths:
# Physics:
# Chemistry:
# Handle karo:
# Marks text ho → "Marks must be numbers"
# Marks 0 se kam ya 100 se zyada ho → "Marks must be between 0 and 100"
# Valid marks ho → Total aur Percentage print karo
# Example:
# Maths: 80
# Physics: 70
# Chemistry: 90
# Total: 240
# Percentage: 80.0
# 💡 Hint: ValueError + if condition use karni hai.

try:
    math = int(input("enter maths marks: "))
    phy = int(input("enter physics marks: "))
    chemi = int(input("enter chemistry marks: "))
    if 0 > math or math > 100:
        print("Marks must be between 0 and 100")
    elif 0 > phy or phy > 100:
        print("Marks must be between 0 and 100")
    elif 0 > chemi or chemi >100:
        print("Marks must be between 0 and 100")
    else:
        total = math + phy + chemi
        percent = total / 3
        print("Total: ",total)
        print("Percentage: ",percent)
    

except ValueError:
    print("Marks must be numbers")

print("---------------------------Q7---------------------------")

# Q7. Challenge 🔥
# Ek program banao jisme user se:
# Student ID:
# Student Name:
# Maths:
# Physics:
# Chemistry:
# input liya jaye.
# Handle karo:
# ValueError
# Duplicate Student ID
# Marks 0–100 ke bahar
# Empty student name
# Unexpected error

# or

# Ek student ka ID, name aur marks input lo aur handle karo:

# Duplicate ID → Student already exists
# Marks text → Marks must be numbers
# Marks 0–100 ke bahar → Invalid marks
# Student name empty ho → Name cannot be empty

# Isme tumhe KeyError + ValueError + conditions combine karne hain.

try:
    students = {
    "101": "Riya",
    "102": "Tina"
    }
    student_id = input("enter student's ID: ")
    student_name = input("enter student's name: ")

    if student_id in students:
        print("Studnet already exist")

    elif student_name == "":
        print("Name cannot be empty")

    else:

        math = int(input("enter maths marks: "))
        phy = int(input("enter physics marks: "))
        chemi = int(input("enter chemistry marks: "))

        if 0 > math or math > 100:
            print("Marks must be between 0 and 100")

        elif 0 > phy or phy > 100:
            print("Marks must be between 0 and 100")

        elif 0 > chemi or chemi >100:
            print("Marks must be between 0 and 100")

        else:
            students[student_id] = student_name

            total = math + phy + chemi
            percent = total / 3
            
            print("Studnet added successfully")
            print("Total: ",total)
            print("Percentage: ",percent)
    

except ValueError:
    print("Marks must be numbers")

except KeyError:
    print("Invalid input")

print("---------------------------Q8----------------------------")

# Ek program banao jisme students ki dictionary already given ho:

students = {
    "101": {"name": "Riya", "marks": 85},
    "102": {"name": "Tina", "marks": 92}
}

# User se Student ID input lo aur us student ki details print karo.
# Program ko ye errors handle karne chahiye:
# 🔹 Student ID dictionary mein nahi hai → KeyError
# Print: Student not found
# 🔹 User ne ID ki jagah kuch invalid type diya → ValueError
# Print: Student ID must be a number
# 🔹 Student ke marks ko user se update karne ke liye input lo.
# Agar marks text hain → ValueError
# Print: Marks must be numbers
# 🔹 Marks 0–100 ke bahar hain → condition se handle karo
# Print: Marks must be between 0 and 100
# Agar sab correct hai:
# Marks update karo
# Print: Student updated successfully
# 🎯 Concepts
# Isme tumhe use karna hai:
# try + except ValueError + except KeyError + if/elif/else
# Hint: KeyError ke liye dictionary ko direct key se access karna padega:
# students[student_id]

try:
    students = {
    "101": {"name": "Riya", "marks": 85},
    "102": {"name": "Tina", "marks": 92}
    }

    user_id = input("enter user's ID: ")
    print(students[user_id]["marks"])
    user_input = int(input("enter new marks: "))
    if user_input < 0 or user_input > 100:
        print("marks must be between 0 to 100")
    else:
        students[user_id]["marks"] = user_input
        print("Updated successfully...")

except KeyError:
    print("Student not found")

except ValueError:
    print("Studnet's marks must be number")

print("-------------------------------Q9----------------------------")

# Ab Update Student Name ka code khud likho.

# Requirement:

# ID input lo
# Student nahi mila → "Student not found"
# New name input lo
# Empty name → "Name cannot be empty"
# Otherwise name update karo
# "Updated successfully" print karo

try:
    students = {
    "101": {"name": "Riya", "marks": 85},
    "102": {"name": "Tina", "marks": 92}
    }

    user_id = input("enter user's ID: ")
    print(students[user_id]["marks"])

    user_input = int(input("enter new marks: "))

    if user_input < 0 or user_input > 100:
        print("marks must be between 0 to 100")

    else:
        students[user_id]["marks"] = user_input
        print("Updated successfully...")

        new_name = input("enter new name: ")
        if new_name == "":
            print("name cannot be empty")
    
        else:
            students[user_id]["name"] = new_name
            print("Updated successfully...")

except KeyError:
    print("Student not found")

except ValueError:
    print("Studnet's marks must be number")
