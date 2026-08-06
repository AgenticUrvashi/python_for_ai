'''EN: Write cart_total(*prices) that returns the sum of any number of item prices. Test it with 3 prices and with 6 prices.
हिंदी: cart_total(*prices) बनाओ जो कितने भी item prices का जोड़ return करे। इसे 3 prices और 6 prices के साथ test करो।
Concepts: *args, sum()
Hint: return sum(prices). Inside, prices is a tuple.'''

# restate:ek function banao jo total price nikale.

# example:*prices = (45,78,90,104,678,88)  then the output is 1083

# psudocode:
            # 1.create function cart_total(*prices)
            # 2.return sum(prices)
            # 3.print the function with f-string.

# translate:

def cart_total(*prices):
    return sum(prices)
print("------------------------------")

print(f"your total bill is : {cart_total(45,78,90,104,678,88)}")

print("------------------------------")

# dry run:
1083