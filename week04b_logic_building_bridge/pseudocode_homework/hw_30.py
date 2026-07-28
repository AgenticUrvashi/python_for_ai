# Q30
# EN: A word is given. Print "Palindrome" or "Not palindrome".
# Given: word = "madam"

# restate: Ek word diya hai. "Palindrome" ya "Not palindrome" print karo.

# example:word="boss" for loop se new me reverse se store hoga fir if/else condition se comapare hoga then output not palindrome aayega.

# pseudocode:
            # 1.initilize with given word.
            # 2.create a variable new = ""
            # 3.create words variable.(words = word.lower())
            # 4.use for loop for word.
            # 5.update new variable as new = i + new.
            # 6.if words = new then print("palindrome").
            # 7.else print("not palindrome").

# translate:
word = "madam"
new = ""
words = word.lower()
for i in word:
    new = i + new

if words == new:
    print("palindrome")
else:
    print("not palindrome")

# dry run
# step |  new  |  output  |
#   1  |  ""   |     -    |
#   2  |  "m"  |     -    |
#   3  |  "ma" |     -    |
#   4  | "mad" |     -    |
#   5  |"mada" |     -    |
#   6  |"madam"|     -    |
#   7  |"madam"|palindrome|

# final output:
# palindrome