# restate: 'Har error ke liye ek line likho:"yeh error kab aata hai?"'

# example: number = [1,4,56,7,8,9] when user give 8 then they show error of IndexError

# pseudocode:
            # 1.write try keyword 
            # 2.a = int(input("enter number: ")) and b = int(input("enter number: "))
            # 3.print(a/b)
            # 4.write except ZeroDivisionError as e: print(f"Error:{e}")
            # 5.print("when b is zero")
            # 6.write except ValueError as e: print(f"Error:{e}")
            # 7.print("when user give any string")
            # 8.write try then number = [1,4,56,7,8,9] then ind = int(input("enter index: ")) 
            # 9.print(number[ind])
            # 10.write except IndexError as e: print(f"Error:{e}")
            # 11.print("when index is not available in given collection")
            # 12.write except ValueError as e: print(f"Error:{e}")
            # 13.print("when user give any string")


try: 
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a/b)

except ZeroDivisionError as e:
    print(f"Error: {e}")
    print("when b is zero")

except ValueError as e:
    print(f"Error:{e}")
    print("when user give any string")

try:
    number = [1,4,56,7,8,9]
    ind = int(input("enter index: "))
    print(number[ind])

except IndexError as e:
    print(f"Error:{e}")
    print("when index is not available in given collection")

except ValueError as e:
    print(f"Error:{e}")
    print("when user give any string")

