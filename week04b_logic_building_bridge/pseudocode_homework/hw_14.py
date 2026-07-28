# Q14
# EN: A list is given. Find the biggest number without using max().
# Given: nums = [4, 9, 2, 11, 6]

# restate:Ek list di hai. max() ke bina sabse bada number dhoondho.
# example:input = [4,6,8,1,24,6] hum 4 ko biggest consider karke for aur if ke help se check karenge agar bada ho to i = biggest.
#                 the output = 24.
# pseudocode:1.starts with given list.
#            2.we suppose the nums[0] is biggest.
#            3.fix the for loop for nums.
#            4.fix the condition like this: biggest<i then biggest = i
#            5. print biggest.

# translate:
nums = [4, 9, 2, 11, 6]
biggest = nums[0]
for i in nums:
    if biggest<i:
        biggest = i

print(biggest)

# dry run:
# step | biggest | i |
#   1  |    4    | - |
#   2  |    4    | 4 |
#   3  |    4    | 4 |
#   4  |    4    | 9 |
#   5  |    9    | 9 |
#   6  |    9    | 2 |
#   7  |    9    | 2 |
#   8  |    9    | 11|
#   9  |   11    | 11|
#  10  |   11    | 6 |
#  11  |   11    | 6 |

# final output:
11