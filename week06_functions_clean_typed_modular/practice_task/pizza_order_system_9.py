'''
EN: Write order_pizza(item, qty=1, size="medium"). Show 3 orders: only item; 
item + qty; item + size="large" using a keyword argument.
हिंदी: order_pizza(item, qty=1, size="medium") बनाओ। 3 orders दिखाओ: सिर्फ़ item; 
item + qty; और item + size="large" keyword argument से।
Concepts: multiple defaults, positional vs keyword arguments
Hint: return f"{qty} {size} {item}". Try order_pizza("pizza", size="large").'''

# restate:ek function banao jo order le kisi bhi item ka.jisme do default value ho qty and size.

# example:item = pizza , qty = 3, size = large

# pseudocode:
            # 1.create function order_pizza(item,qty=1,size="medium")
            # 2.return f"{qty} {size} {item}"
            # 3.print the function with one, two or three parameter.

# translate:
def order_pizza(item, qty=1, size="medium"):
        return f"{qty} {size} {item}"

print("---------------------------------")
print(order_pizza("pizza"))
print("--------------------------------")
print(order_pizza("pizza",3))
print("--------------------------------")
print(order_pizza("pizza", size ="large"))
print("---------------------------------")

# dry run:
# 1 medium pizza
# 3 medium pizza
# 1 large pizza