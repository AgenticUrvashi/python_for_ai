# Task 19 — Number Grid + Diagonal Sum (nested list)
# Ek 3x3 grid banao:

# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Poora grid tidy print karo (rows/columns aligned). Phir main diagonal ka sum (1+5+9) nikaalo.

# Concepts: nested list, nested loop, grid[i][i], running total
# Hint: diagonal ke liye ek hi index use karo: grid[i][i] for i in range(3).


print("==================================Number Grid + Diagonal Sum =================================")

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in grid:
    for item in row:
        print(item , end=" ")

    print()

print("-----------------------------------------------------------------------------------------------")

diagonal_sum = [grid[i][i] for i in range(3)]
final = sum(diagonal_sum)
print(f"the sum of diagonal is {final}")

print("============================================== end =============================================")
