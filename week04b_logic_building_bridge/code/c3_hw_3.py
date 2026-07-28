# restate:Ek list mein sabse chhota number dhoondho (bina min()).

# example:[3,5,2,9,6] 3 ko smallest consider karke hum for loop aur if condition se ek ek check karenge.
#                jo chhota hoga vo smallest ki jagh lega.

# pseudocode:
            # 1.initilize with given nums.
            # 2.create new variable samllest = nums[0].
            # 3.use for loop for nums.
            # 4.fix the condition using:if samllest>i.
            # 5.upadate the variable smallest=i.
            # 6.print(samllest).


# translate:
nums = [7,3,8,1,5]
samllest = nums[0]
for i in nums:
    if samllest>i:
        samllest = i

print(samllest)

# dry run:
# step | samllest | i |
#   1  |    7     | 7 |
#   2  |    3     | 3 |
#   3  |    3     | 8 |
#   4  |    1     | 1 |
#   5  |    1     | 5 |

# final output:
1