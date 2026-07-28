# Q27
# EN: A number is given. Print the sum of its digits (use while).
# Given: n = 123   →  6

# restate:Ek number diya hai. Uske digits ka sum print karo (while).

# example:n = 432 fir vo while se total update karke output aayega.the output is 9.

# pseudocode:
            # 1.starts with given n.
            # 2.create new 

# translate:
n = 123
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print(total)

# translate:
# step | total |
#   1  |   0   |
#   2  |   3   |
#   3  |   5   |
#   4  |   6   |

# final output:
6