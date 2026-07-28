# Q26
# EN: A number is given. Count how many digits it has (use while and // 10).
# Given: n = 4592   →  4

# restate:Ek number diya hai. Usme kitne digits hain ginno (while + // 10).

# example:n = 563670 to while loop se jakar digit add hoke fir n me se last digit remove ho jayega fir loop run karenga.
#         then the output is 4.

# pseudocode:
            # 1.initilize with given input.
            # 2.create digits variable as digits = 0
            # 3.in while loop fix the condition as: n > 0.
            # 4.update the digits variable.
            # 5.update the n variable as:n // 10.
            # 6.print digits.

# translate:
n = 4592
digits = 0

while n>0:
    digits += 1
    n = n // 10

print(digits)

# dry run:
# step | digits |   n   |
#   1  |    0   | 4592  |
#   2  |    1   |  459  |
#   3  |    2   |   45  |
#   4  |    3   |   5   |
#   5  |    4   |   -   |

# final output:
4