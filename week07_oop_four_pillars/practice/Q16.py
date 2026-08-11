library = ["ameer","janta","success","humans","psycology"]

class Book:
    def __init__(self,tital,author,availability):
        self.tital = tital
        self.author = author

        self.__availability = True

    def borrow_book(self,book):
        if book in library and self.__availability:
            self.__availability = False
            return "borrow"
        else:
            return "not available"

    def return_book(self,book):
        self.__availability = True
        return book,"is available"

    def get_status(self):
        return self.__availability

