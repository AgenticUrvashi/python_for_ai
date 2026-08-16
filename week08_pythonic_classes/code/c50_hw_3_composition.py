'Computer class banao jo CPU aur RAM objects rakhe (composition).'

# restate:computer naam ki class banao jo CUP aur RAM ke obj rakhe.

# example:CUP(5) , RAM(8)

# pseudocode:
            # 1.create class CUP then create special method __init__(self,c) then self.c = c
            # 2.create class RAM then create special method __init__(self,r) then self.r = r
            # 3.create class computer and create special method __init__(self) then self.c = CUP(5) and self.r = RAM(8)
            # 4.cr = Computer() then print(cr.c.c , cr.r.r)

class CUP:
    def __init__(self,c):
        self.c = c

class RAM:
    def __init__(self,r):
        self.r = r

class Computer:
    def __init__(self):
        self.c = CUP(5)
        self.r = RAM(8)

cr = Computer()
print(cr.c.c, cr.r.r) 

# dry run:
# 5  8