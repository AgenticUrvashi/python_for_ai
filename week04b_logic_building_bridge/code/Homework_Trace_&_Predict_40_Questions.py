# Q1
# EN: Trace x step by step. What prints?
# HI: x ko step-by-step trace karo. Kya print hoga?
x = 5
x = x + 3
x = x * 2
print(x)


# Q2
# EN: Predict the final total. 
# HI: Aakhri total predict karo.

total = 0

for n in [1, 2, 3, 4]:

    total = total + n

print(total)


# Q3
# EN: Trace x through each turn. 
# HI: Har chakkar mein x trace karo.

x = 20

for i in range(4):

    x = x - 5

print(x)


# Q4
# EN: What do // and % give? 
# HI: // aur % kya denge?

a = 17

b = 5

print(a // b, a % b)


# Q5
# EN: How many times does the loop run?
#  HI: Loop kitni baar chalta hai?

count = 0

for letter in "python":

    count = count + 1

print(count)


# Q6
# EN: Trace result (multiplication).
#  HI: result trace karo (guna).

result = 1

for n in [2, 2, 3]:

    result = result * n

print(result)


# Q7
# EN: What do these three prints show? 
# HI: Yeh teen prints kya dikhayenge?

s = "python"

print(s[0], s[-1], s[1:4])


# Q8
# EN: Trace the string word being built.
#  HI: word string banti hui trace karo.

word = ""

for c in "abc":

    word = word + c + "-"

print(word)


# Q9
# EN: Trace x (division makes a float). 
# HI: x trace karo (division float banata hai).

x = 10

x = x / 2

x = x / 2

print(x)


# Q10
# EN: Sum of range(2, 6). Careful with the last number. 
# HI: range(2, 6) ka sum. Aakhri number par dhyaan.

total = 0

for i in range(2, 6):

    total = total + i

print(total)

# Q11
# EN: How many even numbers are counted?
#  HI: Kitne even numbers gine gaye?

count = 0

for n in [1, 2, 3, 4, 5, 6]:

    if n % 2 == 0:

        count = count + 1

print(count)


# Q12
# EN: Trace the built O/E string.
#  HI: O/E string trace karo.

result = ""

for n in [1, 2, 3, 4]:

    if n % 2 == 0:

        result = result + "E"

    else:

        result = result + "O"

print(result)


# Q13
# EN: Trace biggest. HI: biggest trace karo.

biggest = 0

for n in [3, 7, 2, 9, 4]:

    if n > biggest:

        biggest = n

print(biggest)


# Q14
# EN: Note c + result, not result + c.
#  HI: c + result hai, result + c nahi.

result = ""

for c in "hello":

    result = c + result

print(result)


# Q15
# EN: Sum with a step.
#  HI: Step wale range ka sum.

total = 0

for i in range(0, 10, 2):

    total = total + i

print(total)


# Q16
# EN: Only numbers greater than 5 are added. 
# HI: Sirf 5 se bade numbers jodte hain.

total = 0

for n in [3, 8, 1, 10, 5]:

    if n > 5:

        total = total + n

print(total)


# Q17
# EN: Trace the list built with .append(). 
# HI: .append() se banti list trace karo.

items = []

for i in range(1, 4):

    items.append(i * 10)

print(items)


# Q18
# EN: Trace both counters. 
# HI: Dono counters trace karo.

evens = 0

odds = 0

for n in range(1, 8):

    if n % 2 == 0:

        evens = evens + 1

    else:

        odds = odds + 1

print(evens, odds)


# Q19
# EN: Sum of range(5). What does range(5) give? 
# HI: range(5) ka sum. range(5) kya deta hai?

total = 0

for i in range(5):

    total = total + i

print(total)


# Q20
# EN: What do min, max, sum give?
#  HI: min, max, sum kya denge?

nums = [4, 8, 15, 16, 23]

print(min(nums), max(nums), sum(nums))


# Q21
# EN: What do the two in checks print? 
# HI: Dono in checks kya print karenge?

fruits = ["apple", "banana"]

print("apple" in fruits, "cherry" in fruits)


# Q22
# EN: The list is changed by index. What prints? 
# HI: List index se badli jaati hai. Kya print hoga?

nums = [1, 2, 3]

for i in range(len(nums)):

    nums[i] = nums[i] * 10

print(nums)

# Q23
# EN: Trace n and count. Two values print. 
# HI: n aur count trace karo. Do values print hongi.

n = 1

count = 0

while n < 20:

    n = n * 2

    count = count + 1

print(n, count)


# Q24
# EN: The loop stops early with break. 
# HI: Loop break se jaldi rukta hai.

total = 0

for n in [4, 6, 9, 2, 7]:

    if n == 9:

        break

    total = total + n

print(total)


# Q25
# EN: continue skips multiples of 3. 
# HI: continue 3 ke multiples skip karta hai.

total = 0

for n in range(1, 7):

    if n % 3 == 0:

        continue

    total = total + n

print(total)


# Q26
# EN: A loop inside a loop. How many times does count rise? 
# HI: Loop ke andar loop. count kitni baar badhega?

count = 0

for i in range(3):

    for j in range(2):

        count = count + 1

print(count)


# Q27
# EN: Trace count. When does the loop stop? 
# HI: count trace karo. Loop kab rukta hai?

count = 0

num = 100

while num > 1:

    num = num // 2

    count = count + 1

print(count)


# Q28
# EN: while True with a break. What is i?
#  HI: while True + break. i kya hai?

i = 0

while True:

    i = i + 1

    if i == 5:

        break

print(i)


# Q29
# EN: continue skips numbers above 5. 
# HI: continue 5 se bade skip karta hai.

total = 0

for n in [1, 2, 3, 4, 5, 6, 7, 8]:

    if n > 5:

        continue

    total = total + n

print(total)


# Q30
# EN: The inner loop grows each time. Trace lines. 
# HI: Andar wala loop har baar badhta hai. lines trace karo.

lines = 0

for i in range(3):

    for j in range(i + 1):

        lines = lines + 1

print(lines)


# Q31
# EN: Only the first item of each row is added. 
# HI: Har row ka sirf pehla item jodte hain.

matrix = [[1, 2, 3], [4, 5, 6]]

total = 0

for row in matrix:

    total = total + row[0]

print(total)


# Q32
# EN: Tuples are unpacked in the loop. Trace total. 
# HI: Loop mein tuples unpack hote hain. total trace karo.

pairs = [(1, 2), (3, 4), (5, 6)]

total = 0

for a, b in pairs:

    total = total + (a * b)

print(total)

# Q33
# EN: Trace the dictionary being built. 
# HI: Banti hui dictionary trace karo.

counts = {}

for c in "aabbbc":

    if c in counts:

        counts[c] = counts[c] + 1

    else:

        counts[c] = 1

print(counts)
# Q34
# EN: Nested loop + vowel check. How many vowels total? 
# HI: Nested loop + vowel check. Total kitne vowels?

count = 0

for word in ["cat", "dog", "bee"]:

    for letter in word:

        if letter in "aeiou":

            count = count + 1

print(count)


# Q35
# EN: Trace counts (word frequency with .get). 
# HI: counts trace karo (.get se word frequency).

words = ["hi", "bye", "hi", "hi"]

counts = {}

for w in words:

    counts[w] = counts.get(w, 0) + 1

print(counts)


# Q36
# EN: Trace best over the dict values. 
# HI: Dict values par best trace karo.

scores = {"a": 10, "b": 20, "c": 30}

best = 0

for v in scores.values():

    if v > best:

        best = v

print(best)


# Q37
# EN: Sum the prices with .items(). 
# HI: .items() se prices ka sum.

prices = {"pen": 10, "book": 50}

total = 0

for item, price in prices.items():

    total = total + price

print(total)


# Q38
# EN: What does set() do to duplicates? 
# HI: set() duplicates ka kya karta hai?

nums = [1, 2, 2, 3, 3, 3]

print(len(set(nums)))


# Q39
# EN: What do & and | give? 
# HI: & aur | kya denge?

a = {1, 2, 3}

b = {2, 3, 4}

print(a & b, a | b)


# Q40
# EN: Trace the set comprehension. 
# HI: Set comprehension trace karo.

nums = [1, 2, 3, 4, 5, 6]

evens = {n for n in nums if n % 2 == 0}

print(evens)

