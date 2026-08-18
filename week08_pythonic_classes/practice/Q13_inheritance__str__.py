'''restate: Person parent class banao:
name attribute ho.
__str__() method ho jo "Name: ___" return kare.
Student class ko Person se inherit karo:
marks attribute add karo.
__str__() override karo.'''

# example:name = Urvashi ; marks = 89

# pseudocode:
            # 1.create class Person
            # 2.create method __init__(self,name) then self.name = name
            # 3.create method __str__(self) return f"Name : {self.name}"
            # 4.create class Student(Person)
            # 5.create method __init__(self,name,marks) then super().__init__(name) then self.marks
            # 6.create method __str__(self) return f"Name : {self.name} , Marks : {self.marks}"
            # 7.obj = Student("Urvashi",89) then print(obj)

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

# dry run:
# Name : Urvashi , Marks : 89