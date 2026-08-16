'que : Temperature class mein staticmethod c_to_f(c) add karo.'

# restate:temperature naam ki class bano aur staticmethod se c_to_f(c) ye method add karo.

# example: c = 1 

# pseudocode:
            # 1.create class Temperature.
            # 2.write @staticmethod
            # 3.create method c_to_f(c) return (c * 9/5) + 32
            # 4.obj = class().method(1)
            # 5.print(obj)

class Temerature:

    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

q = Temerature().c_to_f(1)
print(q)

# dry run:
33.8