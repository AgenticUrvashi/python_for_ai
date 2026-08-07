'Ek Car class banao with brand, speed, aur ek method drive() jo "BRAND is driving at SPEED" print kare.'

# restate: ek class banani hai jo brand aur speed lekar "brand is driving at speed" return kare.

# example: brand = toyota , speed = 70.

# pseudocode:
            # 1.create class Car.
            # 2.create special method and create objects and store data from user.
            # 3.create another method which include print(f"{self.brand} is driving at {self.speed}km/h.)
            # 4.create object car = Car("toyota",70)
            # 5.call the class with method.

# translate:
class Car:
    def __init__(self, brand:str, speed:int) -> None:
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed}km/h.")

car = Car("toyota",70)

car.drive()

# dry run:
# toyota is driving at 70km/h.