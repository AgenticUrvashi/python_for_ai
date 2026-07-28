# Q20
# EN: A list is given. Count how many numbers are greater than 10.
# Given: nums = [5, 12, 8, 20, 10, 15]

# restate:Ek list di hai. 10 se bade kitne numbers hain ginno.

# example: nums = [8,5,23,18,6,0] for loop aur if ki condition satisfy karke fir count print hoga.then the output is 2
# pseudocode:1.initilize with nums list.
#            2.create new varible count = 0
#            3.fix for loop for nums.
#            4.fix the if condition for greater than 10.
#            5.upadate the value of count.
#            6.print count.

# translate:
nums = [5, 12, 8, 20, 10, 15]
count = 0
for i in nums:
    if i > 10:
        count = count + 1

print(count)

# dry run:
# step | count | i |
#   1  |   0   | - |
#   2  |   0   | 5 |
#   3  |   0   | 5 |
#   4  |   0   | 12|
#   5  |   1   | 12|
#   6  |   1   | 8 |
#   7  |   1   | 8 |
#   8  |   1   | 20|
#   9  |   2   | 20|
#  10  |   2   | 10|
#  11  |   2   | 10|
#  12  |   2   | 15|
#  13  |   3   | 15|

# final output:
3