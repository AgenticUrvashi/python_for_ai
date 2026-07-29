# Q40
# EN: A dict of name → marks is given. Build a new dict of name → "Pass"/"Fail" (pass if marks ≥ 40).
# Given: marks = {"Asha": 35, "Ravi": 80, "Zoya": 40}

# restate:name → marks ki dict di hai. name → "Pass"/"Fail" ki nayi dict banao (40+ = Pass).

# example:asha=35 then the output is Fail.

# pseudocode:
            # 1.starts with marks variable.
            # 2.use for loop for dict as: for key,value in marks.items().
            # 3.if value > 40 then Pass.
            # 4.else Fail.
            # 5.print(f"{key}:{student}")

# translate:
marks = {"Asha": 35, "Ravi": 80, "Zoya": 40}

for key,value in marks.items():
    if value > 40:
        student= "Pass"
    else:
        student= "Fail"

    print(f"{key}:{student}")

# dry run:
# step | value | key | student |
#   1  |   35  |asha |  Fail   |
#   2  |   80  |ravi |  Pass   |
#   3  |   40  |zoya |  Fail   |

# final output:
# asha:Fail
# ravi:Pass
# zoya:Fail