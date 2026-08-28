# class_hw = memory naam ka decorator banao jo class 61 ke base pr memory stored bataye.

import sys

def memory(func):
    """This is a decorator which is use for memory checking."""
    def wrapper(n):
        result = func(n)
        size = sys.getsizeof(result)
        print(f"{size} memory is stored.")
    return wrapper
        
@memory
def numbers(n):
    for i in range(1,n+1):
        cube = i ** 3
    print(f"{cube} is cube of {n}")

numbers(10)

# dry run:
# 1000 is cube of 10
# 16 memory is stored.