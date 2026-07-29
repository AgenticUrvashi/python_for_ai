# Q37
# EN: Two lists are given. Print the values common to both (use sets).
# Given: a = [1, 2, 3, 4], b = [3, 4, 5, 6]

# restate:Do lists di hain. Dono mein common values print karo (sets).

# example: a = [9, 2, 3, 4, 6], b = [3, 4, 5, 6] then the output is {2,3,6}

# pseudocode:
            # 1.initilize with given input list.
            # 2.list convert into set with the help of a = set(a)
            # 3.create new variable same = a & b
            # 4.print same.

# translate:
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
a = set(a)
b = set(b)
same = a & b
print(same)

# dry run:
# step | a & b |
#   1  |   -   |
#   2  | {3,4} |

# final output:
{3,4}