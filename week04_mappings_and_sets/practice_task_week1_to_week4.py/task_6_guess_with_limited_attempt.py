# Task 6 — Guess with Limited Attempts
# Ek secret number fix karo (secret = 42). User ko sirf 3 chances do guess karne ke. Har galat guess par "Too high" / "Too low" batao. 3 ke andar sahi → "You won", warna → "Game over, number was 42".

# Concepts: while, break, counter, if/elif/else
# Hint: attempts counter rakho, while attempts < 3. Sahi guess par break.

# ans:

print("===============================Guess with Limited Attempts===============================")

print("WEL-COME to our game!!")
secret = 42
print("-----------------------------------------------------------------------------------------")
attempts=0
while attempts<3:
    user_input = int(input("enter your guess number: "))
   
    if user_input>secret:
        print("too high")
        attempts += 1
        print("----------------------------------------------------------------------------------")
    elif user_input<secret:
        print("too low")
        attempts += 1
        print("----------------------------------------------------------------------------------")
    else:
        print("you are win!!!")
        break

print("=======================================THANK YOU ==========================================")