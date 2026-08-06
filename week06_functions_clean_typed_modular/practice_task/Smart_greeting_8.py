'''EN: Write greet(name, greeting="Hello") where greeting has a default. 
Call it once with only a name, and once with a custom greeting like "Namaste".
हिंदी: greet(name, greeting="Hello") बनाओ जिसमें greeting का default हो। 
इसे एक बार सिर्फ़ name के साथ, और एक बार custom greeting जैसे "Namaste" के साथ call करो।
Concepts: default parameter value
Hint: return f"{greeting}, {name}!". Calling greet("Asha") uses the default.'''

# restate:ek function banao jo name leke greet kare aur greeting ko default me "hello" rakho.

# example:name : Urvashi >>>> Hello, Urvashi!    name = Urvashi,greeting = Namaste >>>> Namaste, Uravshi!

# pseudocode:
            # 1.create function greet(name,greeting="Hello")
            # 2.return f"{greeting}, {name}!"
            # 3.print function with one or two parameter.

# translate:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("-------------------")
print(greet("Urvashi"))
print("-------------------")
print(greet("Urvashi","Namaste"))
print("-------------------")

# dry run:
# Hello, Urvashi!
# Namaste, Uravshi!