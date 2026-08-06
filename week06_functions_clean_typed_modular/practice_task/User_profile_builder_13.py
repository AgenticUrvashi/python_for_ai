'''EN: Write show_profile(**details) that prints each detail as key: value. Call it with name, age, and city.
हिंदी: show_profile(**details) बनाओ जो हर detail को key: value की तरह print करे। इसे name, age, और city के साथ call करो।
Concepts: **kwargs, dict .items(), loop
Hint: for key, value in details.items(): print(f"{key}: {value}").'''

# resstate:ek function banao jo user ki profile banaie.

# example:show_profile(name = "Asha", age = 16, city = "Indore").

# pseudocode:
            # 1.create function show_profile(**details)
            # 2.use for loop for dict.
            # 3.print key value with the help of f-string.
            # 4.call the function with keyword arguments.

# translate:
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print("-------------------")
print("======profile======")
print("-------------------")
show_profile(name = "Asha", age = 16, city = "Indore")
print("-------------------")
print("======profile======")
print("-------------------")
show_profile(first_name = "Ananya", last_name = "Joshi", passion = "Actor", hobbies = "dancing", monthly_income = 500000)
print("-------------------")

# dry run:

# name: Asha
# age: 16
# city: Indore
# -------------------
# first_name: Ananya
# last_name: Joshi
# passion: Actor
# hobbies: dancing
# monthly_income: 500000
# -------------------
