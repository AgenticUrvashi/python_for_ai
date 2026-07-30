# que: Ek function is_even(n) jo True/False return kare; 5 numbers par test karo.

# restate:even value hai to True nhi to false.

# example : n = 3,4,7,5,8

# pesudocode:
            # 1.create function is_even(n)
            # 2.create new variable nums = false.
            # 3.if n % 2 == 0 then update nums = True.
            # 4.return nums
            # 5.print the function with variable agrument.

# translate:
def is_even(n):
    nums = False
    if n % 2 == 0:
        nums = True
    return nums

print(is_even(3))
print(is_even(4))
print(is_even(7))
print(is_even(5))
print(is_even(8))

# dry run:
False
True
False
False
True