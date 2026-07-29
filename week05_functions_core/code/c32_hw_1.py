# restate: power(base, exp=2) jo default square kare, par exp dene par woh power kare.

# example:if base = 3 then output is 9.

# pseudocode:
            # 1.create a function having two parameter(base,exp=2)
            # 2.create variable square = base * exp.
            # 3.return square.
            # 4.print the function and give one parameter.

# translate:
def power(base,exp = 2):
    square = base**exp
    return square

print(power(4))
print(power(2,4))

# dry run:
# step | base | exp | power |
#   1  |   -  |  2  |   -   |
#   2  |   4  |  2  |  16   |
#   3  |   2  |  4  |  16   |

# final output:
16
16