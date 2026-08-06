# Logic Class 2 — Homework: Pseudocode & Translate (40 Questions)

> **Companion to `Week-04b_Logic-Building-Bridge.md` → Logic Class 2.**
> **Rule:** Har question ke liye pehle **kaagaz par pseudocode** (plain English/Hinglish steps) likho, PHIR har step ko ek Python line mein badlo, aur ANT mein apne code ko **trace** karke check karo. Keyboard ko haath lagane se PEHLE plan likho. / For each question, first write **pseudocode on paper** (plain steps), THEN translate each step into a Python line, and finally **trace** your code to check it.
>
> **Sabhi 40 questions ek hi skill ke liye hain: PSEUDOCODE se CODE tak (problem → steps → Python).** Sirf Week 0–4 ke concepts. **Koi functions nahi.** Difficulty neeche ki taraf badhti hai — order mat badlo.
>
> **5-step method yaad rakho:** Restate → Example → Pseudocode → Translate → Trace.

---

# PART A — Questions (student worksheet)

## 🟢 Warm-up (1–10): ek variable / if-else / simple maths

### Q1
**EN:** Two numbers are given. Print their sum. **HI:** Do numbers diye hain. Unka sum print karo.
```text
Given: a = 7, b = 5   →  print the total
```

### Q2
**EN:** Two numbers are given. Print the larger one. **HI:** Do numbers diye hain. Bada wala print karo.
```text
Given: a = 8, b = 3
```

### Q3
**EN:** A number is given. Print its square. **HI:** Ek number diya hai. Uska square print karo.
```text
Given: n = 6
```

### Q4
**EN:** A number is given. Print `"Even"` or `"Odd"`. **HI:** Ek number diya hai. `"Even"` ya `"Odd"` print karo.
```text
Given: n = 9
```

### Q5
**EN:** A number is given. Print `"Positive"`, `"Negative"`, or `"Zero"`. **HI:** Ek number diya hai. `"Positive"`, `"Negative"`, ya `"Zero"` print karo.
```text
Given: n = -4
```

### Q6
**EN:** A Celsius temperature is given. Print it in Fahrenheit. (`F = C * 9/5 + 32`) **HI:** Celsius diya hai. Fahrenheit mein print karo.
```text
Given: c = 100
```

### Q7
**EN:** A word is given. Print how many letters it has. **HI:** Ek word diya hai. Usme kitne letters hain print karo.
```text
Given: word = "python"
```

### Q8
**EN:** Two names are given. Join them with a space and print. **HI:** Do naam diye hain. Beech mein space laga kar jodo aur print karo.
```text
Given: first = "Ravi", last = "Kumar"   →  "Ravi Kumar"
```

### Q9
**EN:** A number is given. Print its last digit. **HI:** Ek number diya hai. Uska aakhri digit print karo.
```text
Given: n = 574   →  4
```

### Q10
**EN:** Total seconds are given. Print how many full minutes and leftover seconds. **HI:** Total seconds diye hain. Kitne poore minutes aur bache hue seconds print karo.
```text
Given: total = 130   →  2 minutes 10 seconds
```

---

## 🟡 Core (11–22): loop + accumulator / list / string

### Q11
**EN:** A number `n` is given. Print the sum of all numbers from 1 to `n`. **HI:** Ek number `n` diya hai. 1 se `n` tak sabka sum print karo.
```text
Given: n = 5   →  1+2+3+4+5 = 15
```

### Q12
**EN:** A list of numbers is given. Print the total. **HI:** Numbers ki ek list di hai. Total print karo.
```text
Given: nums = [10, 20, 30, 40]
```

### Q13
**EN:** A list of numbers is given. Count how many are even. **HI:** Numbers ki list di hai. Kitne even hain ginno.
```text
Given: nums = [1, 4, 6, 7, 10, 3]
```

### Q14
**EN:** A list is given. Find the biggest number **without** using `max()`. **HI:** Ek list di hai. `max()` ke bina sabse bada number dhoondho.
```text
Given: nums = [4, 9, 2, 11, 6]
```

### Q15
**EN:** A word is given. Count the vowels in it. **HI:** Ek word diya hai. Usme vowels ginno.
```text
Given: word = "education"
```

### Q16
**EN:** Print all even numbers from 1 to 10, each on its own line. **HI:** 1 se 10 tak saare even numbers print karo, har ek nayi line mein.
```text
(no input — just 1..10)
```

### Q17
**EN:** A list of marks is given. Print the average. **HI:** Marks ki list di hai. Average print karo.
```text
Given: marks = [40, 55, 70, 90]
```

### Q18
**EN:** A word is given. Build and print its reverse (accumulator = `""`). **HI:** Ek word diya hai. Uska reverse banao aur print karo.
```text
Given: word = "hello"   →  "olleh"
```

### Q19
**EN:** A number `n` is given. Print its multiplication table from 1 to 10. **HI:** Ek number `n` diya hai. 1 se 10 tak uska table print karo.
```text
Given: n = 7   →  7 x 1 = 7 ... 7 x 10 = 70
```

### Q20
**EN:** A list is given. Count how many numbers are greater than 10. **HI:** Ek list di hai. 10 se bade kitne numbers hain ginno.
```text
Given: nums = [5, 12, 8, 20, 10, 15]
```

### Q21
**EN:** A list is given. Print the sum of only the odd numbers. **HI:** Ek list di hai. Sirf odd numbers ka sum print karo.
```text
Given: nums = [1, 2, 3, 4, 5, 6]
```

### Q22
**EN:** A number `n` is given. Build a list of squares from 1 to `n` and print it. **HI:** Ek number `n` diya hai. 1 se `n` tak squares ki list banao aur print karo.
```text
Given: n = 5   →  [1, 4, 9, 16, 25]
```

---

## 🟠 Challenge (23–32): while / nested / flag / patterns

### Q23
**EN:** A number `n` is given. Print its factorial (`n!`). **HI:** Ek number `n` diya hai. Uska factorial print karo.
```text
Given: n = 5   →  120
```

### Q24
**EN:** A number is given. Print whether it is prime (flag pattern). **HI:** Ek number diya hai. Batao prime hai ya nahi (flag).
```text
Given: number = 13
```

### Q25
**EN:** A list and a target value are given. Print `True` if the target is in the list, else `False` (flag, no `in`). **HI:** Ek list aur ek target diya hai. Target list mein hai toh `True`, warna `False`.
```text
Given: nums = [3, 8, 1, 7, 5], target = 7
```

### Q26
**EN:** A number is given. Count how many digits it has (use `while` and `// 10`). **HI:** Ek number diya hai. Usme kitne digits hain ginno (`while` + `// 10`).
```text
Given: n = 4592   →  4
```

### Q27
**EN:** A number is given. Print the sum of its digits (use `while`). **HI:** Ek number diya hai. Uske digits ka sum print karo (`while`).
```text
Given: n = 123   →  6
```

### Q28
**EN:** A number is given. Print it reversed (`123` → `321`, use `while`). **HI:** Ek number diya hai. Ulta print karo (`while`).
```text
Given: n = 123   →  321
```

### Q29
**EN:** A number `n` is given. Print a left-aligned star triangle of `n` rows (nested loop). **HI:** Ek number `n` diya hai. `n` rows ka star triangle print karo (nested loop).
```text
Given: n = 4
*
**
***
****
```

### Q30
**EN:** A word is given. Print `"Palindrome"` or `"Not palindrome"`. **HI:** Ek word diya hai. `"Palindrome"` ya `"Not palindrome"` print karo.
```text
Given: word = "madam"
```

### Q31
**EN:** A list is given. Find the smallest number **without** using `min()`. **HI:** Ek list di hai. `min()` ke bina sabse chhota number dhoondho.
```text
Given: nums = [8, 3, 9, 1, 5]
```

### Q32
**EN:** Print FizzBuzz from 1 to 15 (3→Fizz, 5→Buzz, 15→FizzBuzz). **HI:** 1 se 15 tak FizzBuzz print karo.
```text
(order matters: 15 wali shart pehle)
```

---

## 🔴 Advanced (33–40): dict / set / combined

### Q33
**EN:** A word is given. Build a dict counting each character's frequency. **HI:** Ek word diya hai. Har character ki frequency ki dict banao.
```text
Given: word = "banana"   →  {'b': 1, 'a': 3, 'n': 2}
```

### Q34
**EN:** A sentence is given. Build a dict of word → count. **HI:** Ek sentence diya hai. word → count ki dict banao.
```text
Given: sentence = "the cat sat the cat"
```

### Q35
**EN:** A dict of names → scores is given. Print the name with the highest score. **HI:** names → scores ki dict di hai. Sabse zyada score wala naam print karo.
```text
Given: scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}
```

### Q36
**EN:** A list with duplicates is given. Print how many unique values it has (use `set`). **HI:** Duplicates wali list di hai. Kitni unique values hain print karo (`set`).
```text
Given: nums = [1, 2, 2, 3, 3, 3, 4]
```

### Q37
**EN:** Two lists are given. Print the values common to both (use sets). **HI:** Do lists di hain. Dono mein common values print karo (sets).
```text
Given: a = [1, 2, 3, 4], b = [3, 4, 5, 6]
```

### Q38
**EN:** A dict of item → price is given. Print the total cost. **HI:** item → price ki dict di hai. Total cost print karo.
```text
Given: prices = {"pen": 10, "book": 50, "bag": 200}
```

### Q39
**EN:** A word is given. Count vowels and consonants separately (two counters). **HI:** Ek word diya hai. Vowels aur consonants alag-alag ginno.
```text
Given: word = "python"   →  vowels 1, consonants 5
```

### Q40
**EN:** A dict of name → marks is given. Build a new dict of name → "Pass"/"Fail" (pass if marks ≥ 40). **HI:** name → marks ki dict di hai. name → "Pass"/"Fail" ki nayi dict banao (40+ = Pass).
```text
Given: marks = {"Asha": 35, "Ravi": 80, "Zoya": 40}
```

---

# PART B — Answer Key (teacher / self-check)

> *Pehle khud pseudocode (English + Hindi) likho, PHIR Python, PHIR yahan dekho. Aapka code alag dikh sakta hai — output sahi hona chahiye, style exact match zaroori nahi.*

## 🟢 Warm-up (1–10)

### A1 — Sum of two numbers
**Pseudocode (EN):**
```text
1. take the two numbers a and b
2. add them into a total
3. print the total
```
**Pseudocode (HI):**
```text
1. dono numbers a aur b lo
2. dono ko jod kar total banao
3. total print karo
```
**Python:**
```python
a, b = 7, 5
print(a + b)                      # 12
```

### A2 — Larger of two
**Pseudocode (EN):**
```text
1. take a and b
2. if a is greater than b, print a
3. otherwise print b
```
**Pseudocode (HI):**
```text
1. a aur b lo
2. agar a, b se bada hai toh a print karo
3. warna b print karo
```
**Python:**
```python
a, b = 8, 3
if a > b:
    print(a)
else:
    print(b)                      # 8
```

### A3 — Square of a number
**Pseudocode (EN):**
```text
1. take the number n
2. multiply n by itself
3. print the result
```
**Pseudocode (HI):**
```text
1. number n lo
2. n ko usi se guna karo
3. result print karo
```
**Python:**
```python
n = 6
print(n * n)                      # 36
```

### A4 — Even or Odd
**Pseudocode (EN):**
```text
1. take the number n
2. if the remainder of n divided by 2 is 0, print "Even"
3. otherwise print "Odd"
```
**Pseudocode (HI):**
```text
1. number n lo
2. agar n ko 2 se divide karne par remainder 0 hai toh "Even" print karo
3. warna "Odd" print karo
```
**Python:**
```python
n = 9
if n % 2 == 0:
    print("Even")
else:
    print("Odd")                  # Odd
```

### A5 — Positive / Negative / Zero
**Pseudocode (EN):**
```text
1. take the number n
2. if n is greater than 0, print "Positive"
3. else if n is less than 0, print "Negative"
4. otherwise print "Zero"
```
**Pseudocode (HI):**
```text
1. number n lo
2. agar n, 0 se bada hai toh "Positive" print karo
3. warna agar n, 0 se chhota hai toh "Negative" print karo
4. warna "Zero" print karo
```
**Python:**
```python
n = -4
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")             # Negative
else:
    print("Zero")
```

### A6 — Celsius to Fahrenheit
**Pseudocode (EN):**
```text
1. take the Celsius value c
2. compute f = c * 9 / 5 + 32
3. print f
```
**Pseudocode (HI):**
```text
1. Celsius value c lo
2. f = c * 9 / 5 + 32 nikalo
3. f print karo
```
**Python:**
```python
c = 100
f = c * 9 / 5 + 32
print(f)                          # 212.0
```

### A7 — Length of a word
**Pseudocode (EN):**
```text
1. take the word
2. count its letters using len
3. print the count
```
**Pseudocode (HI):**
```text
1. word lo
2. len se uske letters ginno
3. count print karo
```
**Python:**
```python
word = "python"
print(len(word))                  # 6
```

### A8 — Join two names
**Pseudocode (EN):**
```text
1. take first and last name
2. join them with a space in between
3. print the joined name
```
**Pseudocode (HI):**
```text
1. first aur last naam lo
2. beech mein space laga kar jodo
3. joined naam print karo
```
**Python:**
```python
first, last = "Ravi", "Kumar"
print(first + " " + last)         # Ravi Kumar
```

### A9 — Last digit
**Pseudocode (EN):**
```text
1. take the number n
2. the last digit is the remainder of n divided by 10
3. print it
```
**Pseudocode (HI):**
```text
1. number n lo
2. aakhri digit = n ko 10 se divide karne ka remainder
3. use print karo
```
**Python:**
```python
n = 574
print(n % 10)                     # 4
```

### A10 — Minutes and seconds
**Pseudocode (EN):**
```text
1. take total seconds
2. minutes = total divided by 60 (whole number)
3. seconds = remainder of total divided by 60
4. print minutes and seconds
```
**Pseudocode (HI):**
```text
1. total seconds lo
2. minutes = total ko 60 se poora divide (whole number)
3. seconds = total ko 60 se divide karne ka remainder
4. minutes aur seconds print karo
```
**Python:**
```python
total = 130
minutes = total // 60
seconds = total % 60
print(minutes, "minutes", seconds, "seconds")   # 2 minutes 10 seconds
```

## 🟡 Core (11–22)

### A11 — Sum from 1 to n
**Pseudocode (EN):**
```text
1. make a box total = 0
2. for every number i from 1 to n:
3.    add i into total
4. print total
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. 1 se n tak har number i ke liye:
3.    i ko total mein jodo
4. total print karo
```
**Python:**
```python
n = 5
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)                      # 15
```

### A12 — List total
**Pseudocode (EN):**
```text
1. make a box total = 0
2. for every number x in the list:
3.    add x into total
4. print total
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. list ke har number x ke liye:
3.    x ko total mein jodo
4. total print karo
```
**Python:**
```python
nums = [10, 20, 30, 40]
total = 0
for x in nums:
    total = total + x
print(total)                      # 100
```

### A13 — Count evens
**Pseudocode (EN):**
```text
1. make a counter count = 0
2. for every number x in the list:
3.    if x is even, add 1 to count
4. print count
```
**Pseudocode (HI):**
```text
1. ek counter count = 0 banao
2. list ke har number x ke liye:
3.    agar x even hai toh count mein 1 jodo
4. count print karo
```
**Python:**
```python
nums = [1, 4, 6, 7, 10, 3]
count = 0
for x in nums:
    if x % 2 == 0:
        count = count + 1
print(count)                      # 3
```

### A14 — Biggest (no max)
**Pseudocode (EN):**
```text
1. assume biggest = first item of the list
2. for every number x in the list:
3.    if x is greater than biggest, set biggest = x
4. print biggest
```
**Pseudocode (HI):**
```text
1. maano biggest = list ka pehla item
2. list ke har number x ke liye:
3.    agar x, biggest se bada hai toh biggest = x
4. biggest print karo
```
**Python:**
```python
nums = [4, 9, 2, 11, 6]
biggest = nums[0]
for x in nums:
    if x > biggest:
        biggest = x
print(biggest)                    # 11
```

### A15 — Count vowels
**Pseudocode (EN):**
```text
1. make a counter count = 0
2. for every letter in the word:
3.    if the letter is a vowel (a e i o u), add 1 to count
4. print count
```
**Pseudocode (HI):**
```text
1. ek counter count = 0 banao
2. word ke har letter ke liye:
3.    agar letter vowel hai (a e i o u) toh count mein 1 jodo
4. count print karo
```
**Python:**
```python
word = "education"
count = 0
for letter in word:
    if letter in "aeiou":
        count = count + 1
print(count)                      # 5
```

### A16 — Even numbers 1 to 10
**Pseudocode (EN):**
```text
1. for every number n from 1 to 10:
2.    if n is even, print n
```
**Pseudocode (HI):**
```text
1. 1 se 10 tak har number n ke liye:
2.    agar n even hai toh n print karo
```
**Python:**
```python
for n in range(1, 11):
    if n % 2 == 0:
        print(n)                  # 2 4 6 8 10 (each on its own line)
```

### A17 — Average of marks
**Pseudocode (EN):**
```text
1. make a box total = 0
2. for every mark m in the list, add m into total
3. average = total divided by how many marks there are
4. print average
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. list ke har mark m ko total mein jodo
3. average = total ko marks ki ginti se divide karo
4. average print karo
```
**Python:**
```python
marks = [40, 55, 70, 90]
total = 0
for m in marks:
    total = total + m
print(total / len(marks))         # 63.75
```

### A18 — Reverse a string
**Pseudocode (EN):**
```text
1. make an empty box reversed_word = ""
2. for every letter in the word:
3.    put the letter in FRONT of reversed_word
4. print reversed_word
```
**Pseudocode (HI):**
```text
1. ek khaali box reversed_word = "" banao
2. word ke har letter ke liye:
3.    letter ko reversed_word ke AAGE lagao
4. reversed_word print karo
```
**Python:**
```python
word = "hello"
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
print(reversed_word)              # olleh
```

### A19 — Multiplication table
**Pseudocode (EN):**
```text
1. for every i from 1 to 10:
2.    print n, "x", i, "=", n * i
```
**Pseudocode (HI):**
```text
1. 1 se 10 tak har i ke liye:
2.    print karo n, "x", i, "=", n * i
```
**Python:**
```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

### A20 — Count greater than 10
**Pseudocode (EN):**
```text
1. make a counter count = 0
2. for every number x in the list:
3.    if x is greater than 10, add 1 to count
4. print count
```
**Pseudocode (HI):**
```text
1. ek counter count = 0 banao
2. list ke har number x ke liye:
3.    agar x, 10 se bada hai toh count mein 1 jodo
4. count print karo
```
**Python:**
```python
nums = [5, 12, 8, 20, 10, 15]
count = 0
for x in nums:
    if x > 10:
        count = count + 1
print(count)                      # 3
```

### A21 — Sum of odds
**Pseudocode (EN):**
```text
1. make a box total = 0
2. for every number x in the list:
3.    if x is odd, add x into total
4. print total
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. list ke har number x ke liye:
3.    agar x odd hai toh x ko total mein jodo
4. total print karo
```
**Python:**
```python
nums = [1, 2, 3, 4, 5, 6]
total = 0
for x in nums:
    if x % 2 != 0:
        total = total + x
print(total)                      # 9
```

### A22 — List of squares
**Pseudocode (EN):**
```text
1. make an empty list squares
2. for every i from 1 to n:
3.    append i * i to squares
4. print squares
```
**Pseudocode (HI):**
```text
1. ek khaali list squares banao
2. 1 se n tak har i ke liye:
3.    i * i ko squares mein append karo
4. squares print karo
```
**Python:**
```python
n = 5
squares = []
for i in range(1, n + 1):
    squares.append(i * i)
print(squares)                    # [1, 4, 9, 16, 25]
```

## 🟠 Challenge (23–32)

### A23 — Factorial
**Pseudocode (EN):**
```text
1. make a box product = 1
2. for every i from 1 to n:
3.    multiply product by i
4. print product
```
**Pseudocode (HI):**
```text
1. ek box product = 1 banao
2. 1 se n tak har i ke liye:
3.    product ko i se guna karo
4. product print karo
```
**Python:**
```python
n = 5
product = 1
for i in range(1, n + 1):
    product = product * i
print(product)                    # 120
```

### A24 — Prime check (flag)
**Pseudocode (EN):**
```text
1. assume is_prime = True
2. if number is less than 2, is_prime = False
3. for every i from 2 to number-1:
4.    if number divides evenly by i, is_prime = False
5. print is_prime
```
**Pseudocode (HI):**
```text
1. maano is_prime = True
2. agar number 2 se chhota hai toh is_prime = False
3. 2 se number-1 tak har i ke liye:
4.    agar number, i se poora divide ho jaata hai toh is_prime = False
5. is_prime print karo
```
**Python:**
```python
number = 13
is_prime = True
if number < 2:
    is_prime = False
for i in range(2, number):
    if number % i == 0:
        is_prime = False
print(is_prime)                   # True
```

### A25 — Search in list (flag)
**Pseudocode (EN):**
```text
1. assume found = False
2. for every number x in the list:
3.    if x equals the target, found = True
4. print found
```
**Pseudocode (HI):**
```text
1. maano found = False
2. list ke har number x ke liye:
3.    agar x, target ke barabar hai toh found = True
4. found print karo
```
**Python:**
```python
nums = [3, 8, 1, 7, 5]
target = 7
found = False
for x in nums:
    if x == target:
        found = True
print(found)                      # True
```

### A26 — Count digits (while)
**Pseudocode (EN):**
```text
1. make a counter count = 0
2. while n is greater than 0:
3.    remove the last digit (n = n // 10)
4.    add 1 to count
5. print count
```
**Pseudocode (HI):**
```text
1. ek counter count = 0 banao
2. jab tak n, 0 se bada hai:
3.    aakhri digit hatao (n = n // 10)
4.    count mein 1 jodo
5. count print karo
```
**Python:**
```python
n = 4592
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print(count)                      # 4
```

### A27 — Sum of digits (while)
**Pseudocode (EN):**
```text
1. make a box total = 0
2. while n is greater than 0:
3.    add the last digit (n % 10) into total
4.    remove the last digit (n = n // 10)
5. print total
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. jab tak n, 0 se bada hai:
3.    aakhri digit (n % 10) ko total mein jodo
4.    aakhri digit hatao (n = n // 10)
5. total print karo
```
**Python:**
```python
n = 123
total = 0
while n > 0:
    total = total + (n % 10)
    n = n // 10
print(total)                      # 6
```

### A28 — Reverse a number (while)
**Pseudocode (EN):**
```text
1. make a box reversed_num = 0
2. while n is greater than 0:
3.    take the last digit (n % 10)
4.    reversed_num = reversed_num * 10 + last digit
5.    remove the last digit (n = n // 10)
6. print reversed_num
```
**Pseudocode (HI):**
```text
1. ek box reversed_num = 0 banao
2. jab tak n, 0 se bada hai:
3.    aakhri digit lo (n % 10)
4.    reversed_num = reversed_num * 10 + aakhri digit
5.    aakhri digit hatao (n = n // 10)
6. reversed_num print karo
```
**Python:**
```python
n = 123
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + (n % 10)
    n = n // 10
print(reversed_num)               # 321
```

### A29 — Star triangle (nested loop)
**Pseudocode (EN):**
```text
1. for every row i from 1 to n:
2.    make an empty line ""
3.    for j from 1 to i: add a "*" to the line
4.    print the line
```
**Pseudocode (HI):**
```text
1. 1 se n tak har row i ke liye:
2.    ek khaali line "" banao
3.    1 se i tak har j ke liye: line mein ek "*" jodo
4.    line print karo
```
**Python:**
```python
n = 4
for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line = line + "*"
    print(line)
```

### A30 — Palindrome
**Pseudocode (EN):**
```text
1. build the reverse of the word (empty box, letter in front)
2. if the word equals its reverse, print "Palindrome"
3. otherwise print "Not palindrome"
```
**Pseudocode (HI):**
```text
1. word ka reverse banao (khaali box, letter aage lagao)
2. agar word apne reverse ke barabar hai toh "Palindrome" print karo
3. warna "Not palindrome" print karo
```
**Python:**
```python
word = "madam"
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
if word == reversed_word:
    print("Palindrome")           # Palindrome
else:
    print("Not palindrome")
```

### A31 — Smallest (no min)
**Pseudocode (EN):**
```text
1. assume smallest = first item of the list
2. for every number x in the list:
3.    if x is less than smallest, set smallest = x
4. print smallest
```
**Pseudocode (HI):**
```text
1. maano smallest = list ka pehla item
2. list ke har number x ke liye:
3.    agar x, smallest se chhota hai toh smallest = x
4. smallest print karo
```
**Python:**
```python
nums = [8, 3, 9, 1, 5]
smallest = nums[0]
for x in nums:
    if x < smallest:
        smallest = x
print(smallest)                   # 1
```

### A32 — FizzBuzz 1 to 15
**Pseudocode (EN):**
```text
1. for every n from 1 to 15:
2.    if n divides by BOTH 3 and 5, print "FizzBuzz"
3.    else if n divides by 3, print "Fizz"
4.    else if n divides by 5, print "Buzz"
5.    otherwise print n
```
**Pseudocode (HI):**
```text
1. 1 se 15 tak har n ke liye:
2.    agar n, 3 AUR 5 dono se divide ho toh "FizzBuzz" print karo
3.    warna agar n, 3 se divide ho toh "Fizz" print karo
4.    warna agar n, 5 se divide ho toh "Buzz" print karo
5.    warna n print karo
```
**Python:**
```python
for n in range(1, 16):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
```

## 🔴 Advanced (33–40)

### A33 — Character frequency dict
**Pseudocode (EN):**
```text
1. make an empty dict counts
2. for every character c in the word:
3.    if c is already in counts, add 1 to its value
4.    otherwise set counts[c] = 1
5. print counts
```
**Pseudocode (HI):**
```text
1. ek khaali dict counts banao
2. word ke har character c ke liye:
3.    agar c pehle se counts mein hai toh uski value mein 1 jodo
4.    warna counts[c] = 1 set karo
5. counts print karo
```
**Python:**
```python
word = "banana"
counts = {}
for c in word:
    if c in counts:
        counts[c] = counts[c] + 1
    else:
        counts[c] = 1
print(counts)                     # {'b': 1, 'a': 3, 'n': 2}
```

### A34 — Word frequency dict
**Pseudocode (EN):**
```text
1. split the sentence into words
2. make an empty dict counts
3. for every word:
4.    counts[word] = its current count (0 if new) + 1
5. print counts
```
**Pseudocode (HI):**
```text
1. sentence ko words mein todo (split)
2. ek khaali dict counts banao
3. har word ke liye:
4.    counts[word] = uski abhi ki count (naya ho toh 0) + 1
5. counts print karo
```
**Python:**
```python
sentence = "the cat sat the cat"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)                     # {'the': 2, 'cat': 2, 'sat': 1}
```

### A35 — Highest score name
**Pseudocode (EN):**
```text
1. make boxes best_name = "" and best_score = 0
2. for every name and score in the dict:
3.    if score is greater than best_score:
4.        best_score = score and best_name = name
5. print best_name
```
**Pseudocode (HI):**
```text
1. do box banao: best_name = "" aur best_score = 0
2. dict ke har name aur score ke liye:
3.    agar score, best_score se bada hai:
4.        best_score = score aur best_name = name
5. best_name print karo
```
**Python:**
```python
scores = {"Asha": 40, "Ravi": 85, "Zoya": 70}
best_name = ""
best_score = 0
for name, score in scores.items():
    if score > best_score:
        best_score = score
        best_name = name
print(best_name)                  # Ravi
```

### A36 — Count unique (set)
**Pseudocode (EN):**
```text
1. convert the list into a set (removes duplicates)
2. count how many items the set has
3. print that count
```
**Pseudocode (HI):**
```text
1. list ko set mein badlo (duplicates hat jaate hain)
2. set mein kitne items hain ginno
3. woh count print karo
```
**Python:**
```python
nums = [1, 2, 2, 3, 3, 3, 4]
print(len(set(nums)))             # 4
```

### A37 — Common values (sets)
**Pseudocode (EN):**
```text
1. convert both lists into sets
2. take the values present in BOTH sets (intersection)
3. print the result
```
**Pseudocode (HI):**
```text
1. dono lists ko sets mein badlo
2. dono sets mein jo values common hain woh lo (intersection)
3. result print karo
```
**Python:**
```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set(a) & set(b))            # {3, 4}
```

### A38 — Total cost from dict
**Pseudocode (EN):**
```text
1. make a box total = 0
2. for every item and price in the dict:
3.    add price into total
4. print total
```
**Pseudocode (HI):**
```text
1. ek box total = 0 banao
2. dict ke har item aur price ke liye:
3.    price ko total mein jodo
4. total print karo
```
**Python:**
```python
prices = {"pen": 10, "book": 50, "bag": 200}
total = 0
for item, price in prices.items():
    total = total + price
print(total)                      # 260
```

### A39 — Vowels vs consonants
**Pseudocode (EN):**
```text
1. make two counters vowels = 0 and consonants = 0
2. for every letter in the word:
3.    if it is a vowel, add 1 to vowels
4.    otherwise add 1 to consonants
5. print vowels and consonants
```
**Pseudocode (HI):**
```text
1. do counter banao: vowels = 0 aur consonants = 0
2. word ke har letter ke liye:
3.    agar vowel hai toh vowels mein 1 jodo
4.    warna consonants mein 1 jodo
5. vowels aur consonants print karo
```
**Python:**
```python
word = "python"
vowels = 0
consonants = 0
for letter in word:
    if letter in "aeiou":
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print(vowels, consonants)         # 1 5
```

### A40 — Pass/Fail dict
**Pseudocode (EN):**
```text
1. make an empty dict result
2. for every name and score in the marks dict:
3.    if score is 40 or more, result[name] = "Pass"
4.    otherwise result[name] = "Fail"
5. print result
```
**Pseudocode (HI):**
```text
1. ek khaali dict result banao
2. marks dict ke har name aur score ke liye:
3.    agar score 40 ya usse zyada hai toh result[name] = "Pass"
4.    warna result[name] = "Fail"
5. result print karo
```
**Python:**
```python
marks = {"Asha": 35, "Ravi": 80, "Zoya": 40}
result = {}
for name, score in marks.items():
    if score >= 40:
        result[name] = "Pass"
    else:
        result[name] = "Fail"
print(result)                     # {'Asha': 'Fail', 'Ravi': 'Pass', 'Zoya': 'Pass'}
```

---

*Pairs with `Week-04b_Logic-Building-Bridge.md` (Logic Class 2 — Pseudocode) aur `Practice-Logic-Class-01_Trace.md`. Yaad rakho: pehle **kaagaz par pseudocode** (English + Hindi), PHIR Python, PHIR trace. Plan pehle, code baad mein.*
