# Student Report Card Generator — 
# Ek list of dicts banao jisme har student ka name aur teen subjects ke marks (ek list) ho.
#  Har student ke liye: total, average, aur grade (A/B/C/D) nikaalo. Sabse aakhir mein class topper aur class average batao.
#  Original data safe rakhne ke liye kaam karne se pehle copy.deepcopy() use karo.

# Concepts: list of dicts, nested list, loops, sum()/len(), if/elif/else, sorted(key=...), copy.deepcopy
# Yeh capstone hai — agar aap yeh khud bina notes ke bana lete ho, toh aapne Week 1-4 sach mein master kar liya. 💪

print("********************************************************************************************************")
print("===================================STUDENT REPORT CARD GERERATOR========================================")
print("******************************************************************************************************")

students=[
    {
        "name":"mohan",
        "marks":[56,89,56]
        },
    {
        "name":"rama",
        "marks":[82,64,87]
        },
    {
        "name":"mira",
        "marks":[56,87,51]
        }
]

import copy

students_copy = copy.deepcopy(students)


for student in students_copy:
    
    total = sum(student["marks"])
    avgerage = total / len(student["marks"])

    if avgerage>=90:
        grade ="A"
    elif avgerage>=80:
        grade ="B"
    elif avgerage>=70:
        grade ="C"
    else:
        grade ="D"

    # print(f"name:{(student["name"])}, grade: {grade}")

    student["total"]= total
    student["avg"]= avgerage
    student["grade"]= grade

class_topper = sorted(
        students_copy,
        key=lambda student:student["total"],
        reverse=True
)

class_avg = sum(student["avg"] for student in students_copy)/len(students_copy)

print("~~~~~~~~~~~~~~~~~~~")

print("STUDENT REPORT: ")

print("~~~~~~~~~~~~~~~~~~~")
for student in students_copy:
    print(student)
    
print()

print("***********************************************************************************************************")
print()

print("Topper:", class_topper[0]["name"])
print()

print("************************************************************************************************************")
print()

print("class avgerage: ", class_avg)
print()

print("=============================================================================================================")
print("                                               **thank you**                                                 ")
print("=============================================================================================================")


