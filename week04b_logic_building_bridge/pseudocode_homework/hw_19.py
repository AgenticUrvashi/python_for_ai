# Q19
# EN: A number n is given. Print its multiplication table from 1 to 10. 
# Given: n = 7   →  7 x 1 = 7 ... 7 x 10 = 70

# restate:Ek number n diya hai. 1 se 10 tak uska table print karo.

# example:n = 2 for loop se one by one numbers n se multiply honge aur print me f-string ke help se table print hoga.
#             the output = 2 * 1 = 2 ... 2 * 10 = 20

# pseudocode:1.start with n = 7.
#            2.fix with for loop with the range(1,11).
#            3.create a varible table = n * 1
#            4.print the table with the help of f-string:f"n * {i} = {table}".

# translate:
n = 7
for i in range(1,11):
    table = n * i 
    print(f"n * {i} = {table}")

# dry run:
# step | i |    table    | 
#   1  | 1 |      7      |
#   2  | 2 |      14     |
#   3  | 3 |      21     |
#   4  | 4 |      28     |
#   5  | 5 |      35     |
#   6  | 6 |      42     |
#   7  | 7 |      49     |
#   8  | 8 |      56     |
#   9  | 9 |      63     |
#  10  | 10|      70     |

# final output:
7,14,21,28,35,42,49,56,63,70
