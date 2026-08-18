'''Restate : Computer class banao jo CPU aur RAM objects rakhe.
Requirements:
CPU mein cores ho.
RAM mein size ho.
Computer ke andar CPU aur RAM ke objects banao (Composition).
Computer mein @property ka use karke ram_size access karo.
ram_size ko change karne par value 4 GB ya usse zyada honi chahiye.
Valid value ho to update karo, warna "Invalid RAM size" print karo.'''

# example: CPU(9) and RAM(18)

# psudocode:
            # 1.create class CPU 
            # 2.create method __init__(self,cores) then self.cores = cores
            # 3.create class RAM
            # 4.create method __init__(self,size) then self.size = size
            # 5.create class Computer
            # 6.create method __init__(self) then self.cpu = CUP(9) and self.ram = RAM(18)
            # 7.write @property
            # 8.create method ram_size(self) then return self.ram.size
            # 9.write @ram_size.setter
            # 10.create method ram_size(self,new): if new >= 4 self.ram.size = new else: print("invalid ram size")
            # 11.obj = Computer()
            # 12.print(obj.ram_size) then obj.ram_size = 32 then print(computer.ram_size)

class CPU:
    def __init__(self,cores):
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class Computer:
    def __init__(self):
        self.cpu = CPU(9)
        self.ram = RAM(18)
    @property
    def ram_size(self):
        return self.ram.size

    @ram_size.setter
    def ram_size(self,new):
        if new >= 4:
            self.ram.size = new
        else:
            print("Invalid RAM size")

computer = Computer()

print(computer.ram_size)

computer.ram_size = 32
print(computer.ram_size)

# dry run:
# 18
# 32