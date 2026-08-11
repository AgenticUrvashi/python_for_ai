'Animal parent banao; Cat aur Cow children banao, har ek apni awaaz wala method.'

# restate: parent class Animal banao disme child class cat aur cow ho jisme alag alg aawaj de.

# example: if class cow then the output is meow meow.

# pseudocode:
            # 1.create parent class Animal.
            # 2.create special method __init__(self) then pass.
            # 3.create method speak(self) then print animal bark.
            # 4.create child class Cat.then create method speak(self) then print meow meow.
            # 5.create child class Cow. then create method speak(self) then print moo moo.
            # 6.call child.parent directly.

class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("animal bark")

class Cat(Animal):
    def speak(self):
        print("meow meow!")

class Cow(Animal):
    def speak(self):
        print("moo moo!")

Cat().speak()

Cow().speak()

# dry run:
# meow meow!
# moo moo!