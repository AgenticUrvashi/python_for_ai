# restate: jo program humne pehle likhe the unmese 3 program ko function me dalke type hint aur docstrings add karna hai.

# example: fara = 77 then output is c= 25.0

# pseudocode:
            # 1.create function fahrenheit_to_celsius(fahrenheit)
            # 2.returns (fahrenheit - 32) * 5 / 9
            # 3.print the function with parameter

def fahrenheit_to_celsius(fahrenheit=float) -> float:
  return (fahrenheit - 32) * 5 / 9
  '''
  this function is use for converting fahrenheit tempreture to celsius.
  returns:
  in celsius tempreture.

  '''

print("============================= converter ==============================")

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# dry run:
25
35
10