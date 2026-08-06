# Task 11 — Student Records (list of tuples)
# Ek list of tuples banao: [("Asha", 85), ("Rahul", 92), ("Priya", 78)]. Har student ka naam aur marks unpacking se print karo.
#  Phir sabse zyada marks waale ka naam batao.

# Concepts: list of tuples, tuple unpacking in for, running max
# Hint: for name, mark in students: — yeh unpacking hai.

# ans:

print("=============================Student Records (list of tuples)================================")

students =[("Asha", 85), ("Rahul", 92), ("Priya", 78)]


for name,marks in students:
    print(f"{name}:{marks}")

    
print("------------------------------------------------------------------")

studnet = students[1][0]
top_student = max(students)
print(f"the student who is top on class is {studnet}")

print("====================================end the program===========================================")