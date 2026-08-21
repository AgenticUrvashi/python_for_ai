'Ek custom exception NegativeNumberError banao aur ek function jo negative pr use raise kare.'

# restate: custom error banake use function me use karke dikhao.

# example: n = -9

# pseudocode:
            # 1.create custom error by using class NegativeNumberError(Exception) then "raise when number negative" then pass
            # 2.create function negative(n)
            # 3.if n < 0 then raise NegativeNumberError("this input cannot be negative...")
            # 4.else print("congrts! Your input is correct...")

class NegativeNumberError(Exception):
    "raise when number negative"
    pass

def negative(n):
    if n < 0:
        raise NegativeNumberError("this input cannot be negative...")

    else:
        print("congrts! Your input is correct...")

negative(-9)

# dry run:
# give error