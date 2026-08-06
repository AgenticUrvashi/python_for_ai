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


function_list = ["add","sub","mul","div","flore div","mod"]


'---------------------------------Q1------------------------------------'

import math

def is_palindrome(text: str) -> bool:

    """Check if a text reads the same forwards and backwards."""

    return text == text[::-1]

'---------------------------------Q3---------------------------------------'

def circle_area(radius: float) -> float:

    """Return the area of a circle given its radius."""

    return math.pi * radius ** 2


'------------------------------------ Q.20---------------------------------------'


def celsius_to_f(c):
    return (c * 9 / 5) + 32

def bmi(weight,height):
    return  weight / (height ** 2)

def is_prime(n):
    if n <= 1:
        return False
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return prime

def word_count(text):
    word = text.split()
    return len(word)

'-----------------------------------------------------------------------------'

if __name__ == "__main__":

    print("Testing add function: ")
    add_result = add(3,5)
    print("addition result: ", add_result)
    sub_result = subtract(3,5)
    print("subtraction result: ", sub_result)
    print("Testing mul function: ")
    mul_result = multiply(3,5)
    print("multiplication result: ", mul_result)
    print("Testing div function: ")
    div_result = divide(3,5)
    print("Division result: ", div_result)
    print("Testing flore_div function: ")
    flore_div = flore_division(3,5)
    print("flore division result: ",flore_div)
    print("Testing mod function: ")
    mod_result = remender(3,5)
    print("modulus result: ", mod_result)