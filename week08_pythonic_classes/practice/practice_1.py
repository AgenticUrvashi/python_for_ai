'Aisa function banao jo list mein kitne even numbers hain ye return kare.'

# ans:
def count_even(n):
    count = 0
    for i in n:
        if i % 2 == 0:
            count += 1
    print(count)

count_even([1, 2, 4, 7, 8])


'''Ek Student class banao jisme:
name aur marks constructor mein aaye
self.name aur self.marks mein store ho
show() method ho jo name aur marks return kare'''

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def show(self):
        return f"{self.name} : {self.marks}"

s = Student("Asha",89)

print(s.show())