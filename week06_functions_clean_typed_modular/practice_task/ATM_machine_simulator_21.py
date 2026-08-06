'''EN: Build an ATM with functions check_balance(balance), deposit(balance, amount), and withdraw(balance, amount) 
(block overdraft with a message). Run a while menu: 1) Balance 2) Deposit 3) Withdraw 4) Exit. Keep updating the balance 
from the returned values.
हिंदी: एक ATM बनाओ जिसमें functions हों check_balance(balance), deposit(balance, amount), और withdraw(balance, amount) 
(पैसे कम हों तो message देकर रोको)। एक while menu चलाओ: 1) Balance 2) Deposit 3) Withdraw 4) Exit. हर बार return की गई 
value से balance update करते रहो।
Concepts: multiple functions, return, while menu, if/elif/else
Hint: In withdraw, if amount > balance: return balance (unchanged) with a warning; else return balance - amount.'''


# restate: ATM system ki tarah code banao jo balance show kare, amount deposite kare, withdraw kare aur upadated balance dikhai.

# example: 1st input is 2 then second is 300 then the total is 1300.

# pseudocode:
            # 1.create 3 functions for checking balance, deposit amount and withdraw balance.
            # 2.create variable balance = 1000.
            # 3.use while loop.
            # 4.print ATM menu with the help of print.
            # 5.take user's input for choicing from menu.
            # 6.if choice is 1 then print check balance function.
            # 7.if choice is 2 then print deposit function.
            # 8.if choice is 3 then print withdraw function.
            # 9.if choice is 4 then print brake.
            # 10.else print invalid input.

# translate:
def check_balance(balance):
    return f" Current balance : {balance}"

def deposit(balance,amount):
    return balance + amount

def withdraw(balance,amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient balance")
        return balance
        

balance = 1000

while True:
    print("====================================ATM menu====================================")

    print("1) check balance")
    print("2) deposit")
    print("3) withdraw")
    print("4) Exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        print(check_balance(balance))

    elif choice == 2:
        amount_for_deposit = float(input("enter your amount of deposit: "))
        balance = deposit(balance,amount_for_deposit)
        print(balance)

    elif choice == 3:
        amount_for_withdraw = float(input("enter your amount of withdraw: "))
        balance = withdraw(balance,amount_for_withdraw)
        print(balance)

    elif choice == 4:
        print("Thank You for using ATM")
        break
    
    else:
        print("Invalid choice!")

print("======================================= End ==================================")

# dry run:
# ====================================ATM menu====================================
# 1) check balance   
# 2) deposit
# 3) withdraw        
# 4) Exit
# enter your choice: 2
# enter your amount of deposit: 300
# 1300.0