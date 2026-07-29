# restate : greet_all(*names) jo har naam ko "Hello NAME" print kare (loop se).

# example :names =rekha,ganga,janu then the output is HELLO REKHA,HELLO GANGA,HELLO JANU.

# pesudocode:
            # 1.create new function greet_all(*names).
            # 2.use for loop for names:for i in names
            # 3.convert i in uppercase.i = i.upper()
            # 4.print hello name with the help of f-string.print(f"hello,{i}")
            # 5.call the function with parameter.

# translate:
def greet_all(*names):
    for i in names:
        i = i.upper()
        print(f"HELLO,{i}") 

greet_all("shanta","shobha","chhya")

# final output:

# HELLO SHANTA
# HELLO SHOBHA
# HELLO CHHAYA
