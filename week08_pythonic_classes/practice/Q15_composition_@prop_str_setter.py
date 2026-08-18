'''Restate: Ek Car class banao jo:
Engine object ko composition se rakhe.
Engine mein horsepower attribute ho.
Car mein @property se horsepower access karo.
Setter mein horsepower 100 se kam nahi hona chahiye.
__str__() use karke car ki horsepower print karo.'''

# example: horsepower = 300 , vlaue = 400

# pseudocode:
            # 1.create class Engine
            # 2.create method __init__(self,horsepower) then self.horsepower
            # 3.create class Car
            # 4.create method __init__(self) then self.power = Engine(300)
            # 5.write @property
            # 6.create method horsepower(self) return self.power.horsepower
            # 7.write @horsepower.setter
            # 8.overwrite method horsepower(self,value)
            # 9.if valuse >= 100: self.power.horsepower = value
            # 10.else: print("invalid")
            # 11.create method __str__(self) return f"the horsepower of car is {self.horsepower}"
            # 12.obj = Car() then print(obj)
            # 13.obj.horsepower = 400 then print(obj)

class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self):
        self.power = Engine(300)

    @property
    def horsepower(self):
        return self.power.horsepower

    @horsepower.setter
    def horsepower(self,value):
        if value >= 100:
            self.power.horsepower = value

        else:
            print("invalid")

    def __str__(self):
        return f"The horsepower of car is {self.horsepower}"

h = Car()

print(h)

h.horsepower = 400

print(h)

# dry run:
# The horsepower of car is 300
# The horsepower of car is 400