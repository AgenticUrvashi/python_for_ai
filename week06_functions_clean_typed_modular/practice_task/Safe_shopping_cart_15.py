'''EN: Write add_item(item, cart=None) correctly so that each fresh call (without a cart) starts with an EMPTY cart. \
Call it 3 separate times and show each returns only its own item. (Do NOT use cart=[] — explain in a comment why.)
हिंदी: add_item(item, cart=None) सही तरीके से बनाओ ताकि हर नई call (बिना cart के) खाली cart से शुरू हो।
 इसे 3 अलग बार call करके दिखाओ कि हर बार सिर्फ़ अपना item आता है। (cart=[] मत इस्तेमाल करो — comment में कारण लिखो।)
Concepts: mutable default trap, None sentinel, is None
Hint: if cart is None: cart = [] — this makes a fresh list every call.'''

# restate:ek function banao jo har el item ke liye nayi list banaie.

# example:print(add_item("Asha"))  >>>>> ['Asha']

# psedocode:
            # 1.create function add_item(item, cart=None).
            # 2.if cart is none then cart = [].
            # 3.add items by append operation.
            # 4.return cart.
            # 5.print function with one parameter.

# translate:
def add_item(item, cart=None):
    if cart == None:                 ### cart = [] — this makes a fresh list every call.
        cart = []
        cart.append(item)
        return cart

print("===========RESULT:=============")

print(add_item("Asha"))
print(add_item("Ananya"))
print(add_item("dog"))

print("-------------------------------")

# dry run:
# ['Asha']
# ['Ananya']
# ['dog']