'''EN: Write restaurant_bill(*prices, tax=5, tip=0) that returns the final total:
 sum of all item prices, plus tax%, plus tip%. Call it with tax defaulted and tip=10 passed as a keyword argument.
हिंदी: restaurant_bill(*prices, tax=5, tip=0) बनाओ जो final total return करे: सभी item prices का जोड़, फिर tax%, फिर tip%। 
इसे एक बार tax को default रखते हुए और tip=10 keyword argument देकर call करो।
Concepts: *args + keyword-only-style defaults together, percentage maths
Hint: subtotal = sum(prices), then add subtotal * tax / 100 and subtotal * tip / 100.'''

# restate:ek function banao jo total(subtotal+tax+tip) value return kare.

# example: restaurant_bill(30,60,tip = 10)),(restaurant_bill(30,60,tax = 10) >>>> 103.5 , 99.0

# pseudocode:
            # 1.create function restaurant_bill(*prices, tax=5, tip=0)
            # 2.create variable subtotal = sum(prices)
            # 3.create another variable tax_amount = subtotal * tax / 100
            # 4.create another variable tip_amount = subtotal * tip / 100.
            # 5.return  subtotal + tax_amount +tip_amount
            # 6.print function with one or two or three parameter.

# translate:
def restaurant_bill(*prices, tax=5, tip=0):
    subtotal = sum(prices)
    tax_amount = subtotal * tax / 100
    tip_amount = subtotal * tip / 100.

    return  subtotal + tax_amount +tip_amount

print(restaurant_bill(30,60,tip = 10))
print(restaurant_bill(30,60,tax = 10))

# dry run:
103.5
99.0