# Q29
# EN: A number n is given. Print a left-aligned star triangle of n rows (nested loop). 
# Given: n = 4
# *
# **
# ***
# ****

# restate:Ek number n diya hai. n rows ka star triangle print karo (nested loop).

# example:n = 3 for loop se ek ek number leke ek ek line me number by number hum * print karte jayenge.

# pseudocode:
            # 1.starts with n = 3.
            # 2.use for loop and give range(1,n+1)
            # 3.print("*"*i)

# translate:
n = 4
for i in range(1,n+1):
    print("*" * i)

# dry run:
# step | i | output |
#   1  | 1 | *      |
#   2  | 2 | *      |
#            * *    |
#   3  | 3 | *      |
#            * *    |
#            * * *  |
#   4  | 4 | *      |
#            * *    |
#            * * *  |
#            * * * *|