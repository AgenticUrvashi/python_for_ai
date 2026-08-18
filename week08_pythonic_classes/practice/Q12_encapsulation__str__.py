'''Restate: BankAccount class banao:
owner aur private __balance rakho.
deposit(amount) method banao.
get_balance() method se balance return karo.
__str__() define karo.
Jab object ko print() karo, output aaye:'''

# example: owner = Asha and balance = 5000

# pseudocode:
            # 1.create class BankAccount
            # 2.create method __init__(self,owner,balance) then self.owner = owner and self.__balance = balance
            # 3.create method deposit(self,amount) then self.__balance += amount
            # 4.create method get_balance(self) return self.__balance
            # 5.create method __str__(self) return f"Owner:{self.owner} , Balance = {self.__balance}"
            # 6.obj = BankAccount("Asha",5000)
            # 7.print(obj.get_balance()) then print(obj)

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

# dry run:
# 5000
# Owner:Asha , Balance = 5000