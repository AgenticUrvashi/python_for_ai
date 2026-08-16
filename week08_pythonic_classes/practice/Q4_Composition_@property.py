'''Computer class banao jo CPU aur RAM objects rakhe.
Requirements:
CPU mein cores ho.
RAM mein size ho.
Computer ke andar CPU aur RAM ke objects banao (Composition).
Computer mein @property ka use karke ram_size access karo.
ram_size ko change karne par value 4 GB ya usse zyada honi chahiye.
Valid value ho to update karo, warna "Invalid RAM size" print karo.'''

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