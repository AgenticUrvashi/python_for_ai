# Q11
# EN: A number n is given. Print the sum of all numbers from 1 to n.
# Given: n = 5   →  1+2+3+4+5 = 15

# restate:Ek number n diya hai. 1 se n tak sabka sum print karo.
# example:we have n = 3 fir vo for loop me one by one jakar total me add hoga then the output is 6
# pseudocode:1.starts with given input.
#            2.asign the value to new variable total = 0
#            3.use the for loop having range(1,n+1).
#            4.update the total
#            5. print total

# translate:
n = 5
total = 0

for i in range(1,n+1):
    total = total + i

print(total)

# dry run:
# step | total | i |
#   1  |   0   | - |
#   2  |   0   | 1 |
#   3  |   1   | 1 |
#   4  |   1   | 2 |
#   5  |   3   | 2 |
#   6  |   3   | 3 |
#   7  |   6   | 3 |
#   8  |   6   | 4 |
#   9  |   10  | 4 |
#  10  |   10  | 5 |
#  11  |   15  | 5 |

# final output:
15