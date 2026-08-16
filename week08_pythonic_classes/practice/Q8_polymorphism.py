'''Animal parent class banao:

sound() method rakho.
Dog aur Cat classes ko Animal se inherit karo.
Dono classes mein sound() ko alag-alag override karo.
Dog ka sound "Woof" aur Cat ka sound "Meow" hona chahiye.
Dono objects ke liye same method sound() call karo.'''

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return "some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

u = Dog("tommy")
print(u.name)
print(u.sound())

v = Cat("shera")
print(v.name)
print(v.sound())