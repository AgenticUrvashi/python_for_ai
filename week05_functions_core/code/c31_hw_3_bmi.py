# restate: ek function bmi(weight,height) jo BMI return kare (weight / height**2).

# example:weight=40 and height=4.8 then the output is 1.736.

# pseudocode:
            # 1.create a function bmi(weight,height).
            # 2.create new variable BMI = weight / height**2
            # 3.return BMI.
            # 4.print the function with parameters.

# translate:
def bmi(weight,height):
    BMI = weight / height**2
    return BMI

print(bmi(40,4))

# dry run:
# step | output | wei | hei |
#   1  |   -    | 40  |  4  |
#   2  |  2.5   | 40  |  4  |

# final output:
2.5