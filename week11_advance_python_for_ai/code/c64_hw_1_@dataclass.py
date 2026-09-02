'Restate: Ek @dataclass Book banao (title, author, year) aur 2 objects compare karo.'

# example: Book("life","S.J",2008)

# pseudocode:
            # 1.from dataclasses import dataclass
            # 2.write @dataclass
            # 3.class Book: title:str ; author:str ; year:int
            # 4.print(Book("life","S.J",2008) == Book("life","Y.J",2008))
            # 5.print(Book("life","S.J",2008) == Book("life","S.J",2008))

# translate:
from dataclasses import dataclass

@dataclass
class Book:
    title:str
    author:str
    year:int

print(Book("life","S.J",2008) == Book("life","Y.J",2008))
print(Book("life","S.J",2008) == Book("life","S.J",2008))

# dry run:
# False
# True