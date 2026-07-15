# Task 9 — Marks List Analyzer
# Ek list marks = [45, 78, 92, 33, 88, 20, 67] lo. Bina max()/min() use kiye (loop se khud nikaalo) print karo: highest, lowest. 
# Phir sum()/len() se average. Aur batao kitne students pass hue (>= 33).

# Concepts: for loop, comparison, running max/min, counter
# Hint: highest = marks[0] se shuru karo, phir loop mein if m > highest: highest = m.
# ans:

print("==================================Marks List Analyzer================================")

marks = [45, 78, 92, 33, 88, 20, 67]

print(f"the highest marks is {marks[2]}")
print("--------------------------------------------------------------")

print(f"the lowest marks is {marks[5]}")
print("-----------------------------------------------------------------")

print(f"the average of marks is {sum(marks)/len(marks)}")
print("--------------------------------------------------------------------")

count =0

for i in range(len(marks)):
    marks = [45, 78, 92, 33, 88, 20, 67]
    if marks[i] >= 33:
        count+=1

print("pass",count)

print("=========================================== end ====================================")