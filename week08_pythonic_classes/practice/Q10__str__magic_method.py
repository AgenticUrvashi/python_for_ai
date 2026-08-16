'''Student class banao:

name aur marks attributes rakho.
__str__() method define karo.
Jab Student object ko print() karo, to output aaye:'''

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name : {self.name} , Marks : {self.marks}"

ob = Student("Asha",85)

print(ob)