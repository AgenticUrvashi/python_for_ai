# Task 18 — Contact Book with Search (nested dict)
# Ek dictionary of dicts banao:

# contacts = {
#     "Asha":  {"phone": "98765", "city": "Mumbai"},

#     "Rahul": {"phone": "91234", "city": "Delhi"},
# }

# User se ek naam maango. .get() se safely dhoondho — mile toh phone + city print karo, na mile toh "Contact not found".

# Concepts: nested dict, .get(), input(), if/else
# Hint: contacts.get(name) pehle — agar None mila toh not found, warna andar ke fields access karo.

print("==================================== contact book with search ==================================")

contacts = {
    "Asha":  {"phone": "98765", "city": "Mumbai"},

    "Rahul": {"phone": "91234", "city": "Delhi"},

    "mohan": {"phone": "87234", "city": "indor"},

    "radha": {"phone": "87432", "city": "nagpur"}
}


user_input = input("enter the contact name: ")

print("------------------------------------------------------------------------------------------------")

if contacts.get(user_input):

    print(f"phone:{contacts[user_input]["phone"]}")

    print("--------------------------------------------------------------------------------------------")
    
    print(f"city: {contacts[user_input]["city"]}")

else:
    print("contact not found")

print("================================================== end ===========================================")