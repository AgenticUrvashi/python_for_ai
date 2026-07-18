# Task 13 — Vowel & Consonant Counter
# User se ek sentence lo. Ek dictionary banao jo har vowel (a,e,i,o,u) kitni baar aaya woh count kare. 
# Phir total consonants (letters jo vowel nahi) alag se print karo.

# Concepts: loop over string, dict, .get() ya in check, .lower()
# Hint: counts[ch] = counts.get(ch, 0) + 1 — yeh missing key ko safely handle karta hai.
# ans: 

print("============================= Vowel & Consonant Counter =============================")

user_input = input("enter your sentence: ")

print("-------------------------------------------------------------------------------------")

new = user_input.lower().replace(" ","")
# ch = new.replace(" ","")
counts={}
length =len(new)

for ch in new:
    if ch in "aeiou":
        counts[ch] = counts.get(ch, 0) + 1


vowel_count = sum(counts.values())
consonants = length - vowel_count

print(f"the vowels is {counts}")

print("-------------------------------------------------------------------------------------")

print(f"the consonants is {consonants}")

print("-------------------------------------------------------------------------------------")

print(f"the vowel count is {vowel_count}")

print("========================================= Thank You ==================================")