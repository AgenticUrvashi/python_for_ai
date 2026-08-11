'''Ek BankAccount class banao jisme:

account_holder
private variable __balance
deposit(amount) method
get_balance() method

Object banao aur ₹500 deposit karke balance print karo.'''

# restate:class banao jisme deposite,get_balance naam ke do methods ho deposite se 500 add kare.

# example:balance = 1000 then amount = 500

# pseudocode:
            # 1.create class BankAccount
            # 2.create special methods __init__(self.account_holder,balance).self.account_holder=account_holder,self.__balance=balance
            # 3.create method deposit(self,amount). if amount<0 then print invalid, if amount>0 then self.__balance+=amount print 
            #   self.__balance.
            # 4.create another method get_balance(self). print self__balance.
            # 5.create object = class("ashu",1000)
            # 6.obj.get_balance() and obj.deposite(500)

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self,amount):
        if amount < 0:
            print("invalid")

        if amount > 0:
            self.__balance += amount
            print(self.__balance)

    def get_balance(self):
        print(self.__balance)

obj = BankAccount("ashu",1000)

obj.get_balance()

obj.deposit(500)
            
# dry run:
1000
1500