 
a = 5
b = 0

try:
    result = a / b
    print("Result is:", result)
except Exception :
    print("An error Occurred: Division by zero is not allowed.")

print("End of the execution")

print("-----------------------------------------------------")

a = int(input("enter numerator: "))
b = int(input("enter denominator: "))

try:
    result = a / b
    print("Result is:", result)
except Exception :
    print("An error Occurred: Division by zero is not allowed.")

print("End of the execution")

print("-----------------------------------------------------")

try:
    a = int(input("enter numerator: "))
    b = int(input("enter denominator: "))
    result = a / b
    print("Result is:", result)
except Exception as e:
    print("An error Occurred: Division by zero is not allowed.", e)

print("End of the execution")

print("------------------------------------------------------------------")

print("Resource opened Successfully.")

try:
    a = int(input("enter numerator: "))
    b = int(input("enter denominator: "))
    result = a / b
    print("Result is:", result)
except ZeroDivisionError as zde:
    print("An error occurred : Division by zero is not allowed.", zde)

except ValueError as ve:
    print("An error occurred : Invalid input. Please enter numeric value only.", ve)

except Exception as e:
    print("An unexpeted error occrred: ", e)

finally:
    print("Resource closed")

print("End of the execution")

print("------------------------------------------------------------------")

try:
    a = int(input("enter numerator: "))
    b = int(input("enter denominator: "))
    result = a / b
    print("Result is:", result)

finally:
    print("Cleaning up resorces...")

print("end of execution")


print("------------------------------------------------------------------")

a = 4
b = 2

try:
    print("resourse Open")
    print(a/b)
    u = int(input("enter number: "))
    print(u)

except Exception as e:
    print("cannot divided by zero", e)

finally:
    print("resourse Closed")

print("hey")

print("-----------------------------------------------------------")

a = 4
b = 2

u = int(input("enter number: "))
print(u)


try:
    print("resourse Open")
    print(a/b)
    
except Exception as e:
    print("cannot divided by zero", e)

finally:
    print("resourse Closed")

print("hey")


print("--------------------------------------------------------")

a = 4
b = 2

u = int(input("enter number: "))
print(u)


try:
    print("resourse Open")
    print(a/b)
    
except ZeroDivisionError as e:
    print("cannot divided by zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resourse Closed")

print("hey")

# chatgpt:

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

else:
    print("Result:", result)

finally:
    print("Program finished")


# Kaise kaam karega?

# 1. try → jis code me error aa sakti hai.

# 2. except → agar error aayi, usko handle karega.

# 3. else → sirf tab chalega jab try successfully complete ho.

# 4. finally → har situation me chalega, error aaye ya na aaye.