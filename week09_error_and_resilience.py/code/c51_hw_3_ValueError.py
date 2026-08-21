'int(input(...)) main letters daalo aur dekho kaunsa error aata hai.'

# example: a = two and b =7 

#pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter number: ")) and b = int(input("enter number: "))
            # 3.print(a/b)
            # 4.write except ZeroDivisionError as e: print(f"Error:{e}")
            # 5.write except ValueError as e: print(f"Error:{e}")

try: 
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a/b)

except ZeroDivisionError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error:{e}")


# dry run:
# enter number: two 
# Error:invalid literal for int() with base 10: 'two '