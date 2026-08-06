'''EN: Write three functions: c_to_f(c), f_to_c(f), c_to_k(c). Run a while menu asking which conversion the user wants, 
take the value, call the right function, and print the result. Loop until the user chooses Exit.
हिंदी: तीन functions बनाओ: c_to_f(c), f_to_c(f), c_to_k(c)। एक while menu चलाओ जो पूछे कौन-सा conversion चाहिए, value लो, 
सही function call करो, और result print करो। Exit चुनने तक loop चलाओ।
Concepts: several functions, menu dispatch, float(input()), loop
Hint: f_to_c = (f - 32) * 5 / 9; c_to_k = c + 273.15.'''

# restate: hame isa program banana hai jo temperature ko user ke kahene anusar convert karke de.

# example: in celsius the temp is 100 then in kelvin 373.15.

# pseudocode:
            # 1.create functions c_to_f(c), f_to_c(f), c_to_k(c).
            # 2.use while loop until its True.
            # 3.print menu then print options like Celsius to Fahrenheit,Fahrenheit to Celsius, Celsius to Kelvin,Exit
            # 4.take user's choice.
            # 5.if 1 then take user's temperature in c and print the function c_to_f(c).
            # 6.if 2 then take user's temperature in f and print the function f_to_c(f).
            # 7.if 3 then take user's temperature in c and print the function c_to_k(c).
            # 8.if 4 then print thank you and break
            # 9.else print invalid input.

# translate:
def c_to_f(c):
    return (c * 9 / 5) + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_k(c):
    return  c + 273.15

print("=========================== Temperature Conversion Tool ==============================")

while True:

    print("===== MENU ======")
    print(" 1) Celsius to Fahrenheit ")
    print(" 2) Fahrenheit to Celsius ")
    print(" 3) Celsius to Kelvin ")
    print(" 4) Exit")

    user_choice = int(input("enter your choice: "))

    if user_choice == 1:
        user_input = float(input("enter temperature in Celsius: "))
        print(c_to_f(user_input))

    elif user_choice == 2:
        user_input = float(input("enter temperature in Fahrenheit: "))
        print(f_to_c(user_input))

    elif user_choice == 3:
        user_input = float(input("enter temperature in Celsius: "))
        print(c_to_k(user_input))

    elif user_choice == 4:
        print("** THANK YOU **")
        break

    else:
        print("invalid input")

print("==================================== END =========================================")

# dry run:

# user_choice = 3
# user_input = 100
# 373.15 