# Q13
# EN: A list of numbers is given. Count how many are even.
# Given: nums = [1, 4, 6, 7, 10, 3]

# restate:Numbers ki list di hai. Kitne even hain ginno.
# example:nums = [2,4,5,6,1] one by one for loop me se if me check hoga aur condition sastisfy hone ke baad print hoga.the output = 3
# pseudocode:1.initilize with given input.
#            2.count = 0
#            3.add the for loop for nums
#            4.fix the condition for even value as: i%2 == 0.
#            5.after the condition is satisfied update the count by 1.
#            6.print the count.

# translate:
nums = [1,4,6,7,10,3]
count = 0
for i in nums:
    if i % 2 == 0:
        count = count + 1

print(count)

# dry run:
# step | count | i |
#   1  |   0   | - |
# for2 |   0   | 1 |
# if3  |   0   | 1 |
# for4 |   0   | 4 |
# if5  |   0   | 4 |
#   6  |   1   | 4 |
# for7 |   1   | 6 |
#  if8 |   1   | 6 |
#   9  |   2   | 6 |
# for10|   2   | 7 |
#  if11|   2   | 7 |
# for13|   2   |10 |
# if14 |   2   |10 |
#  15  |   3   |10 |
# for16|   3   | 3 |
# if17 |   3   | 3 |

# final output:
3