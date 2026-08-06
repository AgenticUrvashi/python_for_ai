'''EN: Write a function tip_amount(bill, percent) that returns how much tip to pay. 
Then print the total bill (bill + tip) for a ₹800 bill at 10%.
हिंदी: एक function tip_amount(bill, percent) बनाओ जो tip की रकम return करे। 
फिर ₹800 के bill पर 10% tip के साथ कुल bill (bill + tip) print करो।
Concepts: return, using the returned value in more maths
Hint: return bill * percent / 100, then total = bill + tip_amount(800, 10).

'''

# restate:ek function banao jo tip amount return kare.

# example: tip_amount(800, 10) = 80.00, total bill = 880.00

# pseudocode:
# 1.create a function called tip_amount.
# 2.pass the parameters bill and percent to the function.
# 3.return the tip amount.
# 4.create new variable total = 800 + tip_amount(800,10)
# 5.print the total value and tip amount with f-string.

# translate to code:
def tip_amount(bill=int,percent=float) -> float:
    return bill * percent / 100

total = 800 + tip_amount(800,10)

print("---------------------------------------------------------------------------")
print(f"the tip price is: {tip_amount(800,10)}, and the total cost is :{total}")
print("---------------------------------------------------------------------------")

# dry run:
# tip_amount = 80.0
# total = 880.00