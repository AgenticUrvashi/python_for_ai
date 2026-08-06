'''EN: Refactor the guessing game into functions: check_guess(guess, secret) returns "low"/"high"/"correct", 
and play(secret, max_attempts) runs the whole game loop using it, returning True if the player won. 
Print win/lose with attempts used.
हिंदी: guessing game को functions में बाँटो: check_guess(guess, secret) जो "low"/"high"/"correct" return करे, 
और play(secret, max_attempts) जो पूरा game loop चलाए और जीतने पर True return करे। कितने attempts लगे उसके 
साथ win/lose print करो।
Concepts: helper functions, while, counter, return a boolean
Hint: Loop while attempts < max_attempts; on "correct" return True; after loop return False.
'''

# restate: hame esa function banana hai jo guessing game ko do functions me bat de.

# example:hamare pass 5 attempts hai agar hamara guessing guessing wrong hua to lose aur false aur 
# agar sahi hua to win aur true print hoga 5 attempt ke baad fir se puchha jayega aap fir se khelna chahte ho ya nahi.

# pseudocode:
            # 1.import random.
            # 2.create function check_guess(guess,secret)
            # 3.if guess > secret return high.
            # 4.if guess < secret return low.
            # 5.else return correct.
            # 6.create another function play(secret,max_attempt)
            # 7.use for loop for range(1,max_attempt+1)
            # 8.take user input for entering guessing.
            # 9.create new variable result and call the function check_guess
            # 10.if result == correct return True.
            # 11.else print result.
            # 12.print max_attempt 
            # 13.print secret
            # 14.create secret variable = random.randint(1,100)
            # 15.create another variable max_attempt = 5
            # 16.play(secret,max_attempt)

# translate:

print("==================================== Number guessing game ===================================== ")

import random

def check_guess(guess,secret):
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    else:
        return "correct"


def play(secret,max_attempts):
    for attempt in range(1,max_attempts+1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}:enter your guessing: "))

        result = check_guess(guess, secret)

        if result == "correct":
            print(f"you win! Attempts used:{attempt}")
            return True

        else:
            print(result)

    print(f"you lose! Attempts used: {max_attempts}")
    print(f"the secret number was: {secret}")
    return False


secret = random.randint(1,100)
max_attempts = 5

play(secret,max_attempts)

print("========================================== end ==============================================")



# print("=======================================Number guessing game=============================================")


# secret = random.randint(1,100)
# max_attempts = 5

# while True:

#     for i in range(5):
#         print(f"attempt {i+1} of 5")

#         user_guess = int(input("enter your guessing: "))
#         print( )
#         print(check_guess(user_guess,secret))
#         if user_guess == secret:
#             break
#         print( )

#     print(play(secret,max_attempts))

#     print("--------------------------------------------------------------------------------------------------")

#     user_choice = input("Do you want to continue your game(y/n): ")
#     if user_choice == "n":
#         break

#     print( )
    
# print("=============================================end=======================================================")

