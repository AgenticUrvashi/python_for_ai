'tools.py mein ek aur function add karo: is_palindrome(text: str) -> bool (typed + docstring).'

# restate: hame palindrome ka function tools me dalna hai.

# example: text = madam, the output is True.

# pseudocode:
            # 1.import math
            # 2.create function is_palindrome(text:str) -> bool
            # 3.use docstring.
            # 4.return text == text[::-1]

# in tools

def is_palindrome(text: str) -> bool:

    """Check if a text reads the same forwards and backwards."""

    return text == text[::-1]

print(is_palindrome("madam"))

print(is_palindrome("pashu"))

# dry run:
True