'Restate: ek @uppercase decorator banao jo function ke string-result ko uppercase kare.'

# example: text = janvi

# pseudocode:
            # 1.create decorator uppercase(func): then create another function wrapper(text):
            # 2.upper = text.upper() then result = func(upper) then print(result)
            # 3.return wrapper
            # 4.write decorator @uppercase
            # 5.create another function string(text): return text
            # 6.call the function string("janvi")

def uppercase(func):
    def wrapper(text):
        upper = text.upper()
        result = func(upper)
        print(result)
    return wrapper

@uppercase
def string(text):
    return text

string("janvi")

# dry run:
# JANVI