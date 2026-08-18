'''restate: Book class banao:
title aur price attributes rakho.
__repr__() method define karo.
repr() call karne par output developer-friendly ho.'''

# example: title = success and price = 280

# pseudocode:
            # 1.create class Book
            # 2.create method __init__(self,title,price) then self.title = title and self.price = price
            # 3.create method __repr__(self) return f"Book(title = {self.title}, price = {self.price})"
            # 4.obj = Book("success",200) then print(repr(obj))

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def __repr__(self) -> str:
        return f"Book(title = {self.title}, price = {self.price})"

ob = Book("success",280)
print(repr(ob))

# dry run:
# Book(title = success, price = 280)