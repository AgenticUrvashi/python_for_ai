'Restate: safe division: do numbers lo, divide karo, ZeroDivisionError handle karo'

# example: a =4 and b =0

# pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter any number: ")) 
            # 3.b = int(input("enter any number: "))
            # 4.print(a/b)
            # 5.write except ZeroDivisionError as e: print(f"Error:{e}")


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

# dry run:
# enter number: 4
# enter number: 0
# Error: division by zero