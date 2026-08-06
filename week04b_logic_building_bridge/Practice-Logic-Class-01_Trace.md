# Logic Class 1 — Homework: Trace & Predict (40 Questions)

> **Companion to `Week-04b_Logic-Building-Bridge.md` → Logic Class 1.**
> **Rule:** Har question ke liye pehle **trace table banao** (kaagaz par), output **predict** karo, PHIR code chala kar check karo. Run karne se PEHLE likho. / For each question, **build a trace table on paper**, **predict** the output, and only THEN run the code to check.
>
> **Sabhi 40 questions ek hi skill ke liye hain: TRACING (output predict karna).** Sirf Week 0–4 ke concepts. **Koi functions nahi.** Difficulty neeche ki taraf badhti hai — order mat badlo.

---

# PART A — Questions (student worksheet)

## 🟢 Warm-up (1–10): ek variable / simple loop / basic string

### Q1
**EN:** Trace `x` step by step. What prints? **HI:** `x` ko step-by-step trace karo. Kya print hoga?
```python
x = 5
x = x + 3
x = x * 2
print(x)
```

### Q2
**EN:** Predict the final `total`. **HI:** Aakhri `total` predict karo.
```python
total = 0
for n in [1, 2, 3, 4]:
    total = total + n
print(total)
```

### Q3
**EN:** Trace `x` through each turn. **HI:** Har chakkar mein `x` trace karo.
```python
x = 20
for i in range(4):
    x = x - 5
print(x)
```

### Q4
**EN:** What do `//` and `%` give? **HI:** `//` aur `%` kya denge?
```python
a = 17
b = 5
print(a // b, a % b)
```

### Q5
**EN:** How many times does the loop run? **HI:** Loop kitni baar chalta hai?
```python
count = 0
for letter in "python":
    count = count + 1
print(count)
```

### Q6
**EN:** Trace `result` (multiplication). **HI:** `result` trace karo (guna).
```python
result = 1
for n in [2, 2, 3]:
    result = result * n
print(result)
```

### Q7
**EN:** What do these three prints show? **HI:** Yeh teen prints kya dikhayenge?
```python
s = "python"
print(s[0], s[-1], s[1:4])
```

### Q8
**EN:** Trace the string `word` being built. **HI:** `word` string banti hui trace karo.
```python
word = ""
for c in "abc":
    word = word + c + "-"
print(word)
```

### Q9
**EN:** Trace `x` (division makes a float). **HI:** `x` trace karo (division float banata hai).
```python
x = 10
x = x / 2
x = x / 2
print(x)
```

### Q10
**EN:** Sum of `range(2, 6)`. Careful with the last number. **HI:** `range(2, 6)` ka sum. Aakhri number par dhyaan.
```python
total = 0
for i in range(2, 6):
    total = total + i
print(total)
```

---

## 🟡 Core (11–22): loop + if / accumulator / list

### Q11
**EN:** How many even numbers are counted? **HI:** Kitne even numbers gine gaye?
```python
count = 0
for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 == 0:
        count = count + 1
print(count)
```

### Q12
**EN:** Trace the built `O`/`E` string. **HI:** `O`/`E` string trace karo.
```python
result = ""
for n in [1, 2, 3, 4]:
    if n % 2 == 0:
        result = result + "E"
    else:
        result = result + "O"
print(result)
```

### Q13
**EN:** Trace `biggest`. **HI:** `biggest` trace karo.
```python
biggest = 0
for n in [3, 7, 2, 9, 4]:
    if n > biggest:
        biggest = n
print(biggest)
```

### Q14
**EN:** Note `c + result`, not `result + c`. **HI:** `c + result` hai, `result + c` nahi.
```python
result = ""
for c in "hello":
    result = c + result
print(result)
```

### Q15
**EN:** Sum with a step. **HI:** Step wale range ka sum.
```python
total = 0
for i in range(0, 10, 2):
    total = total + i
print(total)
```

### Q16
**EN:** Only numbers greater than 5 are added. **HI:** Sirf 5 se bade numbers jodte hain.
```python
total = 0
for n in [3, 8, 1, 10, 5]:
    if n > 5:
        total = total + n
print(total)
```

### Q17
**EN:** Trace the list built with `.append()`. **HI:** `.append()` se banti list trace karo.
```python
items = []
for i in range(1, 4):
    items.append(i * 10)
print(items)
```

### Q18
**EN:** Trace both counters. **HI:** Dono counters trace karo.
```python
evens = 0
odds = 0
for n in range(1, 8):
    if n % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1
print(evens, odds)
```

### Q19
**EN:** Sum of `range(5)`. What does `range(5)` give? **HI:** `range(5)` ka sum. `range(5)` kya deta hai?
```python
total = 0
for i in range(5):
    total = total + i
print(total)
```

### Q20
**EN:** What do `min`, `max`, `sum` give? **HI:** `min`, `max`, `sum` kya denge?
```python
nums = [4, 8, 15, 16, 23]
print(min(nums), max(nums), sum(nums))
```

### Q21
**EN:** What do the two `in` checks print? **HI:** Dono `in` checks kya print karenge?
```python
fruits = ["apple", "banana"]
print("apple" in fruits, "cherry" in fruits)
```

### Q22
**EN:** The list is changed by index. What prints? **HI:** List index se badli jaati hai. Kya print hoga?
```python
nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 10
print(nums)
```

---

## 🟠 Challenge (23–32): while / break / continue / nested

### Q23
**EN:** Trace `n` and `count`. Two values print. **HI:** `n` aur `count` trace karo. Do values print hongi.
```python
n = 1
count = 0
while n < 20:
    n = n * 2
    count = count + 1
print(n, count)
```

### Q24
**EN:** The loop stops early with `break`. **HI:** Loop `break` se jaldi rukta hai.
```python
total = 0
for n in [4, 6, 9, 2, 7]:
    if n == 9:
        break
    total = total + n
print(total)
```

### Q25
**EN:** `continue` skips multiples of 3. **HI:** `continue` 3 ke multiples skip karta hai.
```python
total = 0
for n in range(1, 7):
    if n % 3 == 0:
        continue
    total = total + n
print(total)
```

### Q26
**EN:** A loop inside a loop. How many times does `count` rise? **HI:** Loop ke andar loop. `count` kitni baar badhega?
```python
count = 0
for i in range(3):
    for j in range(2):
        count = count + 1
print(count)
```

### Q27
**EN:** Trace `count`. When does the loop stop? **HI:** `count` trace karo. Loop kab rukta hai?
```python
count = 0
num = 100
while num > 1:
    num = num // 2
    count = count + 1
print(count)
```

### Q28
**EN:** `while True` with a `break`. What is `i`? **HI:** `while True` + `break`. `i` kya hai?
```python
i = 0
while True:
    i = i + 1
    if i == 5:
        break
print(i)
```

### Q29
**EN:** `continue` skips numbers above 5. **HI:** `continue` 5 se bade skip karta hai.
```python
total = 0
for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n > 5:
        continue
    total = total + n
print(total)
```

### Q30
**EN:** The inner loop grows each time. Trace `lines`. **HI:** Andar wala loop har baar badhta hai. `lines` trace karo.
```python
lines = 0
for i in range(3):
    for j in range(i + 1):
        lines = lines + 1
print(lines)
```

### Q31
**EN:** Only the first item of each row is added. **HI:** Har row ka sirf pehla item jodte hain.
```python
matrix = [[1, 2, 3], [4, 5, 6]]
total = 0
for row in matrix:
    total = total + row[0]
print(total)
```

### Q32
**EN:** Tuples are unpacked in the loop. Trace `total`. **HI:** Loop mein tuples unpack hote hain. `total` trace karo.
```python
pairs = [(1, 2), (3, 4), (5, 6)]
total = 0
for a, b in pairs:
    total = total + (a * b)
print(total)
```

---

## 🔴 Advanced (33–40): dict / set / comprehension

### Q33
**EN:** Trace the dictionary being built. **HI:** Banti hui dictionary trace karo.
```python
counts = {}
for c in "aabbbc":
    if c in counts:
        counts[c] = counts[c] + 1
    else:
        counts[c] = 1
print(counts)
```

### Q34
**EN:** Nested loop + vowel check. How many vowels total? **HI:** Nested loop + vowel check. Total kitne vowels?
```python
count = 0
for word in ["cat", "dog", "bee"]:
    for letter in word:
        if letter in "aeiou":
            count = count + 1
print(count)
```

### Q35
**EN:** Trace `counts` (word frequency with `.get`). **HI:** `counts` trace karo (`.get` se word frequency).
```python
words = ["hi", "bye", "hi", "hi"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
```

### Q36
**EN:** Trace `best` over the dict values. **HI:** Dict values par `best` trace karo.
```python
scores = {"a": 10, "b": 20, "c": 30}
best = 0
for v in scores.values():
    if v > best:
        best = v
print(best)
```

### Q37
**EN:** Sum the prices with `.items()`. **HI:** `.items()` se prices ka sum.
```python
prices = {"pen": 10, "book": 50}
total = 0
for item, price in prices.items():
    total = total + price
print(total)
```

### Q38
**EN:** What does `set()` do to duplicates? **HI:** `set()` duplicates ka kya karta hai?
```python
nums = [1, 2, 2, 3, 3, 3]
print(len(set(nums)))
```

### Q39
**EN:** What do `&` and `|` give? **HI:** `&` aur `|` kya denge?
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b, a | b)
```

### Q40
**EN:** Trace the set comprehension. **HI:** Set comprehension trace karo.
```python
nums = [1, 2, 3, 4, 5, 6]
evens = {n for n in nums if n % 2 == 0}
print(evens)
```

---

# PART B — Answer Key (teacher / self-check)

> *Pehle khud trace karo, PHIR yahan dekho.*

| Q | Output | Short trace |
|---|---|---|
| 1 | `16` | 5 → 8 → 16 |
| 2 | `10` | 0→1→3→6→10 |
| 3 | `0` | 20→15→10→5→0 |
| 4 | `3 2` | 17//5=3, 17%5=2 |
| 5 | `6` | "python" = 6 letters |
| 6 | `12` | 1×2×2×3 |
| 7 | `p n yth` | index 0='p', -1='n', [1:4]='yth' |
| 8 | `a-b-c-` | ""→"a-"→"a-b-"→"a-b-c-" |
| 9 | `2.5` | 10 → 5.0 → 2.5 (division → float) |
| 10 | `14` | 2+3+4+5 (6 shaamil nahi) |
| 11 | `3` | evens: 2, 4, 6 |
| 12 | `OEOE` | 1=O, 2=E, 3=O, 4=E |
| 13 | `9` | biggest: 0→3→7→9 |
| 14 | `olleh` | har letter aage lagta hai → reverse |
| 15 | `20` | 0+2+4+6+8 |
| 16 | `18` | sirf 8 + 10 |
| 17 | `[10, 20, 30]` | append 10, 20, 30 |
| 18 | `3 4` | evens 2,4,6=3; odds 1,3,5,7=4 |
| 19 | `10` | range(5)=0,1,2,3,4 → sum 10 |
| 20 | `4 23 66` | min=4, max=23, sum=66 |
| 21 | `True False` | "apple" hai, "cherry" nahi |
| 22 | `[10, 20, 30]` | har item ×10 |
| 23 | `32 5` | n:1→2→4→8→16→32; count 5 |
| 24 | `10` | 4+6, phir n=9 par break |
| 25 | `12` | 3 aur 6 skip; 1+2+4+5 |
| 26 | `6` | 3 × 2 = 6 baar |
| 27 | `6` | 100→50→25→12→6→3→1 (6 baar) |
| 28 | `5` | i badhta hai, 5 par break |
| 29 | `15` | 6,7,8 skip; 1+2+3+4+5 |
| 30 | `6` | 1 + 2 + 3 (inner loop badhta hai) |
| 31 | `5` | row[0]: 1 + 4 |
| 32 | `44` | 1×2 + 3×4 + 5×6 = 2+12+30 |
| 33 | `{'a': 2, 'b': 3, 'c': 1}` | a×2, b×3, c×1 |
| 34 | `4` | cat=a(1), dog=o(1), bee=e,e(2) |
| 35 | `{'hi': 3, 'bye': 1}` | hi×3, bye×1 |
| 36 | `30` | best: 0→10→20→30 |
| 37 | `60` | 10 + 50 |
| 38 | `3` | set = {1, 2, 3} |
| 39 | `{2, 3} {1, 2, 3, 4}` | `&`=intersection, `|`=union |
| 40 | `{2, 4, 6}` | sirf even numbers |

