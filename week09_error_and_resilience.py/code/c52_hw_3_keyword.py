'Ek try/except/else/finally ka poora example likho jo chaaron blocks dikhaye.'

# example: a =4 and b =two

# pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter any number: ")) 
            # 3.b = int(input("enter any number: "))
            # 4.print(a/b)
            # 5.write except ZeroDivisionError as e: print(f"Error:{e}")
            # 6.write except ValueError as e: print(Invalid)
            # 7.else: print("successfully exicuted...")
            # 8.finally: print("end of exicution...")

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
else:
    print("successfully exicuted...")

finally:
    print("end of exicution...")

# dry run:
# enter number: 5
# enter number: 7
# 0.7142857142857143      
# successfully exicuted...
# end of exicution...   