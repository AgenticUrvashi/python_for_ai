'''Ek Employee class banao:

name
private __salary
set_salary(salary) → salary 0 se greater ho tabhi update kare
get_salary() → salary return/print kare

Object banao aur salary update karke check karo.

Isme encapsulation properly use karna hai. 😎'''

# restate:hame class banana hai jisme salary ki value replace/update hogi.

# example:name = ashi, old salary = 300000 , new salary = 400000

# pseudocode:
            # 1.create class Employee.
            # 2.create special method __init__(self,name,salary)
            # 3.create method set_salary(self,salary).if salary>0 then self.__salary=salary, else print invalid.
            # 4.create another method get_salary(self), return self.__salary.
            # 5.create obj = class("ashi",300000)
            # 6.obj.set_salary(400000) and print(obj.get_salary())

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("invalid")

    def get_salary(self):
        return self.__salary

obj = Employee("ashi",300000)

obj.set_salary(400000)
print(obj.get_salary())

# dry run:
400000