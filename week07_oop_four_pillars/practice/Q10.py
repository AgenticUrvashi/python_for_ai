'''restate : Ek abstract class Animal banao:sound() naam ka abstract method ho.Dog class Animal se inherit kare.
Dog mein sound() implement karo. Hint: ABC aur @abstractmethod use karna hai.

example : Output "Woof Woof" print karo.'''

# pseudocode:
            # 1.from abc import ABC , abstractmethod
            # 2.create abstract class Animal(ABC) then @abstractmethod, create method sound(self) then ...
            # 3.create child class Dog(Animal) then overwrite sound(self) then print woof woof
            # 4.call child class().method()

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):
    def sound(self):
        print("woof woof!")

Dog().sound()

# dry run:
# woof woof