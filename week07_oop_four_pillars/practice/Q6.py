'''Car class banao:

brand
private __speed
set_speed(speed) → speed 0-200 ke beech ho tabhi update kare
get_speed() → speed return kare

Object bana ke speed 120 set karo. 🚗'''

# restate:class banao car jisme speed private ho aur use hum upadate kare 120 set kare.

# example:old = 80 then new = 120

# pseudocode:
            # 1.create class Car.
            # 2.create special method __init__(self,speed),self.__speed = speed
            # 3.create method set_speed(self,speed).if speed in range(0,201) then self.__speed = speed else print invalid input.
            # 4.create another method get_speed(self) return self.__speed
            # 5.create obj = Car(80) then obj.set_speed(120) then print(obj.get_speed())

# translate:
class Car:
    def __init__(self,speed):
        self.__speed = speed

    def set_speed(self,speed):
        if speed in range(0,201):
            self.__speed = speed

        else:
            print("invalid input")

    def get_speed(self):
        return self.__speed


obj = Car(80)

obj.set_speed(120)
print(obj.get_speed())

# dry run:
120