'''restate : Student class banao:
name aur marks attributes rakho.
__str__() method define karo.
Jab Student object ko print() karo, to output aaye:'''

# example: name = Asha and marks = 85

# pseudocode:
            # 1.create class Student
            # 2.create method __init__(self,name,marks) then self.name = name and self.marks = marks
            # 3.create method __str__(self) return f"Name : {self.name} , Marks : {self.marks}
            # 4.obj = Student("Asha",85) then print(obj)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name : {self.name} , Marks : {self.marks}"

ob = Student("Asha",85)

print(ob)

# dry run:
# Name : Asha , Marks : 85