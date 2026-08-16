'''restate : Library class banao jo Book aur Author objects rakhe (composition).Book class mein title aur price ho.
Author class mein name ho.Library ke andar Book aur Author ke objects create karo.Last mein title, price aur author name print karo.'''

# example: title = python , price = 500 , name = Tang

# pseudocode:
            # 1.create class Book.
            # 2.create special method __init__(self,title,price) then self.title = title and self.price = price
            # 3.create class Author
            # 4.create special method __init__(self,name) then self.name = name
            # 5.create class Library
            # 6.create special method __init__(self) then self.Book = Book("python",500) and self.Author = Author("Tang")
            # 7.create another method get(self) 
            # 8.return f"the book {self.Book.title} and author is {self.Author.name}, price is {self.Book.price}"
            # 9.obj = Library() then print(obj.get())

# translate:
class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price
class Author:
    def __init__(self,name):
        self.name = name

class Library:
    def __init__(self):
        self.Book = Book("python",500)
        self.Author = Author("Tang")

    def get(self):
        return f"the book {self.Book.title} and author is {self.Author.name}, price is {self.Book.price}"

lib = Library()
print(lib.get())

# dry run:
"the book python and author is Tang , price is 500"