# Task 4 — Multiplication Table (clean)
# User se ek number n aur ek limit k lo. n ka table 1 se k tak print karo (loop se).

# Concepts: for loop, range(1, k+1), f-string
# Hint: range ka stop exclusive hai — k ko shaamil karne ke liye k + 1 likho.

# ans:

print("============================Multiplication Table (clean)================================")

number = int(input("enter the number for creating multiplication table: "))

print("-----------------------------------------------------------------------------------------")

k = int(input("enter the limit for multiplication table: "))

print("-----------------------------------------------------------------------------------------")

print(f"the table of {number} is as follow: ")

for i in range(1,k+1):
    print(f"{number} * {i} = {number*i}")

print("=========================================================================================")