# restate: parent class Shape banao area method common banao child classes me circle aur rectangle me.aur area print karo.

# example:r=5 and length = 4, bredth = 5

# pseudocode:
            # 1.create parent class Shape.then create method area(self):
            # 2.create child class Circle.then create special method__init__(self,r),self.r=r then area(self) return 3.14*self.r**2.
            # 3.create child class rectangle. then create special method__init__(self,length,bredth), then area(self) return 
            #   self.length * self.bredth.
            # 4.craete obj = [circle(5),rectangle(4,5)]
            # 5.for a in areas print(a.area())

class Shape:
    '''
    Shape:
        parent class
    area:
        common method
    self:
        attribute
    '''
    def area(self):
        pass

class Circle(Shape):
    '''
    Circle:
        child class inherit from parent Shape
    __init__:
        constructor or the special method
    r and self:
        attributes
    area:
        the area return area of circle only pass radius attribute
    '''
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*self.r**2

class Rectangle(Shape):
    '''
    Rectangle:
        child class inherit from parent Shape
    __init__:
        constructor or special method
    length , bredth , self:
        attributes
    area:
        the area return area of rectangle only pass length and bradth attributes
    '''
    def __init__(self,length,bredth):
        self.length = length
        self.bredth = bredth

    def area(self):
        return self.length * self.bredth

areas = [Circle(5),Rectangle(4,5)]

for a in areas:
    print(a.area())

# dry run:
78.5
20