# restate : Ek function ko keyword arguments se call karke dikhao (order badal kar).

# pseudocode:
            # 1.create new function info having two parameter name and age.
            # 2.print with the help of f-string.
            # 3.call the function as per say in question.info(age= ,name= )

# translate:
def info(name,age):
    print(f"my name is {name},my age is {age}.")

info(age=19,name="ananya")

# final output:
# my name is ananya,my age is 19.