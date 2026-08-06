'''EN: Write a function final_price(price, discount_percent) that returns the price after discount. 
Print the final price of a ₹1500 item with 20% off.
हिंदी: एक function final_price(price, discount_percent) बनाओ जो discount के बाद की कीमत return करे। 
₹1500 के item पर 20% छूट के बाद final price print करो।
Concepts: return, percentage maths
Hint: return price - (price * discount_percent / 100).'''

# restate: ek function banao jo discount ka price katkar baki bachi price print kare.

# example:total = 1500  percent = 20 then the output is 1200.

# pseudocode:
            # 1.create function final_price(price,discount_percent).
            # 2.return price - (price * discount_percent / 100).
            # 3.print the function with two parameter.

# translate:
def final_price(price=int,discount_percent=int) -> float :
    return price - (price * discount_percent / 100)

print(final_price(1500,20))

# dry run:
1200