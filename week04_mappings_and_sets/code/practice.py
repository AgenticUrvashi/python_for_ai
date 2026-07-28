print("---------------------------------------------------------------------------------------------")

print("====================================== contact number =======================================")

print("---------------------------------------------------------------------------------------------")

import copy

contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})

# kuch contacts add karo
add_contact("Asha", "98765")
add_contact("Rahul", "91234")
add_contact("Priya", "90000")

# naam ke hisaab se sorted dikhao (original safe rehe)
for c in sorted(contacts, key=lambda c: c["name"]):
    print(f"{c['name']}: {c['phone']}")

# ek safe copy par kaam karo (original ko mat chhuо)
backup = copy.deepcopy(contacts)
backup[0]["phone"] = "00000"
print(f"Original first phone still: {contacts[0]['phone']}")   # 98765 (safe!)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ end ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
