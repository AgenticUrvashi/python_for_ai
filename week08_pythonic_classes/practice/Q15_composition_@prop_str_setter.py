'''Question 1 📝

Ek Car class banao jo:

Engine object ko composition se rakhe.
Engine mein horsepower attribute ho.
Car mein @property se horsepower access karo.
Setter mein horsepower 100 se kam nahi hona chahiye.
__str__() use karke car ki horsepower print karo.'''



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

    