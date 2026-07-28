# Q32
# EN: Print FizzBuzz from 1 to 15 (3→Fizz, 5→Buzz, 15→FizzBuzz).

# restate:1 se 15 tak FizzBuzz print karo.(order matters: 15 wali shart pehle)

# example : yaha pr 3,6,9,12 ye fizz honge.5,10 ye buzz honge. aur 15 is fizzbuzz.

# pseudocode:
            # 1.for loop se shuru karte hai.
            # 2.if i is divided by 3 and 5 both then print fizzbuzz.
            # 3.if i is divided by 3 then print fizz.
            # 4.if i is divided by 5 then print buzz.

# translate:

for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# dry run.
# step | i | output |
#   1  | 1 |   1    |
#   2  | 2 |   2    |
#   3  | 3 |  fizz  |
#   4  | 4 |   4    |
#   5  | 5 |  buzz  |
#   6  | 6 |  fizz  |
#   7  | 7 |   7    |
#   8  | 8 |   8    |
#   9  | 9 |  fizz  |
#   10 | 10|  buzz  |
#   11 | 11|   11   |
#   12 | 12|  fizz  |
#   13 | 13|   13   |
#   14 | 14|   14   |
#   15 | 15|fizzbuzz|

# final output:
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
