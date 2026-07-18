# Task 14 — Word Frequency Counter
# Ek paragraph string lo (multi-word). Har word kitni baar aaya, ek dictionary mein count karo (case-insensitive).
#  Phir sabse zyada aane wala word batao.

# Concepts: .lower(), .split(), dict counting, max(..., key=...)
# Hint: max(counts, key=counts.get) sabse badi value waali key deta hai.

# ans:

print("====================================Word Frequency Counter==================================")

paragraph = '''hi i am the python learnar 
i am from indor i learn python
i am learning python for becoming agentic ai engineer
pyhon is very easy to understand'''

counts={}

paragraph= paragraph.lower()
words = paragraph.split()

for word in words:
        counts[word] = counts.get(word, 0) + 1

print("the count of every word is as following!!")

print("-------------------------------------------------------------------------------------------")

for word, count in counts.items():
    print(f"{word} : {count}")
    print("---------------------------")         


print("--------------------------------------------------------------------------------------------")

maxminum_number_word = max(counts, key=counts.get)

print(f"the maximum time repeated word is : {maxminum_number_word}")

print("============================================ end ============================================")

