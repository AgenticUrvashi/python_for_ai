'''EN: Write check_strength(password) that returns "Weak", "Medium", or "Strong" based on how many rules it passes:
 length ≥ 8, has a digit, has an uppercase, has a lowercase, has a special character. Test it on 3 different passwords 
 and print each verdict.
हिंदी: check_strength(password) बनाओ जो कितने नियम पास हुए उसके आधार पर "Weak", "Medium", या "Strong" return करे: 
length ≥ 8, एक digit हो, एक uppercase हो, एक lowercase हो, एक special character हो। इसे 3 अलग passwords पर test करके 
हर verdict print करो।
Concepts: helper functions or any(), counting conditions, string checks, return

Hint: Count how many of the 5 checks are True. 4-5 → Strong, 2-3 → Medium, else Weak.'''


# restate: hame ek isa function banana hai jo bataye ki hamara password strong,medium and weak hai.

# example: password = hello then the output is weak.

# pseudocode:
            # 1.create function check_strength(password).
            # 2.create variables length = len(password) >= 8.
            # 3.digit = any(ch.isdigit() for ch in password).
            # 4.upper = any(ch.isupper() for ch in password).
            # 5.lower = any(ch.islower() for ch in password).
            # 6.special = any(not ch.isalnum() for ch in password).
            # 7.count = length + digit + upper + lower + special.
            # 8.if count >= 4 then return strong.
            # 9.if count >= 2 then return medium.
            # 10.else return weak.
            # 11.print the function.

# translate:

def check_strength(password):

    length = len(password) >= 8
    digit = any(ch.isdigit() for ch in password)
    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password )
    special = any(not ch.isalnum() for ch in password)


    count =length + digit + upper + lower + special

    if count >= 4:
        return "Strong"
    elif count >= 2:
        return "medium"
    else:
        return "weak"

print(check_strength("hello"))
print(check_strength("123hello"))
print(check_strength("123@hello"))

# dry run:
'weak'
'medium'
'strong'