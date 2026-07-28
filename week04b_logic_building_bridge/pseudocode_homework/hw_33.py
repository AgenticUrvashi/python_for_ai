# Q33
# EN: A word is given. Build a dict counting each character's frequency.
# Given: word = "banana"   →  {'b': 1, 'a': 3, 'n': 2}

# restate:Ek word diya hai. Har character ki frequency ki dict banao.

# example:word = "baadshah" for loop se one by one if ki condition check karke frequency print hogi.
#                  the output is {'b': 1, 'a': 3, 'n': 2}



# translate:
word = "banana"
frequency = {}
for i in word:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i] = 1

print(frequency)

# dry run
# step | i | frequency 
#   1  | b | {'b':1}
#   2  | a | {'b':1,'a':1}
#   3  | n | {'b':1,'a':1,'n':1}
#   4  | a | {'b':1,'a':2,'n':1}
#   5  | n | {'b':1,'a':2,'n':2}
#   6  | a | {'b':1,'a':3,'n':2}

# final output:
# {'b':1,'a':3,'n':2}