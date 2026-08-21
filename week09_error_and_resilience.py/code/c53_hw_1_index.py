'Ek program jo list se index access kare, ValueError aur IndexError dono alag handle karo.'

# example: index = 9 then finds error

# pseudocode:
            # 1.write try then numbers = [2,7,8,4,6,0,1]
            # 2.index = int(input("enter index: ")) then print(numbers[index])
            # 3.except ValueError as e: print(f"Error:{e}")
            # 4.except IndexError as e: print(f"Error:{e}")

try:
    numbers = [2,7,8,4,6,0,1]
    index = int(input("enter index: "))
    print(numbers[index])

except ValueError as e:
    print(f"Error:{e}")

except IndexError as e:
    print(f"Error:{e}")

# dry run:
# enter index: 9
# Error:list index out of range
