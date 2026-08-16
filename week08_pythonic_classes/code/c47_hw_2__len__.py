'que = Cart class mein __len__ add karo jo items ki sankhya de.'

# restate:cart naam ki class banao usme kuch items add karo aur uski length print karo.

# example: item number 1= A and 2 = B then the length is 2

# pseudocode:
            # 1.create class Cart.
            # 2.create special method __init__(self) then self.storeage = []
            # 3.create method add(self,item) then self.storeage.append(item)
            # 4.create another special method __len__(self) return len(self.storeage)
            # 5.obj = class() then obj.add("A") and obj.add("B") then print len(obj)

# translate:
class Cart:
    def __init__(self):
        self.storeage = []

    def add(self,item):
        self.storeage.append(item)

    def __len__(self):
        return len(self.storeage)

p = Cart()
p.add("A")
p.add("B")
print(len(p))   

# dry run:
2