'''EN: Create a file my_tools.py with 4 reusable functions, each returning a value: 
celsius_to_f(c), bmi(weight, height), is_prime(n), and word_count(text). 
Test all four and print the results. This is the seed of your own "AI tools" library!
हिंदी: एक file my_tools.py बनाओ जिसमें 4 reusable functions हों, हर एक value return करे: 
celsius_to_f(c), bmi(weight, height), is_prime(n), और word_count(text)। चारों को test करके results print करो। 
यह आपकी अपनी "AI tools" library की शुरुआत है!
Concepts: multiple functions, return, loops/flags inside functions, .split()
Hint: For is_prime, use a flag: assume prime, loop 2..n-1, if any divides evenly set flag False. 
For word_count, return len(text.split()).
'''

# restate: hame hamari pehli library tayar karni hai jisme celsius_to_f(c),bmi(weight, height),is_prime(n),word_count(text).

# example: c= 25 ,w=45, h=1.5, n=7, text=I love python.

# pseudocode:
            # 1.create functions celsius_to_f(c) return (c*9/5)+32
            # 2.bmi(w,h) return w / h ** 2
            # 3.is_prime(n) if n <= 1 return False create flage prime = True use for loop for range(2,n) if n%i==0 prime=False.
            #   break then return prime.
            # 4.word_count(text) then create variable word = text.split() then return len(word)
            # 5.print functions with apropriate arguments.

# translate:
# tools me likhana hai:

def celsius_to_f(c):
    return (c * 9 / 5) + 32

def bmi(weight,height):
    return  weight / (height ** 2)

def is_prime(n):
    if n <= 1:
        return False
    prime = True
    for i in range(2,n):
        if n % i == 0:
            prime = False
            break
    return prime

def word_count(text):
    word = text.split()
    return len(word)

# main.py file me likhana hai:'--------------------------------'

# from code import tools

# print(tools.celsius_to_f(25))
# print(tools.bmi(45, 1.5))
# print(tools.is_prime(7))
# print(tools.word_count("I love Python"))

'--------------------------------------------------------------'

print(celsius_to_f(25))
print(bmi(45, 1.5))
print(is_prime(7))
print(word_count("I love Python"))

# dry run:
77.0
20.0
True
3   