'Shape parent; Triangle aur Square children, dono ka apna area().'

# restate:hame ek shape naam ka parent class banana hai then triangle aur square naam ke child class banao aur apna area nikhalo.

# example: in square,side = 5 and in rectangle, length = 3 , bredth = 4

# pseudocode:
            # 1.create parent class Shape then create area(self) method then pass.
            # 2.create child class Triangle(Shape),create special method __init__(self,base,height),self.base = base,
            #   self.height = height.
            # 3.create another method area(self) return 1/2 * self.base * self.height.
            # 4.create child class Square(Shape),create special method __init__(self,side),self.side = side.create area(self) return
            #   self.side * self.side.
            # 5.obj1 = class(side) and obj2 = class(length,bredth)
            # 6.print obj1.area and print obj2.area

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,base,height) -> None:
        self.base = base
        self.height = height
    def area(self):
        return 1/2 * self.base * self.height

class Square(Shape):
    def __init__(self,side) -> None:
        self.side = side
    def area(self):
        return self.side*self.side

u1 = Square(5)
u2 = Triangle(3,4)

print(u2.area())
print(u1.area())

# dry run:
6.0
25