#que: Number guessing game ke 'compare' part ko ek function check_guess(guess, secret) 
# mein nikaalo jo "low"/"high"/"correct" return kare.

# restate:guess game ka campare wala concept ko function me represent karna.

# example:guess = 45,80,78 and secrete=78.

# pseudocode:
            # 1.create function check_guess(guess,secret)
            # 2.if guess<secret then return low.
            # 3.if guess>secret then return high.
            # 4.else return correct.
            # 5.print function with two argument.

# translate:
def check_guess(guess,secret):
    if guess<secret:
        return "low"
    elif guess>secret:
        return "high"
    else:
        return "correct"

print(check_guess(45,78))
print(check_guess(80,78))
print(check_guess(78,78))

# final output:
# low
# high
# correct