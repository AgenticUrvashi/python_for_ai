# restate:Ek list of names mein "Asha" hai kya, aur agar hai toh us par kaunse index par hai (hint: enumerate).

# example:list = ["radha","Asha","jafar","ananya"] then enumerate se index dete hua hum if condition se satisfy karke fir print hoga.

# pesudocode:
            # 1.create words variable having names of boys and girls.
            # 2.use enumerate for indexing.
            # 3.fix the condition for searching Asha as:word == "Asha".
            # 4.print the output with the help of f-string.

# translate:
words = ["radha","Asha","jafar","ananya"]
# is_present = False
for index,word in words:
    if word == "Asha":

        print(f"Found Asha at index {index}")

# dry run:
# step | output | word |
#   1  |   -    |radha |
#   2  |  found | Asha |

# final output:
# found Asha at index 1.

