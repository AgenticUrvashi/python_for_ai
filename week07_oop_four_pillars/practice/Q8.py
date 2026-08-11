'''Ek Mobile class banao jisme:

brand
model
private __price
set_price(price) → price 0 se greater ho tabhi update kare
get_price() → price return kare

Object banao aur price update karke print karo.'''

# restate:ek class banao jisme price private ho aur use update karke print karo.

# example:brand = TATA, model = thar , old_price = 7000000 ,new_price= 7500000

# pseudocode:
            # 1.create class Mobile.
            # 2.create special method __init__(self,brand,model,price)
            # 3.create method set_price(self,price). if price>0 then self.__price =price, else print inavlid input
            # 4.create another method get_price(self) return self.__price.
            # 5.create object = class("TATA","thar",7000000)
            # 6.obj.set_price(7500000)
            # 7.price object.get_price()

class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price

    def set_price(self,price):
        if price > 0:
            self.__price = price
        else:
            print("invalid input")

    def get_price(self):
        return self.__price

obje = Mobile("TATA","thar",7000000)

obje.set_price(7500000)

print(obje.get_price())

# dry run:
7500000