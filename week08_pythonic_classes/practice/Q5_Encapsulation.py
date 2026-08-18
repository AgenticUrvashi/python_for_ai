'''restate: BankAccount class banao:

owner aur private __balance rakho.
Constructor se owner aur balance set karo.
deposit(amount) method banao jo balance mein amount add kare.
get_balance() method se balance return karo.
Private variable __balance ko directly bahar se access nahi karna hai.'''

# example: balance = 5000 then amount = 2000

# pseudocode:
            # 1.create class BankAccount
            # 2.create method __init__(self,owner,balance) then self.owner = owner and self.__balance = balance
            # 3.create method deposit(self,amount) then self.__balance += amount
            # 4.create method get_balance(self) return self.__balance
            # 5.obj = BankAccount("Asha",5000) then print(obj.get_balance())
            # 6.obj.deposit(2000) then print(obj.get_balance())

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance 

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Asha", 5000)

print(account.get_balance())

account.deposit(2000)

print(account.get_balance())

# dry run:
5000
7000