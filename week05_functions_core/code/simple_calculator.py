
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

def flore_division(a, b):
    if b == 0:
        print("can not divided by zero")

    return a // b

def remender(a, b):

    return a % b

print("=============================== simple calculator =================================")

while True:

    user_input1 = int(input("enter any number for calculation: "))
    user_input2 = int(input("enter any number for calculation: "))
    user_input3 = input("enter any operation(+,-,*,/,//,%): ")

    if user_input3 == "+":
        print(add(user_input1 , user_input2))

    elif user_input3 == "-":
        print(subtract(user_input1 , user_input2))
    elif user_input3 == "*":
        print(multiply(user_input1 , user_input2))
    elif user_input3 == "/":
        print(divide(user_input1 , user_input2))
    elif user_input3 == "//":
        print(flore_division(user_input1 , user_input2))
    elif user_input3 == "%":
        print(remender(user_input1 , user_input2))
    else:
        print("Invalid opertaor")

    user_input4 = input("Do you want to continue(yes or no): ")
    if user_input4 == "no":
        break

print("=========================================== end ======================================")
