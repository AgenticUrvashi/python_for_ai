# Q22
# EN: A number n is given. Build a list of squares from 1 to n and print it. 
# Given: n = 5   →  [1, 4, 9, 16, 25]

# restate:Ek number n diya hai. 1 se n tak squares ki list banao aur print karo.
# example: n = 4 for loop se range tak append kiya.then the output = [1,4,9,16]
# pseudocode:1.starts with given input.
#            2.create new variable having empty list.
#            3.fix the for loop at the range(1,n+1).
#            4.add the squaring condition in new variable:the condition(i**2)or (i*i).
#            5.print result.

# translate:
n = 5
result = []
for i in range(1,n+1):
    result.append(i**2)

print(result)

# dry run:
# step |    result    | i |
#   1  |      []      | - |
#   2  |      []      | 1 |
#   3  |      [1]     | 1 |
#   4  |      [1]     | 2 |
#   5  |    [1,4]     | 2 |
#   6  |    [1,4]     | 3 |
#   7  |   [1,4,9]    | 3 |
#   8  |   [1,4,9]    | 4 |
#   9  |  [1,4,9,16]  | 4 |
#  10  |  [1,4,9,16]  | 5 |
#  11  |[1,4,9,16,25] | 5 |

# final output:
[1,4,9,16,25]
