'Ek Student class with name, marks, aur method report() jo report print kare. 2 objects banao.'

# restate: hame ek isa class banana hai jisme student ka report mil sake aur 2 objects banane hai.

# example: name = rahul, anjali  marks = 89, 87

# pseudocode:
            # 1.create class Student.
            # 2.create special method __init__(self,name,marks)
            # 3.store data like self.name = name then self.marks = marks
            # 4.create method report(self) then print(f"{self.name}:{self.marks}")
            # 5.create two objects and give attributes.
            # 6.call objects.report().

# translate:
class Student:
    def __init__(self,name, marks) -> None:
        self.name = name
        self.marks = marks

    def report(self):
        print(f"{self.name} : {self.marks}")

obj1 = Student("rahul",89)
obj2 = Student("anjali",87)

print("---------------")
obj1.report()
print("---------------")
obj2.report()
print("---------------")

# dry run:
# rahul : 89
# anjali : 87