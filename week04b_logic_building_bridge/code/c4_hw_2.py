# restate:Check karo ek word mein koi vowel hai kya.

# example:word = "cloudy" then hum nahi hai consider karte hai aur for loop se ek ek letter ko if condition se satisfy karo.
#                agar ho raha hai to true likho

# pseudocode:
            # 1.create variable word = "cloudy"
            # 2.create flag for vowel = False.
            # 3.use for loop for word.
            # 4.fix condition for vowel as : i in "aeiou"
            # 5.if satisfy the condition then change the flag.
            # 6.print flag.

# translate:
word = "cloudy"
is_vowel = False
for i in word:
    if i in "aeiou":
        is_vowel = True

print(is_vowel)

# dry run:
# step | flag | i |
#   1  |False | c |  
#   2  |False | l | 
#   3  | True | o |

# final output:
True