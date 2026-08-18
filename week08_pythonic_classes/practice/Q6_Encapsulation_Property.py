'''restate : Employee class banao:
name aur private __salary rakho.
__init__() constructor se values set karo.
@property se salary ko access karo.
@salary.setter se salary update karo.
Salary 0 se kam nahi honi chahiye.
Agar negative salary di jaye → "Invalid salary" print karo.'''

# example : name = Tang and salary = 7000000

# pseudocode:
#           1.create class Employee.
#           2.create method __init__(self,name,salary) then self.name = name and self.__salary = salary
#           3.write @property
#           4.create method salary(self) return self.__salary
#           5.write @salary.setter
#           6.create method salary(self,new) if new > 0 : self.__salary = new else: print("invalid salary")
#           7.obj = Employee("Tang",7000000) then print(obj.salary) 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,new):
        if new > 0:
            self.__salary = new
        else:
            print("Invalid salary")

obj = Employee("Tang",7000000)

print(obj.salary)

# dry run:
7000000
