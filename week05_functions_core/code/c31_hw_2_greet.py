# restate: ek function greet(name,city) jo "HI NAME from CITY" return kare (print nahi, return).

# example:name = "shahu", city = "indor" then the output is "HI shahu from indor"

#pseudocode:
#           1.create a function greet(name,city)
#           2.create new varible GREET = (f"HI {name} from {city}.")
#           3.return the GREET.
#           4.print the function.

# translate:
def greet(name,city):
    GREET = f"HI {name} from {city}."
    return GREET

print(greet("shahu","indor"))

# dry run:
# step | name | city | output |
#   1  |shahu |indor |   -    |
#   2  |shahu |indor |HI shahu from indor. 

# final output:
# HI shahu from indor.