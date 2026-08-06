'''EN: Write power(base, exp=2) that returns base ** exp. By default it squares; but power(2, 3) should give 8.
हिंदी: power(base, exp=2) बनाओ जो base ** exp return करे। Default में यह square करे; पर power(2, 3) का जवाब 8 आए।
Concepts: default value, ** operator
Hint: return base ** exp. power(5) → 25.'''

# restate:ek function banao jo base ka by default square kare nhi to number user dega.

# example: power(2,3) >>> 8   power(4) >>>> 16

# pseudocode:
            # 1.create function power(base, exp=2)
            # 2.return base ** exp
            # 3.print function with one or two parameter.

# translate:
def power(base, exp=2):
    return base ** exp

print(power(4))
print(power(2,3))

# dry run:
16
8