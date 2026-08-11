'Jaan-boojh kar ek child banao jo sound() na likhe — error padho.'

# restate: ek abstract class animal banao then sound method banao fir isa class banao jisme sound na ho aur error dikhao.

# example: bird() then find error

# pseudocode:
            # 1.import ABC from abc 
            # 2.create abstract class Animal(ABC) then write @abstractmethod. then create sound(self) method then write ...
            # 3.create child class Dog(Animal) then overwrite sound(self) return woof woof.
            # 4.create child class Cat(Animal) then overwrite sound(self) return meow meow.
            # 5.create child class Bird(Animal) then pass
            # 6.call the class and methods.

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

class Bird(Animal):
    pass

print(Dog().sound())
print(Cat().sound())
print(Bird())

# dry run:
# woof woof
# meow meow
# error 