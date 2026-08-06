# que : apna my_tools.py (week 5) ke 3 functions mein type hints + google-style docstrings add karo.

# restate: jo program humne pehle likhe the unmese 3 program ko function me dalke type hint
#  aur docstrings add karna hai.

# example: a = 4 , b = 2,operator = / then the output is 2.

# pseudocode:
            # 1.create functions add returns a + b
            # 2.create another function subtract returns a - b
            # 3.create another function multiply returns a * b
            # 4.create another function divide returns a / b
            # 5.create another function flore_division returns a // b
            # 6.create another function remender returns a % b
            # 7.use while loop.
            # 8.enter users input 3 times 1st is a 2nd is b 3rd is operator.
            # 9.if operator is + then a + b
            # 10.if operator is - then a - b
            # 11.if operator is * then a * b
            # 12.if operator is / then a / b
            # 13.if operator is // then a // b
            # 14.if operator is % then a % b
            # 15.else print invalid input 
            # 16.take user's input "do you want to continue" 
            # 17.if n then breake while loop

# translate:

def add(a=float, b=float) -> float :

    return a + b

    '''
    add function is used for adding a and b

    '''

def subtract(a=float, b=float) -> float :

    return a - b

    '''
    substract is used for substracting a and b

    '''

def multiply(a=float, b=float) -> float :

    return a * b

    '''
    multiply is used for multipying a and b

    '''

def divide(a=float, b=float) -> float :
    if b == 0:
        print("can not divided by zero")

    return a / b

    '''

    divide is used for division in a and b
    
    condition:
    when b = 0 then input cannot accept

    '''


def flore_division(a=float, b=float) -> float :
    if b == 0:
        print("can not divided by zero")

    return a // b

    '''

    flore_division is used for dividing float numbers.
    
    condition:
    when b is 0 then the ans is infinity so b=0 input cannot accept.

    '''


def remender(a=float, b=float) -> float:

    return a % b

    '''

    remender is used for finding remender and in even/odd problems or any more.
    this function finds the remender of a / b.

    '''

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

print("======================================= end ======================================")
