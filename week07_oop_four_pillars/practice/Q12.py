# restate:do class banao jisme sound naam ka method common ho pr result alag alag ho for loop se represent karo.

# example:in dog,woof and in cat,meow

# pseudocode:
            # 1.create class Dog then create method sound(self) print woof.
            # 2.create class Cat then create method sound(self) print meow.
            # 3.create obj = [Dog(),Cat()]
            # 4.for animal in animals then animal.sound()

class Dog:
    def sound(self):
        print("woof")


class Cat:
    def sound(self):
        print("meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# dry run:
# woof
# meow