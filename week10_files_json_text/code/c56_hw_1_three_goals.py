'ek file mygoals.txt mein 3 goals likho (write mode).'

# restate: 3 goals likho aur print karo mygoals.txt me

# example:# Hello!
        # HI! how are you?
        # good morning!

# pseudocode:
            # 1.with open('mygoals.txt','w') as f: f.write('goal1),f.write(goal2)
                # and f.write(goal3)
            # 2.with open('mygoals.txt','r') as f: print(f.read())

# translate: 
with open('mygoals.txt','w') as f:
    f.write('Hello!')
    f.write('\nHi! how are you?')
    f.write('\ngood morning!')

with open('mygoals.txt','r') as f:
    print(f.read())

# dry run:
# Hello!
# HI! how are you?
# good morning!