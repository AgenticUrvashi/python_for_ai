# Q15
# EN: A word is given. Count the vowels in it.
# Given: word = "education"

# restate:Ek word diya hai. Usme vowels ginno.
# example: input = "ananya" pehle lower case me convert hokar for loop aur if ki condition satisfy karke count add hoga.then the output = 3
# pseudocode:1.starts with given input.
#            2.upadate word variable for lowercase the word.
#            3.create new varible count=0.
#            4.use for loop for word.
#            5.fix the condition using if/else:if i in "aeiou".
#            6.update the count variable.
#            7. print the count.

# trnaslate:
word = "education"
word = word.lower()
count = 0
for i in word:
    if i in "aieou":
        count = count + 1

print(count)

# dry run:
# step | count | i |
#   1  |   0   | - |
#   2  |   0   | e |
#   3  |   1   | e |
#   4  |   1   | d |
#   5  |   1   | d |
#   6  |   1   | u |
#   7  |   2   | u |
#   8  |   2   | c |
#   9  |   2   | c |
#  10  |   2   | a |
#  11  |   3   | a |
#  12  |   3   | t |
#  13  |   3   | t |
#  14  |   3   | i |
#  15  |   4   | i |
#  16  |   4   | o |
#  17  |   5   | o |
#  18  |   5   | n |
#  19  |   5   | n |

# final output:
5