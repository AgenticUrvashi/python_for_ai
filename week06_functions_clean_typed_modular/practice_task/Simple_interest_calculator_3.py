'''
EN: Write a function simple_interest(principal, rate, years) that returns the simple interest (P × R × T) / 100.
 Print interest for ₹10000 at 5% for 3 years.
हिंदी: एक function simple_interest(principal, rate, years) बनाओ जो simple interest (P × R × T) / 100 return करे। 
₹10000 पर 5% की दर से 3 साल का interest print करो।
Concepts: three parameters, return
Hint: return (principal * rate * years) / 100.
'''

# restate:hame ek function banana hai jisme principal, rate aur years ko pass karege 
# aur uske baad simple interest return karega.

# examples: simple_interest(10000,5,3) = 1500.0

# pseudocode:
            # 1.create a function called simple_interest.
            # 2.pass the parameters principal, rate and years to the function.
            # 3.calculate the simple interest using the formula (principal * rate * years) / 100.
            # 4.return the simple interest.

# translate to code:
def simple_interest(principal=int,rate=float,years=int) -> float:
    return (principal * rate * years) / 100

    '''
    this function calculates the simple interest on the given principal, rate and years.
    in this example, the principal is 10000, the rate is 5% and the years are 3.
    the simple interest is 1500.0
    '''

print(simple_interest(10000,5,3))

# dry run:
1500.0