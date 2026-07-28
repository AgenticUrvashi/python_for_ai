# Q12
# EN: A list of numbers is given. Print the total.
# Given: nums = [10, 20, 30, 40]

# restate:Numbers ki ek list di hai. Total print karo.
# example: nums =[20,10,40] to vo for loop se one by one total me add hoga then the output = 70.
# pseudocode:1.start with given input.
#            2.create new variable total = 0
#            3.fix the for loop for nums
#            4.update value of total by adding i.
#            5.print value of total.

# translate:
nums = [10,20,30,40]
total = 0

for i in nums:
    total = total + i

print(total)

# dry run:
# step | total |  i |
#   1  |   0   |  - |
#   2  |   0   | 10 |
#   3  |  10   | 10 |
#   4  |  10   | 20 |
#   5  |  30   | 20 |
#   6  |  30   | 30 |
#   7  |  60   | 30 |
#   8  |  60   | 40 |
#   9  |  100  | 40 |

# final output:
100