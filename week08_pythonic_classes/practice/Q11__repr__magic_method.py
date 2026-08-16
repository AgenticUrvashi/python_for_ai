'''Book class banao:

title aur price attributes rakho.
__repr__() method define karo.
repr() call karne par output developer-friendly ho.'''

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def __repr__(self) -> str:
        return f"Book(title = {self.title}, price = {self.price})"

ob = Book("success",280)
print(repr(ob))