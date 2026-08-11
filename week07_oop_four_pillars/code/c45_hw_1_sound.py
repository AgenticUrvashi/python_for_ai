'Ek abstract Animal banao with abstract sound(). Dog aur Cat se implement karo.'

# restate: ek abstract class animal banao then sound method banao fir dog aur cat me sound implement karo.

# example:dog = woof woof and cat = meow meow

# pseudocode:
            # 1.import ABC from abc 
            # 2.create abstract class Animal(ABC) then write @abstractmethod. then create sound(self) method then write ...
            # 3.create child class Dog(Animal) then overwrite sound(self) return woof woof.
            # 4.create child class Cat(Animal) then overwrite sound(self) return meow meow.
            # 5.call Dog().sound() and Cat().sound()

# ans:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):
    def sound(self):
        return "woof woof!"

class Cat(Animal):
    def sound(self):
        return "meow meow!"

print(Dog().sound())
print(Cat().sound())

# dry run:
# woof woof
# meow meow