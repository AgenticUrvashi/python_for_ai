'''BankAccount class banao:

owner aur private __balance rakho.
deposit(amount) method banao.
get_balance() method se balance return karo.
__str__() define karo.
Jab object ko print() karo, output aaye:'''

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Owner:{self.owner} , Balance = {self.__balance}"

obj = BankAccount("Asha", 5000)

print(obj.get_balance())

print(obj)