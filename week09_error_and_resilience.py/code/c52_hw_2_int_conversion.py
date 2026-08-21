'restate: Safe int conversion: user input ko int banao, ValueError handle karke "Invalid" bolo.'

# example: a =4 and b =two

# pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter any number: ")) 
            # 3.b = int(input("enter any number: "))
            # 4.print(a/b)
            # 5.write except ZeroDivisionError as e: print(f"Error:{e}")
            # 6.write except ValueError as e: print(Invalid)

try: 
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a/b)

except ZeroDivisionError as e:
    print(f"Error: {e}")
    '''
    ZeroDivisionError:
        handle error create from b = 0
    e:
        msg from error
    '''

except ValueError as e:
    print("Invalid")
    '''
    ValueError:
        handle error create from a or b = str(...)
    '''

# dry run:
# enter number: 4
# enter number: two
# Invalid