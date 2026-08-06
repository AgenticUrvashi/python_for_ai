'''EN: Write get_grade(marks) returning "A"/"B"/"C"/"D". 
Then loop over a dict of students {"Asha": 92, "Rahul": 70, "Priya": 81} and print each student's grade using the function.
हिंदी: get_grade(marks) बनाओ जो "A"/"B"/"C"/"D" return करे। 
फिर students के dict {"Asha": 92, "Rahul": 70, "Priya": 81} पर loop चलाकर हर student का grade function से print करो।
Concepts: return, if/elif/else, reusing a function in a loop, dict .items()
Hint: >= 90 → A, >= 75 → B, >= 60 → C, else D.'''

# restate: ek function banao jo if/elif/else condition se grade bataye.

# example: if shenha got 79 marks then the grade is C.

# psudocode:
            # 1.create function get_grade(marks).
            # 2.if marks >= 90 return A
            # 3.if marks >= 80 return B
            # 4.if marks >= 70 return C
            # 5.else return D
            # 6.take dict.
            # 7.use for loop for dict.
            # 8.print grade and name with the help of f-string.

# translate:
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"

students = {"Asha": 92, "Rahul": 70, "Priya": 81}

for name , marks in students.items():

    print(f"{name}, Grade: {get_grade(marks)}")


# dry run:
# Asha, Grade A
# Rahul, Grade C
# Priya, Grade B
