'Restate: Ek generator even_numbers(n) jo pehle n even number yield kare.'

# example:n = 10

# pseudocode:
            # 1.create function even_numbers(n):
            # 2.for i in range(1,n+1): yield i % 2 == 0
            # 3.create generator even_gen = even_numbers(10)
            # 4.for i,even in zip([1,2,3,4,5,6,7,8,9,10],even_gen)
            # 5.print(f"{i} : {even}")

def even_numbers(n):
    for i in range(1,n+1):
        yield i % 2 == 0

even_gen = even_numbers(10)

for i,even in zip([1,2,3,4,5,6,7,8,9,10],even_gen):
    print(f"{i} : {even}")

# dry run:
# 1 : False
# 2 : True
# 3 : False
# 4 : True
# 5 : False
# 6 : True
# 7 : False
# 8 : True
# 9 : False
# 10 : True