'que01: jaan-boojh kar 3 alag error banao (ZeroDivisionError,ValueError,IndexError) aur traceback padho.'

# restate: hame 3 alag alag error banane hai.

# example : a = 4 and b = 0,two 

# pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter number: ")) and b = int(input("enter number: "))
            # 3.print(a/b)
            # 4.write except ZeroDivisionError as e: print(f"Error:{e}")
            # 5.write except ValueError as e: print(f"Error:{e}")
            # 6.write try then number = [1,4,56,7,8,9] then ind = int(input("enter index: ")) print(number[ind])
            # 7.write except IndexError as e: print(f"Error:{e}")
            # 8.write except ValueError as e: print(f"Error:{e}")


try: 
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a/b)

except ZeroDivisionError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error:{e}")

try:
    number = [1,4,56,7,8,9]
    ind = int(input("enter index: "))
    print(number[ind])

except IndexError as e:
    print(f"Error:{e}")

except ValueError as e:
    print(f"Error:{e}")

# dry run:
# enter number: 5
# enter number: 0
# Error: division by zero
# enter index: two
# Error:invalid literal for int() with base 10: 'two'