'''Person parent class banao:

name attribute ho.
__str__() method ho jo "Name: ___" return kare.

Student class ko Person se inherit karo:

marks attribute add karo.
__str__() override karo.'''

# translate:

class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Name : {self.name}"

class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks

    def __str__(self):
        return f"Name : {self.name} , Marks : {self.marks}"


obje = Student("Urvashi",89)

print(obje)