'''Q1. Ek Student class banao jisme:

name
age
course

constructor (__init__) se values set karo aur ek object bana kar teeno values print karo.'''


# restate:class banao usme 3 attribute do aur uski value print karo.

# example:name = ananaya  age = 17  course = CSE

# pseudocode:
            # 1.create class Student.
            # 2.write special method __init__(self,name,age,course)
            # 3.self.name = name, self.age = age, self.course = course
            # 4.create object = class(ananaya,17,CSE)
            # 5.print(obj.name,age,course)

# translate:
class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age 
        self.course = course

    
obj = Student("ananaya",17,"CSE")
print(obj.name)
print(obj.age)
print(obj.course)

# dry run:
# ananaya
# 17
# CSE