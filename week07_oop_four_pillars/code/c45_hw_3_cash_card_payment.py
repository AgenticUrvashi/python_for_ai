'Ek abstract PaymentMethod with abstract pay(amount); Cash aur Card se implement karo.'

# restate:Payment naam ka abstract method banao aur usme pay(amount) naam ki abstractmethod banao card aur cash implement karo.

# example: in card, amount = 1000 and in cash, amount = 200

# pseudocode:
            # 1.import ABC from abc then abstractmethod.
            # 2.create abstract class PaymentMethod(ABC).
            # 3.write @abstractmethod and create method pay(self,amount) then ...
            # 4.create child class Cash(Paymentmethod) then overwrite pay method and print "cash payment of rupees", amount
            # 5.create child class Card(paymentmethod) then overwrite pay method and print "card payment of repees", amount
            # 6.call the class and method with amount

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self,amount):
        ...

class Cash(PaymentMethod):
    def pay(self,amount):
        print("cash payment of rupees", amount)

class Card(PaymentMethod):
    def pay(self,amount):
        print("card payment of repees", amount)

Cash().pay(200)

Card().pay(1000)

# dry run:
# cash payment of rupees 200
# card payment of rupees 1000