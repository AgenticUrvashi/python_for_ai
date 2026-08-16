'que : 3 objects ki list banao aur print karke dekho __repr__ kaise kaam karta hai.'

# restate:3 objects ki list bana kar use __repr se print karo.

# example: list = [TextBook("Chemistry",342),TextBook("Mathematics",230),TextBook("Physics",421)]

# pseudocode:
            # 1.create class TextBook
            # 2.create special method def __init__(self,name,page_no) then self.name = name and self.page_no = page_no
            # 3.create another special method __repr__(self) return f"Name of book:{self.name} , Total Page numbers:{self.page_no}"
            # 4.create object books =   [TextBook("Chemistry",342),TextBook("Mathematics",230),TextBook("Physics",421)]
            # 5.print object.

# translate:
class TextBook:
    def __init__(self,name,page_no) -> None:
        self.name = name
        self.page_no = page_no

    def __repr__(self) -> str:
        return f"Name of book:{self.name} , Total Page numbers:{self.page_no}"

books = [TextBook("Chemistry",342),TextBook("Mathematics",230),TextBook("Physics",421)]

print(books)

# dry run:
# [Name of book:Chemistry , Total Page numbers:342, Name of book:Mathematics , Total Page numbers:230, Name of book:Physics , Total Page numbers:421]
