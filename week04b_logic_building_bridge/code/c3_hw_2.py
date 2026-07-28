# restate:Ek sentence mein kitne words hain ginno (hint: .split()).

# example:if sentence is "i have confidance" then the count is 3.

# pseudocode:
            # 1.create sentence variable and write:"I am learning python" 
            # 2.create new variable as:sentence.split().
            # 3.create another variable count = 0
            # 4.use for loop for new.
            # 5. update count by 1.
            # 6.print count.

# translate:
sentence = "I am learning python"
new = sentence.split()
count = 0
for i in new:
    count = count + 1

print(count)

# dry run:
# step | count |   i    |
#   1  |   0   |   I    |
#   2  |   1   |   I    |
#   3  |   1   |  am    |
#   4  |   2   |  am    |
#   5  |   2   |learning|
#   6  |   3   |learning|
#   7  |   3   | python |
#   8  |   4   | python |

# final output:
4
