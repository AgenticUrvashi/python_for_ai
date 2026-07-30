#que: add_to_list likho jo default None use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.

# restate:default list ka bug fix karke dikhao.

# example:text = jamoon,moon,vidya 

# pseudocode:
            # 1.create an function having name add_to_list(text,list=None)
            # 2.if list == None then list = []
            # 3.add text with the help of append:list.append(text).
            # 4.return list.
            # 5.print function with argument in string.

# Translate:

def add_to_list(text,list=None):
    if list == None:
        list = []
    list.append(text)
    return list

print(add_to_list("jamoon"))
print(add_to_list("moon"))
print(add_to_list("vidya"))

# dry run:
['jamoon']
['moon']
['vidya']