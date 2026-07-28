# Q25
# EN: A list and a target value are given. Print True if the target is in the list, else False (flag, no in). 
# Given: nums = [3, 8, 1, 7, 5], target = 7

# restate:Ek list aur ek target diya hai. Target list mein hai toh True, warna False.

# example:nums = [3, 8, 1, 7, 5] the target = 0. for loop se jakar if me check hoga agar present hoga to true hoga nahi to false. 
#               the output = false.

# pseudocode:
#           1.initilize with nums list.
#           2.then the target = 7
#           3.create flag for finding 7 using: is_found = False
#           4.use for loop for nums.
#           5.set the condition using:i == target then is_found truns True.
#           6.print the output with the help of f-string.

# translate:
nums = [3, 8, 1, 7, 5]
target = 7

is_found = False
for i in nums:
    if i == target:
        is_found = True

print(f"Is {target} present : {is_found}")

# dry run:
# step | is_found | i |
#   1  |   False  | - |
#   2  |   False  | 3 |
#   3  |   False  | 3 |
#   4  |   False  | 8 |
#   5  |   False  | 8 |
#   6  |   False  | 1 |
#   7  |   False  | 1 |
#   8  |   False  | 7 |
#   9  |   True   | 7 |

# final output:
True