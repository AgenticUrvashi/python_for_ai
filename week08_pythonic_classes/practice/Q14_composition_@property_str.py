'''Restate: Laptop class banao jo Battery object rakhe.
Battery:
capacity attribute ho.
Laptop:
Composition se Battery ka object rakho.
@property se battery capacity access karo.
Setter mein check karo ki capacity 1000 se kam na ho.
__str__() se output do:'''

# example: capacity = 23445 and value = 4000

# pseudocode:
            # 1.create class Battery
            # 2.create method __init__(self,capacity) then self.capacity = capacity
            # 3.create class Laptop
            # 4.create method __init__(self) then self.battery = Battery(23445)
            # 5.write @property
            # 6.create method capacity_batt(self) return self.battery.capacity
            # 7.write @capacity_batt.setter
            # 8.overwrite method capacity_batt(self,value) 
            # 9.if value >= 1000: self.battery.capacity = value
            # 10.else: print("invalid battery capacity")
            # 11.create method __str__(self) return f"the capacity of battery is {self.capacity_batt}"
            # 12.obj = Laptop() then print(obj)
            # 13.obj.capacity.batt = 4000
            # 14.print(obj)

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

# dry run:
# The capacity of battery is 23445
# The capacity of battery is 4000
