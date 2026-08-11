'''Student class banao:

name
private __marks
set_marks(marks) → marks 0 se 100 ke beech ho tabhi update kare
get_marks() → marks return kare

Object banao, marks set karo aur print karo.'''

# restate:class banao student __marks private banao use update kare if marks is in range 0 to 101.

# example: name = Rahul, old marks = 67, new marks = 78

# pseudocode:
            # 1.create class Student.
            # 2.create special method __init__(self,name,marks).
            # 3.create method set_marks(self,marks).if marks in range(0,101) then self.__marks = marks,else print invalid input.
            # 4.create method get_marks(self) then return self.__marks.
            # 5.object = class("Rahul",67) and obj.set_marks(78) then print(obj.get_marks())

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def set_marks(self,marks):
        if marks in range(0,101):
            self.__marks = marks
        else:
            print("invalid input")

    def get_marks(self):
        return self.__marks

obj = Student("Rahul",67)
obj.set_marks(78)
print(obj.get_marks())

# dry run
78