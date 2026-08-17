'''Ek Animal system banao:

Animal parent class ho.
Dog aur Cat classes Animal se inherit karein.
Dog aur Cat dono mein sound() method ho, lekin dono ka output alag ho.
Animal mein name attribute ho.
__str__() ka use karke animal ka name print karo.
Dono objects ke sound() ko call karo.'''

class Animal:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Name : {self.name}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Sound : Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        return "Sound : Meow"



s = Dog("tommy")

print(s)

print(s.sound())


