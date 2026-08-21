'Restate: int(input) mein ek try with ValueError aur ek general exception fallback.'

# example: user = two then got error of ValueError

# pseudocode:
            # 1.write try
            # 2.take input from user as user = int(input("enter any number: "))
            # 3.except ValueError as e: print(f"Error:{e}")
            # 4.except Exception as e: print(f"Error:{e}")

try: 
    user = int(input("enter any number: "))

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error:{e}")

# dry run:
# enter any number: two
# Error: invalid literal for int() with base 10: 'two'