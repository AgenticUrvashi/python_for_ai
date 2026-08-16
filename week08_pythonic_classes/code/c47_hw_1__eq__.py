'que : Money class (amount) mein __eq__ add karo taaki same amount equal ho.'

# restate:money naam ki class bana ke __eq__ se amount equal show karo.

# example: amount = 5000000

# pseudocode:
            # 1.create class Money.
            # 2.create special method __init__(self,amount) then self.amount = amount
            # 3.create special method __eq__(self,other) return self.amount == other.amount
            # 4.print class(amount) == class(amount)

# translate:
class Money:
    def __init__(self,amount):
        self.amount = amount

    def __eq__(self,other):
        return self.amount == other.amount

print(Money(5000000) == Money(5000000))   

# dry run:
True