'que: Book class (title, author) mein __repr__ add karo.'

# restate: class banao book nam ki with tital and author then usme __repr__ add karo.

# example: tital = Mindset author = Carol S. Dweck

# pseudocode:
            # 1.create class Book
            # 2.create special method __init__(self,title,author) then self.title = title , self.author = author
            # 3.create another special method __repr__(self) return f"Title: {self.title}, Author: {self.author}"
            # 4.print the class with attributes

# translate:
class Book:
    def __init__(self,title, author) -> None:
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}"

print(Book("Mindset", "Carol S. Dweck"))

# dry run:
# Title:Mindset , Author:Carol S. Dweck