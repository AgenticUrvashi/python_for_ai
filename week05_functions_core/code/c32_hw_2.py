# restate : intro(name, age, city="India") banao; ek baar city ke saath, ek baar bina, call karo.

# example:name = "vittal",age = 19,city="pandharpur" then the output is name is vittal,age is 19,city is pandharpur.

# pseudocode:
            # 1.create function intro(name,age,city = "India")
            # 2.print with the f-string.
            # 3.call the function with parameter.

# translate:
def intro(name,age,city="India"):
    print(f"name is {name},age is {age},city is {city}")

intro("shanta",30)
intro("shanta",29,"nagpur")

