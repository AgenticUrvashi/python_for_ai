# que : make_counter() banao jo har call par badhta number de (closure se).

# restate:ek function banao jo har call par badhta number de (closure se).

# example: make_counter(2) = 2,3,4,5,6,7,8,9,10

# pseudocode:
# 1.create a function called make_counter.
# 2.pass the parameter n to the function.
# 3.print the value of n.
# 4.if n is less than 10, return the function make_counter with the parameter n+1.
# 5.return the value of n.
# 6.call the function make_counter with the parameter.

# translate to code:

def make_counter(n=int) -> int:
    print(n)
    if n < 10:
        return make_counter(n+1)
    return n

make_counter(2)
print("---------------------------------")
make_counter(0)

# dry run:

2
3
4
5
6
7
8
9
10
"----------------------------------------------"
0
1
2
3
4
5
6
7
8
9
10