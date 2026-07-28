# restate:Check karo ek list mein koi negative number hai kya (flag).

# example:list = [2,4,-7,0] then for loop se ek ek karke if ki condition check hoga aur print hoga True.

# pseudocode:
            # 1.take a list having any type of number.
            # 2.create a flag is_negative = False.
            # 3.use for loop for list.
            # 4.fix the condition for negative numbers as:i < 0. 
            # 5.if satisfy then change the flag into True.
            # 6.then print flag.

# trnaslate:
list = [2,4,-7,0]
is_negative = False
for i in list:
    if i < 0 :
        is_negative = True

print(is_negative)

# dry run:
# step | flag | i |
#   1  |False | 2 |
#   2  |False | 4 |
#   3  | True | -7|

# final output:
True