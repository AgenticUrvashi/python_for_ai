'''Ab isi BankAccount mein withdraw(amount) method add karo.

Condition:

amount balance se kam/equal hai → withdraw
amount balance se zyada hai → "Insufficient balance" print karo.'''

# restate:hame BankAccount naam ka class banana hai jisme hame withdraw bhi add karna aur usme condition set karo.

# example:balance = 1000 then amount = 1200 then the output is Insufficient balance.

# pseudocode:
            # 1.create class BankAccount.
            # 2.create special method __init__(self,account_holder,balance)
            # 3.create another method deposite(self,amount).if ampunt<0 then print invalid, if amount>0 then self.__balance+=amount
            # 4.create another method withdraw(self,amount).if amount <= self.__balance then self.__balance -= amount.
            #   else print Insufficient balance.
            # 5.create another method get_balance(self) then print(self.__balance)
            # 6.create obj = class("shanaya",1000)
            # 7.obj.withdraw(1200)

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        if amount < 0:
            print("invalid")
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        print(self.__balance)

obj = BankAccount("shanaya",1000)

obj1 = BankAccount("ashu",1500)

obj.withdraw(1200)

obj1.withdraw(500)
obj1.get_balance()

# dry run:
# Insufficient balance
# 1000