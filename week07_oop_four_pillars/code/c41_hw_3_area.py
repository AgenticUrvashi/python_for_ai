'Ek Circle class with radius aur method area() jo area return kare.'

# restate:ek isa class banana hai jo circle ka area return kare.

# example: radius = 7

# pseudocode:
            # 1.import pi from maths.
            # 2.create class Circle.
            # 3.create special method __init__(self,radius)
            # 4.self.radius = radius
            # 5.create method area(self)
            # 6.print(pi*radius**2)
            # 7.craete object cir = Circle(7)
            # 8.call the object. cir.area()

# translate:
from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(pi*self.radius**2)

cir = Circle(7)

cir.area()

# dry run:
153.83