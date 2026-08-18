'''Restate : Ek Shape system banao:
Shape ko abstract class banao.
Usme abstract method area() ho.
Rectangle class Shape se inherit kare.
Rectangle mein length aur width ho.
area() implement karo.
__str__() se rectangle ka area print karo.'''


# example: length = 6 and width = 8

# pseudocode:
            # 1.from abc import ABC , abstractmethod
            # 2.create class Shape(ABC) then write @abstractmethod then create method area(self): ...
            # 3.create class Rectangle(Shape)
            # 4.create method __init__(self,length,width) then self.length = length and self.width = width
            # 5.create method area(self) return self.length * self.width
            # 6.create method __str__(self) return f"the area of reactangle is {self.length*self.width}"
            # 7.obj = rectangle(6,8) then print(a)

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

# dry run:
# the area of rectangle is 48