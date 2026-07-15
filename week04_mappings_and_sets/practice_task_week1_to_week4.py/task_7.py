# Task 7 — Word & Character Counter
# User se ek sentence lo. Print karo: kitne words hain, kitne characters (spaces chhod kar), aur sentence UPPERCASE mein.

# Concepts: .split(), .replace(), len(), .upper(), .strip()
# Hint: spaces hatane ke liye .replace(" ", "") phir len().
# ans: 

print("================================ Word & Character Counter===================================")

user_input = input("enter your sentence: ")

print(user_input)

print("------------------------------------------------------------")

word = user_input.split()
print(len(word))

print("-------------------------------------------------------------")
characters = user_input.replace(" ","")
print(len(characters))

print("-------------------------------------------------------------")

print(user_input.upper)

print("============================================ end ============================================")