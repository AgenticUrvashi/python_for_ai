'''
EN: Write a function celsius_to_f(c) that converts Celsius to Fahrenheit and returns the value.
 Test it with 0, 37, and 100 degrees.
हिंदी: एक function celsius_to_f(c) बनाओ जो Celsius को Fahrenheit में बदल कर value return करे। 
इसे 0, 37 और 100 डिग्री पर test करो।
Concepts: def, arithmetic, return
Hint: Formula: (c * 9 / 5) + 32.
'''

# restate:ek function celsius to f(c) banakar hame celsius ka temp fara me batana hai.

# example : c = 0,37,100

# pseudocode:
            # 1.create function celsius_to_f(c).
            # 2.create new variable convert = (c * 9 / 5) + 32.
            # 3.return convert
            # 4.print function with parameter.

# translate:
def celsius_to_f(c=float) -> float:
    convert =(c * 9 / 5) + 32
    return convert

print(celsius_to_f(0))
print(celsius_to_f(37))
print(celsius_to_f(100))

# dry run:
32.0
98.6
212.0