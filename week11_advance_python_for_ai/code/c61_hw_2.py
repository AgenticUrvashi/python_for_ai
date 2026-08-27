'Restate: Ek generator countdown(n) jo n se 1 tak yield kare.'

# example: n = 10

# pseudocode:
            # 1.create function countdown(n):
            # 2.for i in range(n,0,-1): yield i
            # 3.create generator count_gen = countdown(10)
            # 4.for count in count_gen: print(count)

def countdown(n):
    for i in range(n,0,-1):
        yield i

count_gen = countdown(10)

for count in count_gen:
    print(count)

# dry run:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1