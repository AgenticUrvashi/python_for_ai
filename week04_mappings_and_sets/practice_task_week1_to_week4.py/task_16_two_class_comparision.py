# Task 16 — Two Class Comparison (sets)
# Do sets banao: python_students aur java_students (kuch naam dono mein common ho).
#  Print karo: (a) dono seekhne wale, 
# (b) sirf Python, (c) total unique students,
#  (d) sirf ek language seekhne wale.

# Concepts: set operations &, -, |, symmetric difference ^
# Hint: "sirf ek language" = python ^ java (symmetric difference).


print("================================Two Class Comparison=====================================")

python_student = {"shama","radha","mohan","rama"}
java_student = {"sita","rakhu","rama","rahul","shama"}

total= python_student | java_student
both= python_student & java_student
only_one = total-both
one = python_student ^ java_student

print(f"a. {both}")
print("-----------------------------------------------------------------------------")
print(f"b. {python_student}")
print("-----------------------------------------------------------------------------")
print(f"c. {total}")
print("-----------------------------------------------------------------------------")
print(f"d. {only_one}")
print("-----------------------------------------------------------------------------")
print(f"d. {one}")

print("============================================== end =======================================")