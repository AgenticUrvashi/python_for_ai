#restate: 1 se 20 tak ke numbers mein se sirf 3 ke multiples print karo.
# example:when the range is 1 to 16 then the output is 3,6,9,12,15.
# pseudocode:1.use for loop as:for n in range(1,21)
            # 2.if n % 3 == 0 then print n.

# translate:

for n in range(1, 21):

    if n % 3 == 0:

        print(n)

# dry run:
# step | n | output |
#   1  | 1 |    -   |
#   2  | 2 |    -   |
#   3  | 3 |    3   |
#   4  | 4 |    3   |
#   5  | 5 |    3   |
#   6  | 6 |   3,6  |
#   7  | 7 |   3,6  |
#   8  | 8 |   3,6  |
#   9  | 9 |  3,6,9 |
#  10  | 10|  3,6,9 |
#  11  | 11|  3,6,9 |
#  12  | 12| 3,6,9,12|
#  13  | 13| 3,6,9,12|
#  14  | 14| 3,6,9,12|
#  15  | 15| 3,6,9,12,15|
#  16  | 16| 3,6,9,12,15|
#  17  | 17| 3,6,9,12,15|
#  18  | 18| 3,6,9,12,15,18|
#  19  | 19| 3,6,9,12,15,18|
#  20  | 20| 3,6,9,12,15,18|

# final output:
3
6
9
12
15
18