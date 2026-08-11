'''restate: Ek abstract class Payment banao.pay() naam ka abstract method ho.UPI class Payment se inherit kare.
UPI mein pay() implement karo.

example: Output print karo: "Payment done by UPI 5000"'''

# pseudocode:
            # 1.from abc import ABC , abstractmethod
            # 2.create Payment(ABC) then @abstractmethod then create method pay(self) and ...
            # 3.create child class UPI(Payment). overwrite pay(self,amount) then print Payment done by UPI, amount
            # 4.call child class().method(amount)

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self):
        ...

class UPI(Payment):
    def pay(self,amount):
        print("Payment done by UPI", amount)

UPI().pay(5000)

# dry run:
# Payment done by UPI 5000