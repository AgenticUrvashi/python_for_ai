# restate: range(2, 30) mein saare prime numbers print karo (Concept 3 ko loop mein daalo).

# example: range(2,10) then the output=2,3,5,7

# pseudocode:
            # 1.use for loop for range(2,30)
            # 2.use flag give value true.
            # 3.use for loop again for range(2,nums)
            # 4.fix the condition as num % x == 0.
            # 5.change the falg into false.
            # 6.fix the condition as : if is_prime then print num.


# translate:
for num in range(2,30):
    is_prime = True
    for x in range(2,num):
        if num % x == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# dry run:
# step | num | x | falg |
#   1  |  2  | - | True |
#   2  |  2  | 2 | True |
#   3  |  3  | 2 | True |
#   4  |  4  | 2 | False|
#   5  |  5  | 2 | True |
#   6  |  5  | 3 | True |
#   7  |  5  | 4 | True |
#   8  |  6  | 2 | False|
#   9  |  7  | 2 | True |
#   10 |  7  | 3 | True |
#   11 |  7  | 4 | True |
#   12 |  7  | 5 | True |
#   13 |  7  | 6 | True |
#   14 |  8  | 2 | False|
#   15 |  9  | 2 | True |
#   16 |  9  | 3 | False|
#   17 |  10 | 2 | False|
#   18 |  11 | 2 | True |
#   19 |  11 | 3 | True |
#   20 |  11 | 4 | True |
#   21 |  11 | 5 | True |
#   22 |  11 | 6 | True |
#   23 |  11 | 7 | True |
#   24 |  11 | 8 | True |
#   25 |  11 | 9 | True |
#   26 |  11 | 10| True |
#   27 |  12 | 2 | False|
#   28 |  13 | 2 | True |
#   29 |  13 | 3 | True |
#   30 |  13 | 4 | True |
#   31 |  13 | 5 | True |
#   32 |  13 | 6 | True |
#   33 |  13 | 7 | True |
#   34 |  13 | 8 | True |
#   35 |  13 | 9 | True |
#   36 |  13 | 10| True |
#   37 |  13 | 11| True |
#   38 |  13 | 12| True |
#   39 |  14 | 2 | False|
#   40 |  15 | 2 | False|
#   41 |  15 | 3 | False|
#   42 |  16 | 2 | False|
#   43 |  17 | 2 | True |
#   44 |  17 | 3 | True |
#   45 |  17 | 4 | True |
#   46 |  17 | 5 | True |
#   47 |  17 | 6 | True |
#   48 |  17 | 7 | True |
#   49 |  17 | 8 | True |
#   50 |  17 | 9 | True | 
#   51 |  17 | 10| True |
#   52 |  17 | 11| True |
#   53 |  17 | 12| True |
#   54 |  17 | 13| True |
#   55 |  17 | 14| True |
#   56 |  17 | 15| True |
#   57 |  17 | 16| True |
#   58 |  18 | 2 | False|
#   59 |  19 | 2 | True|
#              to|
#              18| 
#   60 | 20 | 2 | False|
#   61 | 21 | 2 | True |
#   62 | 21 | 3 | False|
#   63 | 22 | 2 | False|
#   64 | 23 | 2 | True |
#             to|
#             22|
#   65 | 24 | 2 | False|
#   66 | 25 | 2 | True |
#   67 | 25 | 3 | True |
#   68 | 25 | 4 | True |
#   69 | 25 | 5 | False|
#   70 | 26 | 2 | False|
#   71 | 27 | 2 | True
#             to|
#             26|
#   72 | 28 | 2 | True |
#   73 | 29 | 2 | True |
#            to |
#            28 |

# final output:
2
3
5
7
11
13
17
19
23
29
