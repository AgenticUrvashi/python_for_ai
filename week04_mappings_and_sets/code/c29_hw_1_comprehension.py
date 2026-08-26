### que 1 : 1–20 ke saare numbers ka comprehension banao, sirf woh jo 3 se divisible hain.

divisible_3 = [i for i in range(1, 21) if i % 3 == 0]
print(divisible_3)


# simple way =
# for i in range(1,21):
#     if i % 3 == 0:
#         print(i)