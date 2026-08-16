'''restate : BankAccount class banao: owner aur _balance attributes rakho.@property se balance ko access karo.
@balance.setter se balance change karo.Balance negative nahi hona chahiye.Agar negative value di jaye, to "Invalid balance" print karo.
Object banao aur balance ko update karke print karo.'''

# example: old = 9000000 , new = 10000000

# pseudocode:
#           1.create class BankAccount.
#           2.create special method __init__(self,owner,balance)then self.owner = owner and self._balance = balance
#           3.write @property
#           4.create method balance(self) return self._balance
#           5.write @balance.setter
#           6.overwrite balance(self,value): if value > 0 then self._balance = value, else: print("Invalid balance")
#           7.obj = BankAccount("Tang",9000000) then print(obj.balance)
#           8.obj.balance = 10000000 then print(obj.balance)

# translate:
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value > 0:
            self._balance = value
        else:
            print("Invalid balance")

obj = BankAccount("Tang",9000000)

print(obj.balance)

obj.balance = 10000000

print(obj.balance)

# dry run:
9000000
10000000