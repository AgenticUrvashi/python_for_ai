# Q16
# EN: Print all even numbers from 1 to 10, each on its own line.
# (no input — just 1..10)

# restate:
# 1 se 10 tak saare even numbers print karo, har ek nayi line mein.

# example:input = range(1,5) for loop se ek ek karke if me condition check karke baad me i print hoga.the output = 2
#                                      4

# pseudocode:1.fix the for loop with range(1,11)
#            2.fix the condition for even:i%2 == 0.
#            3.print the i.

# translate:
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# dry run:
# step | i | output |
#   1  | 1 |    -   |
#   2  | 2 |    2   |
#   3  | 3 |    2   |
#   4  | 4 |    2   |
#               4   |
#   5  | 5 |    2   |
#               4   |
#   6  | 6 |    2   |
#               4   |
#               6   |
#   7  | 7 |    2   |
#               4   |
#               6   |
#   8  | 8 |    2   |
#               4   |
#               6   |
#               8   |
#   9  | 9 |    2   |
#               4   |
#               6   |
#               8   |
#   10 |10 |    2   |
#               4   |
#               6   |
#               8   |
#              10   |

# final output:
2
4
6
8
10
