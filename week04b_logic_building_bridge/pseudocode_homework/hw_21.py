# Q21
# EN: A list is given. Print the sum of only the odd numbers.
# Given: nums = [1, 2, 3, 4, 5, 6]

# restate:Ek list di hai. Sirf odd numbers ka sum print karo.
# example:nums=[2,4,6,7,3] for loop aur if ki condition ke baad total me add hoga.then the output = 10
# pseudocode:1.initlize with given input list.
#            2.create new varibale total = 0.
#            3.fix for loop for nums.
#            4.fix the condition for odd: i % 2 != 0.
#            5.update the total by adding i.
#            6.print total.

# translate:
nums = [1,2,3,4,5,6]
total = 0
for i in nums:
    if i % 2 != 0:
        total = total + i

print(total)

# dry run:
# step | total | i |
#   1  |   0   | - |
#   2  |   0   | 1 |
#   3  |   1   | 1 |
#   4  |   1   | 2 |
#   5  |   1   | 3 |
#   6  |   4   | 3 |
#   7  |   4   | 4 |
#   8  |   4   | 5 |
#   9  |   9   | 5 |
#  10  |   9   | 6 |

# final output:
9