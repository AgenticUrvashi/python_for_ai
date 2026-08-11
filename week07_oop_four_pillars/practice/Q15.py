class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    
    def set_salary(self,salary):
        self.__salary = salary

    def get_salary(self):
        return f"{self.name}:{self.__salary}"

s = Employee("asha",456778).get_salary()

print(s)
