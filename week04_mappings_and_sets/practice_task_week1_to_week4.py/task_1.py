#Task 1 — Personal Profile Card
#User se name, age, city, aur favourite_subject maango (input()). Phir ek saaf profile card f-string se print karo.

#Concepts: variables, input(), int(), f-strings
#Hint: age ko int(input(...)) se lo taaki age + 1 chal sake.
#ans:

print("==================profile_card====================")

name = input("enter your name: ")
print("---------------------------------------------------")
age = int(input("enter your age: "))
print("----------------------------------------------------")
city = input("enter your city name: ")
print("---------------------------------------------------")
fav_sub = input("enter your favourite subject: ")

print("---------------------------------------------------")

print(f'''My Name is {name}.

My age is {age}.

I am live in {city}.

My favourite suject is {fav_sub}.''')

print("====================end============================")