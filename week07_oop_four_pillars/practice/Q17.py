class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks

    def get_result(self):
        if self.__marks >= 40:
            return "Pass"
        else:
            return "Fail"

s = Student("asha",192,67).get_result()
print(s)
s1 = Student("riya",563,34).get_marks()
print(s1)