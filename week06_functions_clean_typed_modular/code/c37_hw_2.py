# que : recursion se factorial(6) nikaalo.

# restate: 6 ka factorial nikhalo.

# example: 6 ka factorial 720 hai

# pseudocode:
            # 1.create function factorial(n).
            # 2.if n == 1 return 1.
            # 3.return n * factorial(n-1)
            # 4.print the function.

# translate:
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(6))

# dry run:
720