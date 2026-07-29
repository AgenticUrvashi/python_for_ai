# restate: multiply_all(*nums) jo saare numbers ka product return kare.

# example:multiply_all(3,5,1) then the output is 15.

# pseudocode:
            # 1.create function multiply_all(*nums).
            # 2.create new variable = 1.
            # 3.use for loop for nums.
            # 4.update new variable by multiplying i.
            # 5.return guna.
            # 6.print function.

# translate:
def multiply_all(*nums):
    guna = 1
    for i in nums:
        guna = guna*i

    return guna

print(multiply_all(2,4,5,3))

# final output:
120