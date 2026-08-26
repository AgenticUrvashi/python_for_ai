'Append mode se ek 4th goal add karo, phir dobara poori file padho.'

# restate: appned mode se goal add karo aur print karo 

# example: I am learning python.

# pseudocode:
            # 1.with open('mygoals.txt','a') as f: f.write('\nI am learning python.')
            # 2.with open('mygoals.txt','r') as f: print(f.read())

# translate:
with open('mygoals.txt','a') as f:
    f.write('\nI am learning python.')

with open('mygoals.txt','r') as f:
    print(f.read())


# dry run:
# Hello!
# Hi! how are you?     
# good morning!        
# I am learning python.