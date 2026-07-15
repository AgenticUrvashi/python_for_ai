# Task 3 — Even ya Odd + Positive/Negative
# User se ek number lo. Batao woh positive/negative/zero hai, AUR even/odd hai (zero ke liye even/odd mat batao).

# Concepts: if/elif/else, modulus %, ternary
# Hint: even/odd ke liye n % 2 == 0. Ek ternary se "Even"/"Odd" choose karo.
# ans:

print("==================Even ya Odd + Positive/Negative=====================")

number = int(input("enter any number: "))

print("----------------------------------------------------------------------")

if number>0:
    print("positive")
    
    if number%2==0:
        print("even")

    else:
        print("odd")


elif number<0:
    print("negative")

    if number%2==0:
        print("even")

    else:
        print("odd")
else:
    print("zero")


print("===============================end=================================")