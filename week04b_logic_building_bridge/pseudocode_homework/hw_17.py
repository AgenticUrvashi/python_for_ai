# Q17
# EN: A list of marks is given. Print the average.
# Given: marks = [40, 55, 70, 90]

# restate:input = Marks ki list di hai. Average print karo.
# example:list = [20,30,50] for loop se i total me add hogi then average me total/len(marks) se average print hoga.the output = 33.33
# pesudocode:1.starts with given list.
#            2.create variable total = 0.
#            3.fix for loop for marks.
#            4.update total by adding i.
#            5.create new varible average, outside the loop. using :average = total/len(marks)
#            6.print the average.

# translate:
marks = [40, 55, 70, 90]
total = 0
for i in marks:
    total = total + i

average = total /len(marks)
print(average)

# dry run:
# step | average | total | i  |
#   1  |    -    |   0   | 40 |
#   2  |    -    |   40  | 40 |
#   3  |    -    |   40  | 55 |
#   4  |    -    |   95  | 55 |
#   5  |    -    |   95  | 70 |
#   6  |    -    |   165 | 70 |
#   7  |    -    |   165 | 90 |
#   8  |    -    |   255 | 90 |
#   9  |  65.75  |   255 | 90 |

# final output:
65.75