# restate:"hello" ko reverse karke naya string banao (accumulator = "").

# example:"anushka" for loop se one by one accumulator me reverse me print hoga the output is "olleh". 

# pseudocode:
            # 1.create word variable = "hello"
            # 2.create new variable accumulator = ""
            # 3.use for loop for word.
            # 4.update accumulator by adding i.
            # 5.print accumulator.

# translate:
word = "hello"
accumulator = ""
for i in word:
    accumulator = i + accumulator

print(accumulator)

# dry run :
# step | accumulator | i |
#   1  |      ""     | h |
#   2  |      "h"    | h |
#   3  |     "eh"    | e |
#   4  |     "leh"   | l |
#   5  |    "lleh"   | l |
#   6  |    "olleh"  | o |

# final output:
"olleh"