# Task 2 — Smart Bill Calculator
# Ek item ka price aur quantity maango. Total nikaalo. Agar total 1000 se zyada hai toh 10% discount lagao,
#  warna koi discount nahi. Final amount 2 decimals ke saath print karo.

# Concepts: arithmetic, if/else, f-string formatting :.2f
# Hint: discount = total * 0.10 sirf tab jab total > 1000.

# ans:

print("===========================Smart Bill Calculator==============================")

price = int(input("enter the cost of item: "))
quantity = int(input("enter the qty of item: "))

total = price*quantity

discount = total*10/100
final = total-discount

print("------------------------------------------------------------------------------------")

if total>1000:
    print(f"Your final amount is : {final:.2f}")
else:
    print(f"Your final amount is : {total:.2f}")

print("------------------------------------------------------------------------------------")

print("THANK YOU FOR COMMING!!")

print("============================end========================================")