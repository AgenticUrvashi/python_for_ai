'Shape parent (with name); Square aur Rectangle children with super().'

# restate: shape naam ka parent class banao aur Square aur rectangle naam ke do child classes usme super() ka use dikhao.

# examale: in square, side = 5 and in rectangle, length = 4, bredth = 5

# pseudocode:
            # 1.create parent class Shape then self.name = name.
            # 2.create child class Square then create special method __init__(self,name,side) then super()__init__(name) then
            #   self.side = side.
            # 3.create another method area(self) then print self.side*self.side
            # 4.create another child class Rectangle then  create special method __init__(self,name,length,bredth) then 
            #   super()__init__(name) then self.length = length and self.bredth = bredth.
            # 5.create obj = child class1(name,side) and obj1 = child class2(name,length,bredth) then class.area() and class.area()
            # 6.print class.name and print class.side

class Shape:
    def __init__(self,name):
        self.name = name
    
class Square(Shape):
    def __init__(self,name,side):
        super().__init__(name)
        self.side = side
    def area(self):
        print(self.side * self.side)

class Rectangle(Shape):
    def __init__(self, name, length, bredth):
        super().__init__(name)
        self.length = length
        self.bredth = bredth
    def area(self):
        print(self.length * self.bredth)

d1 = Square("Square",5)
d2 = Rectangle("Rectangle",4,5)

d1.area()
d2.area()

print(d1.name)
print(d1.side)

# dry run:
# 25
# 20    
# Square
# 5     

