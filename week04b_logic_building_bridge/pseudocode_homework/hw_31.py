# Q31
# EN: A list is given. Find the smallest number without using min().
# Given: nums = [8, 3, 9, 1, 5]

# restate:Ek list di hai. min() ke bina sabse chhota number dhoondho.

# example:nums = [3,5,2,9,6] 3 ko smallest consider karke hum for loop aur if condition se ek ek check karenge.
#                jo chhota hoga vo smallest ki jagh lega.

# pseudocode:
            # 1.initilize with given nums.
            # 2.create new variable samllest = nums[0].
            # 3.use for loop for nums.
            # 4.fix the condition using:if samllest>i.
            # 5.upadate the variable smallest=i.
            # 6.print(samllest).

# translate:
nums = [8,3,9,1,5]
samllest = nums[0]
for i in nums:
    if samllest>i:
        samllest = i

print(samllest)

# dry run:
# step | samllest | i |
#   1  |    8     | 8 |
#   2  |    3     | 3 |
#   3  |    3     | 9 |
#   4  |    1     | 1 |
#   5  |    1     | 5 |

# final output:
1
