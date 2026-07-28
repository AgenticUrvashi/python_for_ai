# Q28
# EN: A number is given. Print it reversed (123 → 321, use while). 
# Given: n = 123   →  321

# restate:Ek number diya hai. Ulta print karo (while).

# example:n = 345 while loop se vo digit me last digit leke reverse me reverse * 10 + digit karke hame 543 dega.

# pseudocode:
            # 1.initiate with n = 123
            # 2.create reverse varible having value 0.
            # 3.use while loop and set the condition n > 0.
            # 4.create new varibale digit = n % 10.(3)
            # 5.update reverse variable.(reverse * 10 + digit) iska logic hai(0*10+3=3 then 3*10+2=32 then 32*10+1=321).
            # 6.udpadte the variable n = n // 10(12)
            # 7.print(reverse)

# translate:
n = 123
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)

# translate:
# step |      reverse      | 
#   1  |         0         |
#   2  |   0 * 10 + 3 = 3  |
#   3  |  3 * 10 + 2 = 32  |
#   4  | 32 * 10 + 1 = 321 |

# final output:
321