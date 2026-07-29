
# EN: A list with duplicates is given. Print how many unique values it has (use set).
# Given: nums = [1, 2, 2, 3, 3, 3, 4]

# restate: Duplicates wali list di hai. Kitni unique values hain print karo (set).

# example:nums = [1, 2, 2, 3, 3, 3, 4,1,4,1,2] then the output is (1,2,3,4)

# pseudocode:
            # 1.initilize with given list
            # 2.create a variable count = 0.
            # 3.create new variable and nums convert into set.
            # 4.use for loop for num.
            # 5.upadate count variable by 1.
            # 6.print

# translate:
nums = [1,2,2,3,3,3,4]
count = 0
num = set(nums)
for i in num:
    count = count + 1

print(count)

# dry run:
# step | count | num |
#   1  |   0   |  -  |
#   2  |   1   |  1  |
#   3  |   2   |  2  |
#   4  |   3   |  3  |
#   5  |   4   |  4  |

# final output:
4