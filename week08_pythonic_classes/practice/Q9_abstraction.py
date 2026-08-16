'''Shape naam ki abstract class banao:
area() ko abstract method banao.
Circle class ko Shape se inherit karo.
Circle mein area() implement karo.
Circle ka radius constructor se lo.
Area calculate karke return karo.
Formula:
Area = π x radius²'''

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