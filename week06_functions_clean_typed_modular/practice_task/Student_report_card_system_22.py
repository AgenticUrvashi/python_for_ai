'''EN: Write total(marks), average(marks), and grade(avg) functions. Loop over a list of students 
(each a dict with name and a list of 3 subject marks) and print a full report line for each. 
At the end print the class topper.
हिंदी: total(marks), average(marks), और grade(avg) functions बनाओ। students की list 
(हर एक dict जिसमें name और 3 subjects के marks की list हो) पर loop चलाकर हर student की पूरी report line print करो। 
आख़िर में class topper print करो।
Concepts: functions on lists, loop over list of dicts, running max
Hint: total = sum(marks), average = total / len. Track topper with a max-average variable.'''

# restate: 3 function banao jo student ki report card bana ke de aur last me class topper ka naam print kare.

# example: 

# pseudocode:
            # 1.create 3 functions total , average , grade.
            # 2.create variable students.
            # 3.create variable highest_marks = 0 and topper_name = ""
            # 4.use for loop for students
            # 5.print output with the help of f-string.
            # 6.if total > highest then topper = student[name]
            # 7.print output with the help of f-string.

# translate:

def total(marks):
    return sum(marks)

def average(marks):
    avg = sum(marks)/len(marks)
    return avg

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

print("=================================== STUDENT REPORT CARD =====================================")

students = [
    {"name":"Asha" , "marks":[45,78,34]},
    {"name":"Shobha" , "marks":[56,78,90]},
    {"name":"Jon" , "marks":[45,78,69]}
]

highest_marks = 0

topper_name = ""

for student in students:
    total_marks = total(student["marks"])

    avge = average(student["marks"])

    gra = grade(avge)


    print(f"Name : {student['name']} , Total : {total_marks} , Average : {avge} , Grade : {gra}")
    print( )


    if total_marks > highest_marks:
        highest_marks = total_marks

        topper_name = student["name"]

print("========================================topper name==========================================")
print( )

print(f"topper name : {topper_name} got {highest_marks}, congratulations!!!")

print( )

print("======================================== THANK YOU =========================================")

# dry run:
# =================================== STUDENT REPORT CARD =====================================
# Name : Asha , Total : 157 , Average : 52.333333333333336 , Grade : D

# Name : Shobha , Total : 224 , Average : 74.66666666666667 , Grade : C

# Name : Jon , Total : 192 , Average : 64.0 , Grade : D

# ========================================topper name==========================================

# topper name : Shobha got 224, congratulations!!!

# ======================================== THANK YOU ========================================= 
