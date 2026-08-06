'''EN: Build a shopping system. Functions: add_item(cart, name, price, qty) (returns updated cart list of dicts), 
cart_subtotal(cart), apply_discount(subtotal, percent=0), and print_invoice(cart, discount_percent=0). Add at least
 3 items, apply a discount, and print a neat itemised invoice with subtotal, discount, and grand total.
हिंदी: एक shopping system बनाओ। Functions: add_item(cart, name, price, qty) (dicts की updated cart list return करे),
 cart_subtotal(cart), apply_discount(subtotal, percent=0), और print_invoice(cart, discount_percent=0)। कम से कम 3 
 items जोड़ो, discount लगाओ, और subtotal, discount, और grand total के साथ साफ़-सुथरा itemised invoice print करो।
Concepts: list of dicts, multiple cooperating functions, defaults, return, formatting
Hint: Each cart item is a dict {"name":..., "price":..., "qty":...}. Subtotal = sum(i["price"] * i["qty"] for i in cart).'''

# restate:ek isa program banao jo shopping cart system banye jisme add item kar sake total bataye aur bill de.

# example: item=pen,book,pencil price=10,40,5 qty=2,4,2 then the output is 190.

# pseudocode:
            # 1.create empty list having name cart.
            # 2.create functions add_item(cart, name, price, qty). create dict item having name,price,qty then cart.append(item)
            #   return cart.
            # 3.cart_subtotal(cart) create subtotal = sum(i["price"] * i["qty"] for i in cart) return subtotal.
            # 4.apply_discount(subtotal,percent=0) create new variable discount = subtotal*percent/100
                # if discount>0 then grand total = subtotal - discount return grand total else return subtotal.
            # 5.print invoice(cart,discount_percent=0) then print name,price,qty,total. for i in cart :
                # item_total = i["price"] * i["qty"] then print(i["name"],i["price"],i["qty"],item_total).
            # 6.create variables subtotal=cart_subtotal(cart) and grand_total=apply_discount(subtotal,percent=discount_percent)
            # 7.print subtotal,discount and grand_total with the help of f-string.
            # 8.use while loop until it's true.
            # 9.print menu with options.
            # 10.take input from user to choice from menu.
            # 11.if 1 then take three input name,price,qty then print function.
            # 12.if 2 then print function.
            # 13.if 3 then  subtotal = cart_subtotal(cart) then take input for discount.print function.
            # 14.if 4 then take input for discount percent then print function.
            # 15.if 5 then print thank you and break.
            # 16.else print invalid function.

# translate:

cart = []

def add_item(cart, name, price, qty):
    item = {
    "name": name,
    "price": price,
    "qty": qty
    }
    cart.append(item)
    return cart

def cart_subtotal(cart):
    Subtotal = sum(i["price"] * i["qty"] for i in cart)
    return Subtotal

def apply_discount(subtotal, percent=0):
    discount = subtotal * percent / 100
    if discount > 0:
        grand_total = subtotal - discount
        return grand_total
    else:
        return subtotal

def print_invoice(cart, discount_percent=0):
    print("Name\tPrice\tQty\tTotal")

    print("---------------------------------------------------------")

    for i in cart:

        item_total = i["price"] * i["qty"]
        print(i["name"],i["price"],i["qty"],item_total)

    print("---------------------------------------------------------")

    subtotal = cart_subtotal(cart)
    grand_total = apply_discount(subtotal,percent=discount_percent)

    
    print(f"Subtotal     : {subtotal}")
    print(f"Discount (%) : {discount_percent}")
    print(f"Grand Total  : {grand_total}")


print("======================== shopping cart & invoice genrator =============================")

while True:

    print("==== MENU ====")
    print("1)add item")
    print("2)cart subtotal")
    print("3)apply discount")
    print("4)print invoice")
    print("5)Exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        name = input("enter name of item: ")
        price = int(input("enter item's price: "))
        qty = int(input("enter item qty: "))
        print(add_item(cart,name,price,qty))

    elif choice == 2:
        print(cart_subtotal(cart))
    
    elif choice == 3:
        subtotal = cart_subtotal(cart)
        percent = int(input("enter discount: "))
        print("Grand total: ",apply_discount(subtotal,percent))

    elif choice == 4:
        discount_percent = int(input("enter your discount percent: "))
        print_invoice(cart,discount_percent)

    elif choice == 5:
        print( )
        print("thank you")
        break

    else:
        print("invalid input")

print("=================================== END ========================================")

# dry run:
# MENU   
# 1)add item
# 2)cart subtotal    
# 3)apply discount   
# 4)print invoice    
# 5)Exit
# enter your choice: 1
# enter name of item: pen
# enter item's price: 10
# enter item qty: 2
# [{'name': 'pen', 'price': 10, 'qty': 2}]
# MENU 
# 1)add item
# 2)cart subtotal
# 3)apply discount
# 4)print invoice
# 5)Exit
# enter your choice: 4
# enter your discount percent: 10
# Name    Price   Qty     Total

# pen 10 2 20

# Subtotal     : 20
# Discount (%) : 10
# Grand Total  : 18.0
# MENU 
# 1)add item
# 2)cart subtotal
# 3)apply discount
# 4)print invoice
# 5)Exit
# enter your choice: 5
# thank you