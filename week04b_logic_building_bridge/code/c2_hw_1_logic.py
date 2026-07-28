print("=====================================================")

print("CLASS 2")

print("=====================================================")

# que1: Ek number lo aur batao woh positive, negative ya zero hai.
# restate: input=enter any number.  output=agar number positive hai to positive print ho negative ho to negative and zero ho to zero.
# example: if we enter number 10 then returns positive.
# pseudocode: 1.enter any number.
#             2.if number is greater than 0 then print positive.
#             3.else number is smallar than 0 then print negative.
#             4.else number is equals to zero.

# trnaslate:

nums = 10
if nums>0:
    print("positive")
elif nums<0:
    print("neagtive")
else:
    print("zero")

# dry run:
# setps |  num  | output
#   1   |   10   |
# if 2  |   10   |positive

# final output: zero

print("=======================================================")

#que2: Ek list of marks lo aur unka average nikalo.
# restate: input=take list of marks. output=average.
# example: input=take list of 4 subject. output=give average.
# pseudocode: 1.take 4 subject marks.
#             2.in starting take a variable asign the value of total marks.take inital value as 0(zero).
#             3.take for loop and add the marks one by one in total.
#             4.print the average with the help of f-string,total and len(marks).

# translate:
marks = [45,67,34,98]
total = 0
for mark in marks:
    total = total + mark
print(f"the average is {total/len(marks)}")

# dry run:
# step  | average | total | len(marks) | mark
#   1   |    -    |   0   |      4     |  - 
#  for2 |    -    |   0   |      4     |  45
#   3   |    -    |  45   |      4     |  45
#  for2 |    -    |  45   |      4     |  67
#   3   |    -    | 112   |      4     |  67
#  for2 |    -    | 112   |      4     |  34
#   3   |    -    | 146   |      4     |  34
#  for2 |    -    | 146   |      4     |  98
#   3   |    -    | 244   |      4     |  98
#   4   |    61   | 244   |      4     |  98

# final output: 61

print("======================================================")

#que3: 1 se 20 tak ke numbers mein se sirf 3 ke multiples print karo.
# restate: input=check 1 to 20 number.  output=only 3 multiples
# example: when we check this problem then output is 3,6,9,12,15,18
# pseudocode:1.take for loop and fix the range 1 to 21 because 21 is not included.
#            2.set the condition as i % 3 == 0 then print.

# translate:
for i in range(1,21):
    if i % 3 == 0:
        print(i)

# dry run:
# steps | i  
# for1  | 1
# if2   | 1
# for1  | 2
# if2   | 2
# for1  | 3
# if2   | 3
# print | 3
# for1  | 4
#  if2  | 4
# for1  | 5
#  if2  | 5
#  for1 | 6
#  if2  | 6
# print | 3,6
# for1  | 7
#  if2  | 7
# for1  | 8
#  if2  | 8
#  for1 | 9
#  if2  | 9
# print | 3,6,9
# for1  | 10
#  if2  | 10
# for1  | 11
#  if2  | 11
#  for1 | 12
#  if2  | 12
# print | 3,6,9,12
# for1  | 13
#  if2  | 13
# for1  | 14
#  if2  | 14
#  for1 | 15
#  if2  | 15
# print | 3,6,9,12,15
# for1  | 16
#  if2  | 16
# for1  | 17
#  if2  | 17
#  for1 | 18
#  if2  | 18
# print | 3,6,9,12,15,18

# final output:
3,6,9,12,15,18

print("========================= END ======================")