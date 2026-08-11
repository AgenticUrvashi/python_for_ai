'Employee parent (name, salary); Manager child jo super() use kare aur ek team_size add kare.'

# restate:parent class banao employee naam ki aur uska child class banao with the help of super and add team_size.

# example: name = ravi, salary = 400000, team_size = 9

# pseudocode:
            # 1.create parent class Employee.then write special method __init__(self,name,salary)
            # 2.create child class Manager(Employee) then create special method __init__(self,name,salary,team_size)
            # 3.then use super().__init__(name,salary) then self.team_size = team_size
            # 4.create object = child(name,salary,team_size)
            # 5.print obj.name , print obj.salary , print obj.team_size.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size = team_size

person = Manager("ravi",400000,9)

print(person.name)
print(person.salary)
print(person.team_size)

# dry run:
# ravi
# 400000
# 9     