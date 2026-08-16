'que : Circle mein diameter property banao (2 * radius).'

# restate: circle naam ka class banake diameter naam ka propery banao usme 2*radius return karo.

# example: radius = 4 

# pseudocode:
            # 1.create class Circle.
            # 2.create special method __init__(self,radius) then self.radius = radius
            # 3.write @property
            # 4.create method diameter(self) return 2 * self.radius
            # 5.obj = Circle(4) print(obj.diameter)

# translate:
class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

obj = Circle(4)
print(obj.diameter)

# dry run:
8
