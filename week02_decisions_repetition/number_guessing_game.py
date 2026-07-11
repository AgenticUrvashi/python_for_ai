import random
print("=================number guessing game==================")
while True:
    secret = random.randint(1,100)

    for i in range(5):
        print(f"attempt {i+1} of 5")
        user_input = int(input("your guessing: "))

        if user_input>secret:
            print("too high,enter another number!")

        elif user_input<secret:
            print("too low, enter another number!")

        else:
            print(f"congratulation!! you win in {i+1} attempts.")
            break

        print("--------------------------------------------------")


    print(f"the secret number was: {secret}")
    print("=="*25)
    user_inp = input("do you want to continue(yes or no): ")

    if user_inp=="no":
        break

    print("====================thank you==========================")