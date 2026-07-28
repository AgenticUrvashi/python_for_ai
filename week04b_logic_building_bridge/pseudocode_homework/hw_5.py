# Q5
# EN: A number is given. Print "Positive", "Negative", or "Zero". 
# Given: n = -4

# restate:Ek number diya hai. "Positive", "Negative", ya "Zero" print karo.
# example: we take n = 0 then check the condition for if the elif then else and the output is zero.
# pseudocode:1.starts with given input. 
#            2.they check the if condition if true then print("positive")
#            3.then check the elif condition if true then print("negative")
#            4.then check the else condition if both the conditions are false then print("zero")

# translate:
n = -4
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# dry run:
# step | output | n
#   1  |   -    | -4
#   2  |   -    | -4
#   3  |negative| -4

# final output:
# negative