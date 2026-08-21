'Ek BankAccount class (Week 7) mein withdraw ko custom InsufficientFundsError raise karwao.'

# restate: class banao BankAccount naam ki aur usme withdraw naam ka function bana ke InsufficientFundsError dikhao.

# example: balance = 6000 and amount = 9000

# pseudocode:
            # 1.create custom error InsufficientFundsError(Exception) then "raise when balance is greater than amount." then pass
            # 2.create class BankAccount
            # 3.create special method __init__(self,balance) then self.balance = balance
            # 4.create method withdraw(self,amount)
            # 5.if self.balance < amount then raise InsufficientFundsError("your balance is insufficient for withdraw amount",amount)
            # 6.else: self.balance - amount then print("Withdraw successful")
            # 7.obj = BankAccount(6000) then obj.withdraw(9000)

class InsufficientFundsError(Exception):
    "raise when balance is greater than amount."
    pass

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if self.balance < amount:
            raise InsufficientFundsError("your balance is insufficient for withdraw amount",amount)

        else:
            self.balance - amount
            print("withdraw successful...")

obj = BankAccount(6000)

obj.withdraw(9000)

# dry run:
# give error