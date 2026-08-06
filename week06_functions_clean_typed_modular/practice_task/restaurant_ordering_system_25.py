'''EN: Store a menu as a dict {"pizza": 200, "burger": 120, "coke": 50}. 
Write add_to_order(order, item) (returns updated order list) and bill(order, menu, tax=5) (returns total with tax). 
Run a menu loop to add items, then print an itemised bill.
हिंदी: menu को dict {"pizza": 200, "burger": 120, "coke": 50} में रखो। 
add_to_order(order, item) बनाओ (updated order list return करे) और bill(order, menu, tax=5) (tax के साथ total return करे)। 
items जोड़ने के लिए menu loop चलाओ, फिर itemised bill print करो।
Concepts: dict lookup, */default args, list building, loop, return
Hint: bill = sum(menu[item] for item in order), then add subtotal * tax / 100.'''

# restate: hame ek isa code likhana hai jo order le aur uska bill bhi mangne pr de.

# example:if we choose 1 then append item name then choose 2 then we have bill with 5% tax.

# pseudocode:
            # 1.starts with given input.
            # 2.create new variable order = []
            # 3.create functions add_to_order(order,item) and bill(order,menu,tax=5)
            # 4.use while loop.
            # 5.print choise and options.
            # 6.take input from user for choice.
            # 7. if 1 then print menu and take user's input as whats the order print current order.
            # 8.if 2 then if no items is selected then print no item is selected.else call bill function.
            # 9.if 3 then print thank you and break.
            # 10.else print invalid input. 

menu = {"pizza": 200, "burger": 120, "coke": 50}

order = []

def add_to_order(order, item):
    if item not in menu:
        print("not available")
        return order

    order.append(item)
    return order

def bill(order,menu,tax=5):
    subtotal = sum(menu[item] for item in order)
    tax_amount = subtotal * tax / 100
    final_bill = subtotal + tax_amount
    return subtotal, tax_amount , final_bill

while True:
    
    print("=======choice======")
    print("1) order")
    print("2) bill")
    print("3) exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        print("========== menu ==========")
        print("pizza : 200")
        print("burger : 120")
        print("coke : 50")
        user = input("enter order: ").lower().split(",")
        for i in user:
            add_to_order(order , i.strip())
        print("Current Order:", order)

    elif choice == 2:
        if not order:
            print("no items ordered.")
        else:
            subtotal,tax_amount,final_bill = bill(order, menu)

            print("============bill============")
            for item in order:
                print(f"{item:<10} , ₹{menu[item]}")

            print("----------------------------")
            print("Subtotal:", subtotal)
            print("Tax (5%):", tax_amount)
            print("Total :", final_bill)
        

    elif choice == 3:
        print("============================= THANK YOU =====================================")
        break

    else:
        print("Invalid input")

# dry run:

# =======choice======
# 1) order
# 2) bill
# 3) exit
# enter your choice: 1
# ========== menu ==========
# pizza : 200
# burger : 120
# coke : 50
# enter order: pizza
# Current Order: ['pizza']
# =======choice======     
# 1) order
# 2) bill
# 3) exit
# enter your choice: 2    
# ============bill============
# pizza      , ₹200
# ----------------------------
# Subtotal: 200
# Tax (5%): 10.0
# Total : 210.0
