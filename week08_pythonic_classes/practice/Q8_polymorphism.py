'''restate : Animal parent class banao:
sound() method rakho.
Dog aur Cat classes ko Animal se inherit karo.
Dono classes mein sound() ko alag-alag override karo.
Dog ka sound "Woof" aur Cat ka sound "Meow" hona chahiye.
Dono objects ke liye same method sound() call karo.'''

# example: name = tommy and shera

# pseudocode:
            # 1.create class Animal
            # 2.create method __init__(self,name) then self.name
            # 3.create method sound(self) return "some sound"
            # 4.create class Dog(Animal) 
            # 5.create method sound(self) return "Woof"
            # 6.create class Cat(Animal)
            # 7.create method sound(self) return "Meow"
            # 8.u = Dog("tommy") then print(u.name) and print(u.sound())
            # 9.v = Cat("shera") then print(v.name) and print(v.sound())

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

# dry run:
# tommy
# Woof 
# shera
# Meow 