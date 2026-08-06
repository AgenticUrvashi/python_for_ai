'''
EN: Refactor a calculator into functions: add, subtract, multiply, divide (handle divide-by-zero by returning a message). 
Then write calculate(a, b, op) that calls the right one based on op ("+", "-", "*", "/").
हिंदी: Calculator को functions में बाँटो: add, subtract, multiply, divide (divide-by-zero पर message return करो)। 
फिर calculate(a, b, op) बनाओ जो op ("+", "-", "*", "/") के हिसाब से सही function call करे।
Concepts: many functions, dispatch with if/elif or match, return
Hint: In divide, if b == 0: return "Cannot divide by zero".'''

# restate: 4 alag alag function banao, jo +,-,*,/ . jo methods return kare.

# example: add(4,7)

# pseudocode:
            # 1.create 4 functions add,sub,mult,div.
            # 2.return perform methods.
            # 3.print the functions.

# translate:
def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):
    if b == 0:
        print("can not divided by zero")

    return a / b

print(add(2, 6))
print(subtract(6, 2))
print(multiply(6, 2))
print(divide(6, 2))

# dry run:
8
4  
12 
3.0