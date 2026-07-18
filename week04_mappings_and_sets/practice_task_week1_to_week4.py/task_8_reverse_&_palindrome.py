# Task 8 — Reverse & Palindrome Check
# User se ek word lo. Use ulta print karo, aur batao woh palindrome hai ya nahi (case ignore karo — "Madam" bhi palindrome hai).

# Concepts: slicing [::-1], .lower(), if/else
# Hint: compare karne se pehle dono ko .lower() kar do.
# ans:

print("===================================Reverse & Palindrome Check================================")

user_input = input("enter your word: ")

new = user_input[::-1]
print(new)

print("----------------------------------------------------")
new.lower
user_input.lower
if new==user_input:
    print("palindrome")
else:
    print("not")

print("=====================================================================================")

