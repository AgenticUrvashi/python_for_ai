# Q34
# EN: A sentence is given. Build a dict of word → count.
# Given: sentence = "the cat sat the cat"

# restate:Ek sentence diya hai. word → count ki dict banao.

# example:sentence = "the cat sat the cat" for loop se if condition check karke hamara output = {'the':2,'cat':2,'sat':1}

# pseudocode:
            # 1.create variable sentence = "the cat sat the cat"
            # 2.create new variable words = sentence.split()
            # 3.create empty dict having name freq.
            # 4.use for loop for words list.
            # 5.if i is in freq then upadate the count of word i.
            # 6.else freq[i] = 1
            # 7.print the freq.

# translate:
sentence = "the cat sat the cat"
words = sentence.split()
freq = {}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)

# dry run: 
# step | word | freq |
#   1  | the  |{'the':1}
#   2  | cat  |{'the':1,'cat':1}
#   3  | sat  |{'the':1,'cat':1,'sat':1}
#   4  | the  |{'the':2,'cat':1,'sat':1}
#   5  | cat  |{'the':2,'cat':2,'sat':1}