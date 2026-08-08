'Ek Temperature class banao with _celsius; ek method set_celsius jo -273 se kam value reject kare.'

# restate: ek class Temperature banao jo farhenait se celsius me temp convert kare aur -273 se kam value reject kare.

# example:temp = -110 and -345

# pseudocode:
            # 1.create class Temperature.
            # 2.create special method __init__(self,temp) then self.temp = temp
            # 3.create another set_celsius(self). if self.temp<-273 then print invalid, if self.temp>-273 then print (f - 32) * 5 / 9
            # 4.create two objects temp1 and temp2 then store value.
            # 5.call the methods.

# translate:
class Temperature:
    def __init__(self,_celsius):
        self._celsius = _celsius

    def set_celsius(self):
        if self._celsius < -273:
            print("invalid")

        if self._celsius > -273:
            print((self._celsius - 32) * 5 / 9)

Temp1 = Temperature(-110)

temp2 = Temperature(-345)

Temp1.set_celsius()

temp2.set_celsius()

# dry run:
# -78.8888
# "invalid"