'''restate : Student class banao: name aur _marks attributes rakho.@property ka use karke marks ko access karo.
Agar marks ko change karein, to value 0 se 100 ke beech honi chahiye.Student object banao aur marks print karo.
Hint: @property ke saath @marks.setter use karna.'''

# example: old = 78 and new = 90

# pseudocode:
            # 1.create class Student
            # 2.create special method __init__(self,name,marks) then self.name = name and self_marks = marks
            # 3.write @property
            # 4.create method marks(self) return self._marks 
            # 5.write @marks.setter
            # 6.overwrite method marks(self,value) then if value in range(0,101) self._marks = value
            # 7.obj = Student("Asha",78) print(obj.marks)
            # 8.obj.marks = 90 print(obj.marks)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if value in range(0,101):
            self._marks = value
    

obj = Student("Asha",78)

print(obj.marks)

obj.marks = 90

print(obj.marks)

# dry run:
78
90
