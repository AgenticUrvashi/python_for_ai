#restate: Ek list ke saare numbers ka product (guna) nikalo.

# example:list = [1,2,3] then 1*2=2, 2*3=6

# pseudocode:1.initilize with list.
           # 2.creating new varibale = 1.
           # 3.use for loop for nums.
           # 4.update multi variable by multi*i
           # 5.print multi.  

# translate:
nums= [1,5,7]
multi = 1
for i in nums:
    multi = multi * i

print(multi)

# dry run:
# step | multi | i |
#   1  |   1   | 1 |
#   2  |   1   | 1 |
#   3  |   1   | 5 |
#   4  |   5   | 5 |
#   5  |   5   | 7 |
#   6  |   35  | 7 |

# final output:
35

