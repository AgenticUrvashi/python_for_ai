'''restate: Shape naam ki abstract class banao:area() ko abstract method banao.
Circle class ko Shape se inherit karo.
Circle mein area() implement karo.
Circle ka radius constructor se lo.
Area calculate karke return karo.
Formula:
Area = π x radius²'''

# example: radius = 7

# psudocode:
            # 1.from abc import ABC, abstractmethod
            # 2.create abstract class Shape(ABC) 
            # 3.write @abstractmethod
            # 4.create method area(self): ...
            # 5.create class Circle(Shape)
            # 6.create method __init__(self,radius) then self.radius = radius
            # 7.create method area(self) return 3.14 * self.radius ** 2
            # 8. obj = Circle(7) then print(obj.area())

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(7)

print(c.area())

# dry run:
153.86