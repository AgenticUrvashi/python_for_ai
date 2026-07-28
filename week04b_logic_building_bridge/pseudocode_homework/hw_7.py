# Q7
# EN: A word is given. Print how many letters it has.
# Given: word = "python"
 
# restate:Ek word diya hai. Usme kitne letters hain print karo.
# example:we consider word is "fine" then they exicute by for loop one by one.
#         the chearecters are pass and count by count variable the output is 4.
# pseudocode:1.starts with given and count = 0
#            2.use the for loop for word variable.
#            3.update the count by one inside loop
#            4.print the count.

# translate:
word = "python"
count = 0
for i in word:
    count = count + 1
print(count)

# translate:
# step | count | i |
#   1  |   0   | - |
#   2  |   1   | p |
#   3  |   2   | y |
#   4  |   3   | t |
#   5  |   4   | h |
#   6  |   5   | o |
#   7  |   6   | n |

# final output:
6