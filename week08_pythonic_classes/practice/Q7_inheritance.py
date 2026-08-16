'''Animal naam ki parent class banao:
Animal mein name attribute ho.
sound() method ho jo "Some sound" return kare.
Dog class ko Animal se inherit karo.
Dog mein sound() override karo aur "Woof" return karo.
Dog ka object banao aur name aur sound() print karo.'''

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