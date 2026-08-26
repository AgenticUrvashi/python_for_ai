'restate: Ek CSV file 3 students ke naam+marks ke saath banao aur DictReader se padho.'

# example:Asha,87,Rahul,89,Anju,90

# pseudocode:
            # 1.import csv
            # 2.students = [["Name","Marks"],["Asha",87],["Rahul",89],["Anju",90]]
            # 3.with open('hw_3_students.csv','w',encoding="utf-8") as f:
            # 4.writer = csv.writer(f) then writer.writerows(students)
            # 5.with open('hw_3_students.csv','r',encoding="utf-8") as f:
            # 6.reader = csv.DictReader(f) then for row_dict in reader:
            # 7.print(row_dict["Name"],row_dict["Marks"]) 

import csv
students = [
    ["Name","Marks"],
    ["Asha",87],
    ["Rahul",89],
    ["Anju",90]
]
with open('hw_3_students.csv','w',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open('hw_3_students.csv','r',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row_dict in reader:
        print(row_dict["Name"],row_dict["Marks"])

# dry run:
# Name,Marks

# Asha,87

# Rahul,89

# Anju,90

