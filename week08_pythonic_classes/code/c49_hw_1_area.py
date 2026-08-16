'Square class mein area property banao.'

# restate:area nikalo square ka property use karke.

# example: side = 5

# pseudocode:
            # 1.create class Square.
            # 2.create special method __init__(self,side) then self.side = side
            # 3.write @property
            # 4.create method area(self) return self.side * self.side
            # 5.print Square(5).area

class Square:
    def __init__(self,side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

print(Square(5).area)

# dry run:
25