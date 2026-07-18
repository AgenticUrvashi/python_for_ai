# Task 17 — Sort Students by Marks (list of dicts)
# Ek list of dicts banao: [{"name": "Asha", "marks": 85}, ...] (kam se kam 4 students).
#  Unhe marks ke descending order mein sort karke print karo (rank ke saath). Original list ko mat badlo.

# Concepts: sorted(key=lambda ...), reverse=True, enumerate, nested access
# Hint: sorted(students, key=lambda s: s["marks"], reverse=True). Rank ke liye enumerate(..., start=1).




print("======================================== sort students by marks ========================================")

students = [{"name": "asha", "marks": 85},
        {"name": "shama", "marks": 90},
        {"name": "mohan", "marks": 98},
        {"name": "meera", "marks": 76},
        {"name": "rahul", "marks": 55}
]

new = sorted(students, key=lambda s: s["marks"], reverse=True)
# raw = print(new)

for i in enumerate(new, start=1):
        print(f"{i}")


print("-----------------------------------------------------------------------------------------------------")

