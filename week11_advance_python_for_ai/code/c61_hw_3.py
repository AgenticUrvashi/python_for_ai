'Restate: Generator expression se 1-100 ke squares ke sum nikaalo.'

# example: n = 101

# pseudocode:
            # 1.create function square(n):
            # 2.for i in range(1,n) : yield i ** 2
            # 3.cerate generator sq_gen = square(101)
            # 4.create variable sq_sum = sum(sq_gen) then print(sq_gen)

def square(n):
    for i in range(1,n):
        yield i ** 2

sq_gen = square(101)

sq_sum = sum(sq_gen)

print(sq_sum)

# dry run:
# 338350