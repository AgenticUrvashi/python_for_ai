'''Ek Employee system banao:

Person naam ki parent class ho, jisme name ho.
Employee class Person se inherit kare.
Employee mein private __salary ho.
salary ko @property se access karo.
Setter mein salary 0 se kam ho to "Invalid salary" print karo.
__str__() override karke naam aur salary dono print karo.'''


class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
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

    def __str__(self):
        return f"{self.name} have salary of rupees {self.__salary}"

h = Employee("urvashi",300000)

print(h)

h.salary = 4000000

print(h)

