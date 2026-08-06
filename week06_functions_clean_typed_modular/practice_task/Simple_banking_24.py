'''EN: Use a dict accounts = {"Asha": 5000, "Rahul": 3000}. 
Write deposit(accounts, name, amount) and withdraw(accounts, name, amount) that update and return the dict 
(check the account exists and enough balance). Run a menu to operate on any account and always show the updated balances.
हिंदी: एक dict accounts = {"Asha": 5000, "Rahul": 3000} इस्तेमाल करो। 
deposit(accounts, name, amount) और withdraw(accounts, name, amount) बनाओ जो dict को update करके return करें 
(account मौजूद है और balance काफ़ी है — check करो)। किसी भी account पर काम करने के लिए menu चलाओ और हमेशा updated balances दिखाओ।
Concepts: dict as shared state, functions modifying and returning a dict, validation
Hint: if name not in accounts: return accounts with a message; guard amount > accounts[name] in withdraw.'''

# restate: hame is program me simple banking structure banana hai jo user ke kehne pr kam kare.

# example:when user choose 3 then {'Asha': 5000, 'Rahul': 3000}

# pseudocode:
            # 1.starts with given dict.
            # 2.create functions deposite(accounts,name,amount) if name not in accounts then return else accounts[name]+=account
            #   return accounts.
            # 3.withdraw(accounts,name,amount) if name not in accounts then return if amount>accounts[name]:return insufficient 
                # balance  else: accounts[name] -= amount return accounts.
            # 4.use while loop until it's true.
            # 5.print menu with options.
            # 6.take user's input for choice.
            # 7.if 1 then take two input one is name & other is amount print function.
            # 8.if 2 then take two input one is name & other is amount print function.
            # 9.if 3 then print accounts.
            # 10.if 4 then break
            # 11.if 5 then print invalid input.

accounts = {
    "Asha": 5000, 
    "Rahul": 3000
    }

def deposit(accounts,name,amount):
    if name not in accounts:
        return
    else:
        accounts[name] += amount
        return accounts

def withdraw(accounts,name,amount):
    if name not in accounts:
        return
    if amount > accounts[name]:
        return "Insufficient balance"
    else:
        accounts[name] -= amount
        return accounts

while True:
    print("====== menu ======")
    print("1)deposite")
    print("2)withdraw")
    print("3)show balance")
    print("4)exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        amount_for_deposit = int(input("enter amount for deposit: "))
        name_for_account = input("enter your name: ")
        
        print(deposit(accounts, name_for_account, amount_for_deposit))

    elif choice == 2:
        amount_for_withdraw = int(input("enter amount for withdraw: "))
        name_for_accounts = input("enter your name: ")
        
        print(withdraw(accounts, name_for_accounts, amount_for_withdraw))

    elif choice == 3:
        print(accounts)

    elif choice == 4:
        break

    else:
        print("Invalid input")

print("==================================== END ====================================")

# dry run:
# menu 
# 1)deposite
# 2)withdraw
# 3)show balance     
# 4)exit
# enter your choice: 3
# {'Asha': 5000, 'Rahul': 3000}
