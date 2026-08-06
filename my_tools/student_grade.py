def get_grade(marks):

    if marks >= 90:

        return "A"

    elif marks >= 75:

        return "B"

    elif marks >= 60:

        return "C"

    else:

        return "D"


students = {"Asha": 92, "Rahul": 70, "Priya": 81}

for name, marks in students.items():

    print(f"{name}: Grade {get_grade(marks)}")
