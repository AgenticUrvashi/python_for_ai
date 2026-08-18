'''Restate: Ek Employee system banao:
Person naam ki parent class ho, jisme name ho.
Employee class Person se inherit kare.
Employee mein private __salary ho.
salary ko @property se access karo.
Setter mein salary 0 se kam ho to "Invalid salary" print karo.
__str__() override karke naam aur salary dono print karo.'''

# example : name = urvashi , salary = 300000 and new = 4000000

# pseudocode:
            # 1.create class Person
            # 2.create method __init__(self,name) then self.name = name
            # 3.create class Employee(Person)
            # 4.create method __init__(self,name,salary) then super().__init__(name) then self.__salary = salary
            # 5.write @property
            # 6.create method salary(self) return self.__salary
            # 7.write @salary.setter
            # 8.overwrite method salary(self,new)
            # 9.if new > 0 : self.__salary = new 
            # 10.else: print("invalid salary")
            # 11.create method __str__(self) return f"{self.name} have salary of rupees {self.__salary}"
            # 12.obj = Employee("urvashi",3000000) then print(obj)
            # 13.obj.salary = 40000000 then print(obj)

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

# dry run:
# urvashi have salary of rupees 300000
# urvashi have salary of rupees 4000000