'''Laptop class banao jo Battery object rakhe.

Battery:

capacity attribute ho.

Laptop:

Composition se Battery ka object rakho.
@property se battery capacity access karo.
Setter mein check karo ki capacity 1000 se kam na ho.
__str__() se output do:'''

class Battery:
    def __init__(self,capacity):
        self.capacity = capacity

class Laptop:
    def __init__(self) -> None:
        self.battery  = Battery(23445)

    @property
    def capacity_batt(self):
        return self.battery.capacity

    @capacity_batt.setter
    def capacity_batt(self,value):
        if value >= 1000:
            self.battery.capacity = value
        else:
            print("invalid battery capacity")

    def __str__(self) -> str:
        return f"The capacity of battery is {self.capacity_batt}"

laptop = Laptop()

print(laptop)

laptop.capacity_batt = 4000

print(laptop)
