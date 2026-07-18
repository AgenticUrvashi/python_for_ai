# Task 12 — FizzBuzz (classic logic test)
# 1 se 30 tak loop chalao. 3 se divisible → "Fizz", 5 se divisible → "Buzz", dono se → "FizzBuzz", warna number khud print karo.

# Concepts: for loop, %, nested/ordered if/elif/else
# Hint: order matter karta hai — pehle dono (15) wala check karo, warna sirf Fizz/Buzz kabhi FizzBuzz nahi banega.
# ans:

print("===============================FizzBuzz (classic logic test)================================")

for i in range(1,30):
    user_input = int(input("enter number: "))
    if user_input % 3==0 and user_input % 5==0:
        print("FizzBuzz")
    elif user_input % 3==0:
        print("Fizz")
    elif user_input % 5==0:
        print("Buzz")
    else:
        print(user_input)

    print("============================================= end ==============================================")

