correct_password = "python123"

attempts = 0

while attempts < 3:

    guess = input("Enter password: ")

    if guess == correct_password:

        print("Access granted ✅")

        break

    else:

        attempts = attempts + 1

        print(f"Wrong! {3 - attempts} attempts left")

if attempts == 3:

    print("Account locked 🔒")
