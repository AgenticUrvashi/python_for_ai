# restate: jo program humne pehle likhe the unmese 3 program ko function me dalke type hint aur docstrings add karna hai.

# example: marks = 89 then the output = B

# pseudocode:
            # 1.create function get_grade(marks)
            # 2.if marks >= 90 returns A
            # 3.if marks >= 80 returns B
            # 4.if marks >= 70 returns C
            # 5.if marks >= 60 returns D
            # 6.if marks < 60 returns E
            # 7.user se input lo.
            # 8.if choice is list then take empty list and one new input from user as how many students.
            # 9.use for loop and take two input one is name and another is marks then print output.
            # 10.if choice is single then use while loop.
            # 11.take two input from user one is name and another is marks.
            # 12.print the output.
            # 13.take input for continue program if no then break loop.
            # 14.else print invalid input.

print("============================================== Grade ===================================================")

def get_grade(marks=int) -> str :
    if marks >= 90:
        return "A"

        '''
        marks is input 
        condition: 
        when marks is greater than or equals to 90 
        returns:
        grade = A

        '''
            
    elif marks >= 80:
        return "B"
        '''
        marks is input 
        condition: 
        when marks is greater than or equals to 80 
        returns:
        grade = B
        
        '''

    elif marks >= 70:
        return "C"
        '''
        marks is input 
        condition: 
        when marks is greater than or equals to 70 
        returns:
        grade = C
        
        '''

    elif marks >= 60:
        return "D"
        '''
        marks is input 
        condition: 
        when marks is greater than or equals to 60 
        returns:
        grade = D
        
        '''

    else:
        return "E"
        '''
        marks is input 
        condition: 
        when marks is smaller than 60 
        returns:
        grade = E
        
        '''

print("========================================= student grade =================================================")

choice = input("you want to check grade for list or single mode again: ")
print( )

if choice == "list":
    students = {}
    n = int(input("how many students: "))
        
    for i in range(n):
        name = input("enter student name: ")
        marks = int(input("enter marks(0 to 100): "))
        students[name] = marks
        print( )

    for name, marks in students.items():

        print(f"{name}: Grade {get_grade(marks)}")


elif choice == "single":
    while True:

        name = input("enter student name: ")
        marks = int(input("enter students marks(0 to 100): "))

        print( )

        print(f"{name} : Grade {get_grade(marks)}")

        want_to_continue = input("Do you want to continue(y/n): ")
        if want_to_continue == "n":
            break

else:
    print("Invalid input")


print("===============================================================================================================")