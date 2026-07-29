# Q35
# EN: A dict of names → scores is given. Print the name with the highest score.
# Given: scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}

# restate: names → scores ki dict di hai. Sabse zyada score wala naam print karo.

# example:scores = {"Asha": 40, "Ravi": 85, "Zoya": 90} then for loop se if condition me satisfy hone ke baad vo highest banega.
                    # then the output is 90.

# pseudocode:
            # 1.create variable scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}
            # 2.for values in use scores.values()
            # 3.create new variable highest = 0
            # 4.use for loop for scores.values()
            # 5.fix the condition as value>highest if yes then highest = value.
            # 6.print(highest)

# translate:
scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}
scores.values()
highest = 0
for value in scores.values():
    if value > highest:
        highest = value

print(f"the highest marks is: {highest}")

# dry run:
# step | highest | value |
#   1  |    0    |  40   |
#   2  |   40    |  40   |
#   3  |   40    |  85   |
#   4  |   85    |  85   |
#   5  |   85    |  70   |
#   6  |   85    |  70   |

# final output:
85