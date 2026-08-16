'que:Student class mein __str__ add karo jo "NAME scored MARKS" de.'

# restate:Student naam ki class me __str__ se name scored marks de.

# example: name = Asha, marks = 89

# pseudocode:
            # 1.create class Student.
            # 2.create special method __init__(self,name,marks) then self.name = name and self.marks = marks
            # 3.create another special method __str__(self) then return f"{self.name} scored {self.marks}"
            # 4.then print class with attributes.

# translate:
class Student:
    def __init__(self,name,marks) -> None:
        self.name = name
        self.marks = marks

    def __str__(self) -> str:
        return f"{self.name} scored {self.marks}"

print(Student("Asha",89))

# dry run:

# Asha scored 89