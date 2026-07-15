# Task 5 — Sum & Average of N Numbers
# User se pehle poochho kitne numbers dega (count). Phir loop mein ek-ek karke numbers lo, unka sum aur average print karo.

# Concepts: for loop, running total, int(input()), :.2f
# Hint: loop se pehle total = 0 banao, andar total = total + num.

# ans:
total = 0
print("==============================Sum & Average of N Numbers===============================")

n = int(input("enter your number of count: "))

print("----------------------------------------------------------------------------------------")

for i in range(n):
    num = int(input("enter some numbers(as you want): "))

    print("-------------------------------------------------------------------------------------")

    total += num

average = total/n

print(f"Sum:{total}")
print("--------------------------------------------------------------------------------------")
print(f"Average:{average}")

print("=========================================================================================")