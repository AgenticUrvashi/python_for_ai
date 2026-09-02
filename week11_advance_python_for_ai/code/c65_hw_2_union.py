'Restate: Ek function jo int | None return kare (mile toh number, nahi toh None).'

# example: a = 2, b = 0 and a = 9, b = 3

# pseudocode:
            # 1.create function divide(a:int,b:int) -> int | None
            # 2.if b == 0: return None
            # 3.return a / b
            # 4.print(divide(2,0)) ; print(divide(9,3))

# translate:
def divide(a:int,b:int) -> int | None:
    if b == 0:
        return None
    return a / b

print(divide(2,0))
print(divide(9,3))

# dry run:
# None
# 3.0