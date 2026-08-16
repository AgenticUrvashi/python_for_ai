'''BankAccount class banao:

owner aur private __balance rakho.
Constructor se owner aur balance set karo.
deposit(amount) method banao jo balance mein amount add kare.
get_balance() method se balance return karo.
Private variable __balance ko directly bahar se access nahi karna hai.'''

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance 

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Asha", 5000)

print(account.get_balance())

account.deposit(2000)

print(account.get_balance())