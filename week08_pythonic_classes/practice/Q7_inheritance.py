'''restate: Animal naam ki parent class banao:
Animal mein name attribute ho.
sound() method ho jo "Some sound" return kare.
Dog class ko Animal se inherit karo.
Dog mein sound() override karo aur "Woof" return karo.
Dog ka object banao aur name aur sound() print karo.'''

# example: name = royal and Royal

# pseudocode:
            # 1.create class Animal
            # 2.create method __init__(self,name) then self.name = name
            # 3.create method sound(self) return "Some sound"
            # 4.create class Dog(Animal)
            # 5.create method sound(self) return Woof
            # 6.d = Animal("royal") then print(d.name) and print(d.sound())
            # 7.D = Dog("Royal") then print(D.name) and print(D.sound())

class Animal:

    def __init__(self,name):
        self.name = name

    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

d = Animal("royal")
print(d.name)
print(d.sound())

D = Dog("Royal")
print(D.name)
print(D.sound())

# dry run:
# royal
# Some sound
# Royal     
# Woof      