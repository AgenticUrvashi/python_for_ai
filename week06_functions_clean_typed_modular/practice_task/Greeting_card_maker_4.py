'''EN: Write a function make_greeting(name, occasion) that returns a message like "Happy Diwali, Asha!".
 Do NOT print inside the function — return the string and print it outside.
हिंदी: एक function make_greeting(name, occasion) बनाओ जो "Happy Diwali, Asha!" जैसा message return करे।
 Function के अंदर print मत करो — string return करो और बाहर print करो।
Concepts: f-string, return vs print
Hint: return f"Happy {occasion}, {name}!".
'''

# restate:hame ek function me name aur occasion ko pass karke return happy occasion name! karega.

# example: make_greeting("urvashi","holi") = "Happy holi, urvashi!"

# pseudocode:
            # 1.create a function called make_greeting.
            # 2.pass the parameters name and occasion to the function.
            # 3.return the string using f-string.
            # 4.print the string outside the function.

# translate to code:

def make_greeting(name=str,occasion=str) -> str:
    return (f"Happy {occasion} , {name}!")

print(make_greeting("urvashi","holi"))

# dry run:
"Happy holi, urvashi!"

