'''Restate: Ek Animal system banao:
Animal parent class ho.
Dog aur Cat classes Animal se inherit karein.
Dog aur Cat dono mein sound() method ho, lekin dono ka output alag ho.
Animal mein name attribute ho.
__str__() ka use karke animal ka name print karo.
Dono objects ke sound() ko call karo.'''

# example: name = tommy

# pseudocode:
            # 1.create class Animal
            # 2.create method __init__(self,name) then self.name = name
            # 3.create method __str__(self) return f"Name :{self.name}"
            # 4.create class Dog(Animal)
            # 5.create method __init__(self,name) then super().__init__(name)
            # 6.create method sound(self) return "Sound : Woof"
            # 7.create class Cat(Animal)
            # 8.create method __init__(self,name) then super().__init__(name)
            # 9.create method sound(self) return "Sound : Meow"
            # 10.obj = Dog("tommy") then print(obj) and print(obj.sound())

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

# dry run:
# Name : tommy
# Sound : Woof