'''Ek Shape system banao:

Shape ko abstract class banao.
Usme abstract method area() ho.
Rectangle class Shape se inherit kare.
Rectangle mein length aur width ho.
area() implement karo.
__str__() se rectangle ka area print karo.'''

from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        ...

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        

    def __str__(self):
        return f"the area of rectangle is {self.length*self.width}"


a = Rectangle(6,8)

print(a)