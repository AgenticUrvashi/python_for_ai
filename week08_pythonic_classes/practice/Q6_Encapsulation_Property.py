'''Employee class banao:

name aur private __salary rakho.
__init__() constructor se values set karo.
@property se salary ko access karo.
@salary.setter se salary update karo.
Salary 0 se kam nahi honi chahiye.
Agar negative salary di jaye → "Invalid salary" print karo.'''

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

