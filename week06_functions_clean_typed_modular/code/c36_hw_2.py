# que : make_adder(n) closure banao jo n add kare ; add5 ==make_adder(5) text karo.

# restate:function me function bana ke un numbers ko add karke dikhao.

# example:x = 10 , 8   n = 5  ,the output is 15 , 13.

# pseudocode:
            # 1.create function make_adder(n).
            # 2.create another function add(x).
            # 3.return x + n
            # 4.return add.
            # 5.create variable add5 = make_adder(5).
            # 6.print the variable with parameter: print(add5(10))

# translate:
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
print(add5(10))
print(add5(8))

# Dry run 
15
13