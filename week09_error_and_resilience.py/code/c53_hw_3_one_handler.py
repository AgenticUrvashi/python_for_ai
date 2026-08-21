'Do error (ValueError,ZeroDivisionError) ko ek hi handler se pakdo.'

# example: a = 2 and b = two

# pseudocode:
            # 1.write try
            # 2.a = int(input("enter any number: "))
            # 3.b = int(input("enter any number: "))
            # 4.write print(a/b)
            # 5.except (ValueError,ZeroDivisionError) as e: print(f"Error:{e}")


try: 
    a = int(input("enter any number: "))
    b = int(input("enter any number: "))
    print(a/b)

except (ValueError,ZeroDivisionError) as e:
    print(f"Error: {e}")


# dry run:
# enter any number: 2
# enter any number: two
# Error: invalid literal for int() with base 10: 'two'