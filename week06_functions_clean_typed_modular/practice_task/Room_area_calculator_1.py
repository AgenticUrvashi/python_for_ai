'''
EN: Write a function room_area(length, width) that returns the area of a room. 
Use it to find the area of 3 different rooms and print each result.
हिंदी: एक function room_area(length, width) बनाओ जो कमरे का area return करे। 
इसे 3 अलग-अलग कमरों का area निकालने के लिए इस्तेमाल करो और हर result print करो।
Concepts: def, two parameters, return, function call
Hint: return length * width. Print the call: print(room_area(10, 12)).
'''

# restate: ek function banao jo room ka area nikale jab hum length or width de.

# example: room_area(10, 12)

# peusocode:
            # 1.create a function room_area(length,width)
            # 2.create new variable area and store data length * width
            # 3.return area.
            # 4.print function with two parameter.

# translate:
def room_area(length=float , width=float) -> float :
    area = length * width
    return area

print(room_area(10 , 12))

# dry run:
120