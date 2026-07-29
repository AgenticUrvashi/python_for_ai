# Q38
# EN: A dict of item → price is given. Print the total cost.
# Given: prices = {"pen": 10, "book": 50, "bag": 200}

# estate:item → price ki dict di hai. Total cost print karo.

# example:{"laptop":200000,"mouse":1000} then the total is 201000.

# psudocode:
            # 1.starts with given input dict.
            # 2.create total = 0.
            # 3.use for loop: for value in prices.values()
            # 4.update total += value
            # 5.print(total)

# translate:
prices = {
    "pen": 10,
    "book": 50, 
    "bag": 200
    }
total = 0
for value in prices.values():
    total = total + value

print(total)

# dry run:
# step | total | value |
#   1  |   0   |   -   |
#   2  |   10  |  10   |
#   3  |   60  |  50   |
#   4  |  260  |  200  |

# final output:
260