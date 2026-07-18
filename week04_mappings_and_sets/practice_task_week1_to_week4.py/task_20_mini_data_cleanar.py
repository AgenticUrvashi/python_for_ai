# Task 20 — Mini Data Cleaner (comprehensions — capstone)
# Ek messy list of raw user inputs lo:

# raw = ["  Asha ", "RAHUL", "", "  priya  ", "Amit", "rahul  "]

# Ek hi line ke comprehension se: har naam ko strip + lower karo aur khaali strings hatao.
#  Phir us cleaned list se unique naam (set) nikaalo aur alphabetical order mein sorted print karo.

# Concepts: list comprehension + if filter, .strip(), .lower(), set(), sorted()
# Hint: [n.strip().lower() for n in raw if n.strip()] — filter if n.strip() khaali strings ko hata deta hai.

print("======================================= mini data cleaner ======================================")

raw = ["  Asha ", "RAHUL", "", "  priya  ", "Amit", "rahul  "]

new = [n.strip().lower() for n in raw if n.strip()]

print(new)

print("-------------------------------------------------------------------------------------------------")

unique = set(new)

data = sorted(unique)

print(data)

print("============================================ end ==================================================")