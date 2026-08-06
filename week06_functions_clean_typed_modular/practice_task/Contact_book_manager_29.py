'''EN: Build a contact book (dict of name → phone). Write functions add_contact, search_contact, delete_contact, 
and show_all, each taking and returning/using the contacts dict safely. Run a full while menu with options 1-5 (5 = Exit).
हिंदी: एक contact book बनाओ (dict: name → phone)। functions बनाओ add_contact, search_contact, delete_contact, 
और show_all, हर एक contacts dict को safely ले और return/use करे। पूरा while menu चलाओ options 1-5 के साथ (5 = Exit)।
Concepts: dict CRUD, multiple functions, .get(), in check, menu loop
Hint: In search_contact, use contacts.get(name) and handle None (not found).'''

# restate: hame isa program likha hai jo user ke kehne anusar contact add , search , delete kare aur sare contact show bhi kare.

# example: when we add radha having no. 45632 then output is contact added.

# pseudocode:
            # 1.starts with makeing dict having name and phone no.
            # 2.create functions add_contact(contacts,name,phone): contacts[name] = phone return "contact added"
            # 3.search_contact(contacts,name): if name in contacts: phone = contacts.get(name) return phone else not found
            # 4.delete_contact(contacts,name): if name in contacts: return contacts.pop(name) else not found.
            # 5.show_all(contacts): use for loop for name, phone then print(name,":",phone)
            # 6.use while loop until it's True.
            # 7.print menu with option dd_contact, search_contact, delete_contact, show_all,exit
            # 8.take input from user for chocing options.
            # 9.if 1 then take two input name and no. then print function.
            # 10.if 2 then take one input name then print function.
            # 11.if 3 then take one input name then print function.
            # 12.if 4 then print function.
            # 13.if 5 then print thank you and break.
            # 14.else invalid function.

# translate:

contacts = {
    "asha":96432,
    "rahul":82345,
    "anjali":82435,
    "teena":54328,
    "pk":67895
}

def add_contact(contacts,name,phone):
    contacts[name] = phone
    return "contact added"

def search_contact(contacts,name):
    if name in contacts:
        phone = contacts.get(name)
        return phone
    else:
        return "not found"

def delete_contact(contacts, name):
    if name in contacts:
        return contacts.pop(name)
    else:
        return "not found"

def show_all(contacts):
    for name, phone in contacts.items():
        print( name,":",phone)


print("========================= contact book manager =======================")

while True:

    print("===== MENU =====")
    print("1)add new contact")
    print("2)search contact name")
    print("3)delete contact")
    print("4)show all contacts")
    print("5)Exit")

    print("-------------------------------------------------")

    choice = int(input("Enter your choice: "))

    print("--------------------------------------------------")

    if choice == 1:
        input1 = input("enter name: ")
        input2 = int(input("enter phone no.: "))
        print(add_contact(contacts,input1,input2))

    elif choice == 2:
        name = input("enter name to search: ")
        print(search_contact(contacts,name))

    elif choice == 3:
        input1 = input("enter name: ")
        print(delete_contact(contacts , input1))

    elif choice == 4:
        show_all(contacts)
        print("----------------------------------------------")

    elif choice == 5:
        print("THANK YOU")
        break

    else:
        print("Invalid input")

print("======================== END =============================")

# dry run:

# ===== MENU =====
# 1)add new contact
# 2)search contact name
# 3)delete contact
# 4)show all contacts
# 5)Exit

# Enter your choice: 4

# asha : 96432
# rahul : 82345
# anjali : 82435
# teena : 54328
# pk : 67895

# ===== MENU =====
# 1)add new contact
# 2)search contact name
# 3)delete contact
# 4)show all contacts
# 5)Exit

# Enter your choice: 5
# THANK YOU