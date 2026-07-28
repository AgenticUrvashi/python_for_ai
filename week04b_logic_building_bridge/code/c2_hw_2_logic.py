print("=========================================================")

print("CLASS 3")

print("========================================================")

# Ek list ke saare numbers ka product (guna) nikalo.

guna = [5,7,2,6,9]
product = 1
for g in guna:
    product = product*g
print(product)

print("=========================================================")

# Ek sentence mein kitne words hain ginno (hint: .split()).

sentence = "i am learing python from indian ai production"
words = sentence.split()
count = 0
for w in words:
    count = count + 1

print(count)

print("========================================================")

# Ek list mein sabse chhota number dhoondho (bina min()).

tom = [34,89,567,76,123,54,22]
smallest = tom[0]
for t in tom:
    if t<smallest:
        smallest = t
print(smallest)

print("==========================================================")

# "hello" ko reverse karke naya string banao (accumulator = "").

word = "hello"
reverse = ""
for i in word:
    reverse = i + reverse
print(reverse)

print("=========================================================")
