# Q39
# EN: A word is given. Count vowels and consonants separately (two counters).
# Given: word = "python"   →  vowels 1, consonants 5

# restate: Ek word diya hai. Vowels aur consonants alag-alag ginno.

# example:word = "baadshah" then the output is vowel = 3 and con = 5.

# pseudocode:
            # 1.starts with given input.
            # 2.create two variable count_vowel=0 and count_consonants=0.
            # 3.use for loop for word.
            # 4.if ch is in "aeiou" then update count_vowel+=1.
            # 5.else count_consonants+=1
            # 6.print output with f-string.

# translate:
word = "python"
count_vowel = 0
count_consonants = 0
for ch in word:
    if ch in "aeiou":
        count_vowel += 1
    else:
        count_consonants += 1

print(f'''the number of vowels is : {count_vowel}, 
the number of consonants is : {count_consonants}''')

# dry run:
# step | ch | vowel | con |
#   1  |  p |   0   |  1  |
#   2  |  y |   0   |  2  |
#   3  |  t |   0   |  3  |
#   4  |  h |   0   |  4  |
#   5  |  o |   1   |  4  |
#   6  |  n |   1   |  5  |

# final output:
# vowel = 1 
# con = 5

