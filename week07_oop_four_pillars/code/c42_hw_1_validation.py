'BankAccount mein validation add karo taaki balance kabhi negative na ho.'

# restate:isa class banao jisme bankaccount me validation added ho.

# example:balance = 200 then amount = 500 for withdraw

# pseudocode:
            # 1.create class BankAccount.
            # 2.create special method __init(self, balance) then self.balance = balance
            # 3.create method deposite(self, amount). if amount<0 then invalid input, if amount>0 then self.balance += amount.
            # 4.create another method withdraw(self, amount). if amount<0 then invalid input, if amount>0 then self.balance -= amount
            # 5.create another method get_balance(self) returns self.balance.
            # 6.create object paisa = Bank Account(200)
            # 7.print object.method(amount)

# translate:
class BankAccount:

    def __init__(self, balance):

        self.balance = balance      

    def deposit(self, amount):
        if amount < 0:
            return "invalid input"

        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            return "invalid input"
        if amount > 0:
            self.balance -= amount

    def get_balance(self):

        return self.balance

paisa = BankAccount(200)

print(paisa.deposit(-234))
print()
print(paisa.withdraw(-500))

# dry run:
# invalid input

# invalid input