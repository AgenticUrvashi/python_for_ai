# Q23
# EN: A number n is given. Print its factorial (n!).
# Given: n = 5   →  120

# restate:Ek number n diya hai. Uska factorial print karo.
# example:n = 3 hai to vo pahle for loop me jakar 1 se 3 tak fact se multiply hoga aur output = 6 aayega.
# pseudocode:1.initilize with given input.
#            2.create new variable having value 1.
#            3.using for loop fix the range(1,n+1)
#            4.upadate the value of new variable by multiplying i
#            5.print fact.

# translate:
n = 5
fact = 1

for i in range(1,n+1):
    fact = fact * i

print(fact)

# dry run:
# step | fact | i |
#   1  |   1  | - |
#   2  |   1  | 1 |
#   3  |   1  | 1 |
#   4  |   1  | 2 |
#   5  |   2  | 2 |
#   6  |   2  | 3 |
#   7  |   6  | 3 |
#   8  |   6  | 4 |
#   9  |  24  | 4 |
#  10  |  24  | 5 |
#  11  | 120  | 5 |

# final output:
120