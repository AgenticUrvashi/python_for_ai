'''EN: Write average(*marks) that returns the average of any number of marks. 
If called with no marks, return 0 (avoid divide-by-zero).
हिंदी: average(*marks) बनाओ जो कितने भी marks का average return करे। 
अगर बिना marks के call हो तो 0 return करो (divide-by-zero से बचो)।
Concepts: *args, len(), guard condition
Hint: if len(marks) == 0: return 0 first, then return sum(marks) / len(marks).'''

# restate: ek function banao jo average print kare.

# example: marks = (23,67,65,34,98,40)

# pseudocode:
            # 1.create function average(*marks).
            # 2. if length of marks is equals to 0 then returns 0.
            # 3. returns sum of all marks / length of marks.
            # 4.print average with parameters.

# translate:
def average(*marks):
    if len(marks) == 0:
        return 0 
    return sum(marks) / len(marks)

print(average(23,67,65,34,98,40))

# dry run:
54.5