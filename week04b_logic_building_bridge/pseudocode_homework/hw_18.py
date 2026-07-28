# Q18
# EN: A word is given. Build and print its reverse (accumulator = ""). 
# Given: word = "hello"   →  "olleh"

# restate:Ek word diya hai. Uska reverse banao aur print karo.
# example:word = cat for loop se ek ek karke reverse me satya me add honge then the output = tac.
# pesudocode:1.initilize with given word.
#            2.create new varible include empty string.
#            3.fix the for loop for word.
#            4.update new variable by adding i in starting.
#            5.print the new variable.

# translate:
word = "hello"
satya = ""
for i in word:
    satya = i + satya

print(satya)

# dry run:
# step | satya | i |
#   1  |  ""   | - |
#   2  |  ""   | h |
#   3  |   h   | h |
#   4  |   h   | e |
#   5  |  eh   | e |
#   6  |  eh   | l |
#   7  |  leh  | l |
#   8  |  leh  | l |
#   9  |  lleh | l |
#  10  |  lleh | o |
#  11  | olleh | o |

# final output:
"olleh"