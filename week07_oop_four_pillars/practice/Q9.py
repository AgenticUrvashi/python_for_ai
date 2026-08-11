'''restate :Ek abstract class Shape banao.Usme abstract method area() hona chahiye.Circle class Shape se inherit kare.
Circle mein area() implement karo.

example: Circle ka radius 5 rakho.area() call karke result print karo.'''

# pseudocode:
            # 1.import ABC from abc then write abstractmethod.
            # 2.create abstract class Shape(ABC). then @abstractmethod then create abstract method area(self) and ...
            # 3.create child class Circle(Shape). overwrite method area(self,radius) then print 3.14 * radius ** 2.
            # 4.call the class circle and method area with radius.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def area(self,radius):
        print(3.14 * radius**2)

Circle().area(5)

# dry run:
78.5

