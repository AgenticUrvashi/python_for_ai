'Employee parent with work(); Developer aur Designer children jo alag-alag work print karein.'

# restate:ek parent class banao aur do child class har child ka alag work dikhao.

# example:developer ka kam hoga code likhana aur designer ka hoga UI disign karna.

# pseudocode:
            # 1.create parent class Employee then create method work(self) then pass.
            # 2.create child class Developer(Employee) then overwrite work method print code writing.
            # 3.create child class Designer(Employee) then overwrite work method print disigning user interface (UI).
            # 4.child class().method()

class Employee:
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("code writing")

class Designer(Employee):
    def work(self):
        print("disigning user interface (UI)")

Developer().work()

Designer().work()

Employee().work()

# dry run:
# code writing
# disigning user interface (UI)