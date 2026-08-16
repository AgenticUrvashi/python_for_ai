'que : Person class mein age property + setter jo negative age reject kare.'

# restate: person naam ki class banao jisme ek method banake negative ages reject karo.

# example: age = 25 and value = -20

# pseudocode:
            # 1.create class Person.
            # 2.create special method __init__(self,age) then self._age = age
            # 3.write @property
            # 4.create method negative(self) return self._age
            # 5.write @negative.setter
            # 6.overwrite method negative(self,value) if value < 0 raise ValueError("below zero")
            # 7.else or without else write self._age = value
            # 8.obj = class(25) then obj.negative = -20 print obj.negative

# translate:
class Person:
    def __init__(self,age):
        self._age = age

    @property
    def negative(self):
        return self._age

    @negative.setter
    def negative(self,value):
        if value < 0:
            raise ValueError("below zero")

        self._age = value

t = Person(25)    
t.negative = -20
print(t.negative)      
   
# dry run:
# error dega