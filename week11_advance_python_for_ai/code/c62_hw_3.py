'Restate: @timer ko ek function par lagao jo loop chalata hai.'

# example: when we use loop for square of numbers.

# pseudocode:
            # 1.create decorator timer(func):
            # 2.create function wrapper(n):
            # 3.use for i in range(1,n+1) then create variable result = func(i ** 2) then print(result)
            # 4.return wrapper
            # 5.write @timer
            # 6.create function time(n) then return n
            # 7.call time(10)

def timer(func):
    def wrapper(n):
        for i in range(1,n+1):
            result = func(i ** 2)
            print(result)

    return wrapper

@timer
def time(n):
    return n

time(10)

# dry run:
1
4
9
16
25
36
49
64
81
100

