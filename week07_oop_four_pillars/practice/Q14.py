# restate: person naam ka parent class banao fir child class banao Student naam ki aur usme name aur roll no attributes hone chahiye.
#           name ko print karo aur roll no ko print karo.


class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name,roll_no):
        super().__init__(name)
        self.roll_no = roll_no

s = Student("urvashi",101)
s1 = Student("pashu",11)


print(s.name)
print(s.roll_no)
print(s1.name)
print(s1.roll_no)