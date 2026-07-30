# Jaan-boojh kar def f(x=[]) waala bug banao, 3 call karke bug dikhao.

# restate:default ke bug ko dikhao.

# example:n= 2,4

# pseudocode:
            # 1.create function UBON(n,li = [])
            # 2.append the n into li.
            # 3.return li.
            # 4.print the function with argument.

# translate:
def UBON(n,li = []):
    li.append(n)
    return li

print(UBON(2))
print(UBON(4))
print(UBON(9))

# dry run:
[2]
[2,4]
[2,4,9]