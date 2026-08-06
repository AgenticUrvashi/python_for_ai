# WEEK 3 — Sequences: Lists, Tuples & Strings (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Ab tak hum ek box mein ek hi value rakhte the. Is week ek box mein BAHUT SAARI values rakhna sikhenge — yeh hain lists, tuples. Yeh super important hai kyunki ek AI agent ki poori chat history bhi ek 'list' hi hoti hai."*

---

## CLASS 21 — Lists: Create, Index, Slice

*"Recap: ab tak ek variable = ek value. Par socho aapko 50 students ke naam store karne hain. 50 variables? Pagal ho jayenge! Solution: ek LIST — ek hi box jo kai values ek line mein, order ke saath rakhta hai."*

### 🎯 Today's goal
List banana, items ko index se nikalna, aur slicing se hisse kaatna.

### 👨‍🏫 Concept 1 — list banana

> **📖 Technical definition — List:** A list is an ordered, mutable collection that can hold items of any type. Elements are accessed by a zero-based index, and the list can grow or shrink as items are added or removed.

*"List square brackets `[ ]` se banti hai, items comma se alag."*
```python
fruits = ["apple", "banana", "mango"]
marks = [85, 90, 78, 92]
mixed = ["Asha", 17, True]     # alag types bhi chal jaate hain
empty = []                     # khaali list

print(fruits)        # ['apple', 'banana', 'mango']
print(len(fruits))   # 3  — len() items ginta hai
```

### 👨‍🏫 Concept 2 — indexing (position se item nikalna)

> **📖 Technical definition — Indexing:** Indexing is accessing a single element of a sequence by its position. Positions start at 0 for the first element; negative indices count backwards from the end, so `-1` is the last element.

*"BAHUT important: counting 0 se shuru hoti hai, 1 se nahi! Pehla item index 0 par hai."*
```python
fruits = ["apple", "banana", "mango"]
#            0         1         2

print(fruits[0])     # apple   (pehla)
print(fruits[1])     # banana  (doosra)
print(fruits[2])     # mango   (teesra)
```
**Negative index — peeche se ginti:**
```python
print(fruits[-1])    # mango   (aakhri)
print(fruits[-2])    # banana  (aakhri se doosra)
```
*"`[-1]` ka matlab hamesha 'aakhri item'. Yeh super useful hai — chat history ka aakhri message paane ke liye perfect."*

### 👨‍🏫 ⚠️ Concept 3 — IndexError
```python
fruits = ["apple", "banana", "mango"]
print(fruits[3])     # ❌ IndexError — sirf 0,1,2 exist karte hain
```
*"3 items hain, toh valid indexes 0,1,2 hain. Index 3 maangoge → error. Yaad rakho: last valid index hamesha `len - 1` hota hai."*

### 👨‍🏫 Concept 4 — slicing (ek hissa kaatna)

> **📖 Technical definition — Slicing:** Slicing extracts a subsequence using the form `sequence[start:stop:step]`. The start index is included and the stop index is excluded; step controls the direction and stride. Slicing returns a new sequence and leaves the original unchanged.

*"Slice ek 'sub-list' deta hai. Format: `list[start:stop]` — start SHAMIL, stop SHAMIL NAHI (jaise range)."*
```python
nums = [10, 20, 30, 40, 50]
#         0   1   2   3   4

print(nums[1:4])     # [20, 30, 40]  (index 1,2,3 — 4 nahi)
print(nums[:3])      # [10, 20, 30]  (shuru se index 2 tak)
print(nums[2:])      # [30, 40, 50]  (index 2 se end tak)
print(nums[:])       # poori copy
print(nums[::2])     # [10, 30, 50]  (har doosra item — step 2)
print(nums[::-1])    # [50, 40, 30, 20, 10]  (ulta!)
```
*"`[::-1]` ek famous trick hai — list (ya string) ko ulta kar deta hai."*

### 💻 Demo — weekday list
```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(f"First day: {days[0]}")
print(f"Last day: {days[-1]}")
print(f"Weekend: {days[5:]}")        # ['Sat', 'Sun']
print(f"Working days: {days[:5]}")   # Mon..Fri
```

### ❌ Common mistakes
```python
fruits = ["apple", "banana"]
print(fruits[2])     # ❌ IndexError — index 0 aur 1 hi valid hain
print(fruits(0))     # ❌ TypeError — () nahi, [] use karo indexing ke liye
```

### 🔗 Agentic link
*"Yeh week ka sabse bada idea: **ek AI chatbot ki poori conversation ek LIST hoti hai.** Har message list ka ek item hai. Aakhri message paane ke liye `messages[-1]` use karte hain — bilkul jo aaj seekha. Lists master = agent memory ka aadha kaam done."*

### ✍️ Homework
1. 5 favourite movies ki list banao, pehli aur aakhri print karo.
2. `[10,20,30,40,50,60]` mein se beech ke 3 numbers slice karo.
3. Kisi bhi list ko `[::-1]` se ulta karke print karo.

**Answers:**
```python
# 1
movies = ["3 Idiots", "Dangal", "RRR", "PK", "Sholay"]
print(movies[0])     # 3 Idiots
print(movies[-1])    # Sholay

# 2
nums = [10, 20, 30, 40, 50, 60]
print(nums[2:5])     # [30, 40, 50]

# 3
print(nums[::-1])    # [60, 50, 40, 30, 20, 10]
```

### 🔗 Agli class
*"Agli class — lists ko BADALNA: items add karna, hatana, sort karna. Lists ki asli power yahin hai."*

---

## CLASS 22 — List Methods

*"Pichli class mein humne list padhi (read ki). Aaj use BADLENGE — items add, remove, sort. Lists 'mutable' hain (badal sakti hain), aur yahi unhe itna useful banata hai."*

### 🎯 Today's goal
List ko modify karna: `append/insert/remove/pop/extend`, aur `sort/sorted/reverse`, plus `len/in/min/max/sum`.

### 👨‍🏫 Concept 1 — items add karna

> **📖 Technical definition — List method:** A list method is a built-in operation attached to a list object that inspects or modifies the list, such as `append()`, `insert()`, `remove()`, `pop()`, `extend()`, `sort()`, and `reverse()`. Because lists are mutable, many of these methods change the list in place.

```python
cart = ["milk", "bread"]

cart.append("eggs")          # end mein add
print(cart)                  # ['milk', 'bread', 'eggs']

cart.insert(0, "butter")     # index 0 par add
print(cart)                  # ['butter', 'milk', 'bread', 'eggs']

cart.extend(["rice", "dal"]) # ek saath kai items add
print(cart)                  # ['butter', 'milk', 'bread', 'eggs', 'rice', 'dal']
```
*"`append` = ek item end mein. `insert` = ek item kisi position par. `extend` = ek poori list jod do. Sabse zyada `append` use hota hai."*

### 👨‍🏫 Concept 2 — items hatana
```python
cart = ["butter", "milk", "bread", "eggs"]

cart.remove("milk")      # value se hatao
print(cart)              # ['butter', 'bread', 'eggs']

last = cart.pop()        # aakhri item nikaalo AUR woh value return karo
print(last)              # eggs
print(cart)              # ['butter', 'bread']

cart.pop(0)              # index se hatao (yahan pehla)
print(cart)              # ['bread']
```
*"`remove(value)` value dhoondh kar hatata hai. `pop(index)` position se hatata hai AUR hata hui value wapas deta hai (useful!)."*

### 👨‍🏫 Concept 3 — sort karna (do tareeke)

> **📖 Technical definition — `sort()` vs `sorted()`:** The list method `.sort()` reorders a list in place and returns `None`. The built-in function `sorted()` returns a new sorted list and leaves the original untouched. Both accept a `reverse` flag and an optional `key` function.

```python
nums = [40, 10, 30, 20]

nums.sort()              # ORIGINAL list ko badal deta hai
print(nums)              # [10, 20, 30, 40]

nums.sort(reverse=True)  # ulta sort
print(nums)              # [40, 30, 20, 10]
```
```python
nums = [40, 10, 30, 20]
new_list = sorted(nums)  # NAYI sorted list, original safe
print(new_list)          # [10, 20, 30, 40]
print(nums)              # [40, 10, 30, 20]  (original unchanged)
```
*"Bada difference: `.sort()` original ko BADAL deta hai. `sorted()` ek NAYI list deta hai, original chhodta hai. Jab original safe rakhna ho, `sorted()` use karo."*

### 👨‍🏫 Concept 4 — kaam ke helpers
```python
marks = [85, 90, 78, 92, 88]

print(len(marks))        # 5    (kitne items)
print(max(marks))        # 92   (sabse bada)
print(min(marks))        # 78   (sabse chhota)
print(sum(marks))        # 433  (sabka total)
print(sum(marks) / len(marks))   # 86.6 (average)
print(90 in marks)       # True (member check)
print(100 in marks)      # False
```

### 💻 Demo — to-do list live editing
```python
todo = []

todo.append("Study Python")
todo.append("Do homework")
todo.append("Play cricket")
print(todo)

todo.remove("Play cricket")     # cancel
print(f"Tasks left: {len(todo)}")     # Tasks left: 2

done = todo.pop(0)              # pehla task complete
print(f"Completed: {done}")     # Completed: Study Python
print(f"Remaining: {todo}")     # Remaining: ['Do homework']
```

### ❌ Common mistakes
```python
nums = [3, 1, 2]
result = nums.sort()     # ❌ result None hai! .sort() kuch return nahi karta
print(result)            # None
# sahi: nums.sort() phir nums use karo, YA sorted(nums) lo

cart = ["milk"]
cart.remove("bread")     # ❌ ValueError — "bread" list mein hai hi nahi
```

### 🔗 Agentic link
*"Jab user naya message bhejta hai, agent `history.append(new_message)` karta hai. Jab search results aate hain, hum unhe score ke hisaab se `sorted()` karte hain. `.append()` aur `sorted()` aap har agent mein dekhoge."*

### ✍️ Homework
1. Khaali list mein 5 numbers append karo, phir max, min, aur average print karo.
2. Ek list ko `sorted()` se sort karo BINA original badle (dono print karke dikhao).
3. Ek list se `pop()` se aakhri item nikaalo aur use print karo.

**Answers:**
```python
# 1
nums = []
nums.append(10)
nums.append(50)
nums.append(20)
nums.append(40)
nums.append(30)
print(f"Max: {max(nums)}, Min: {min(nums)}, Avg: {sum(nums)/len(nums)}")
# Max: 50, Min: 10, Avg: 30.0

# 2
original = [5, 2, 8, 1]
new = sorted(original)
print(new)         # [1, 2, 5, 8]
print(original)    # [5, 2, 8, 1]

# 3
items = ["a", "b", "c"]
last = items.pop()
print(last)        # c
```

### 🔗 Agli class
*"Agli class — list ke andar list (nested lists). Tables aur grids banayenge."*

---

## CLASS 23 — Nested Lists

*"Ek list ke andar values hoti hain. Par agar har value KHUD ek list ho? Tab humein ek 'grid' ya 'table' mil jaata hai — rows aur columns. Yeh data ke liye bahut common hai."*

### 🎯 Today's goal
Nested lists (list of lists) banana, index karna, aur loop karna.

### 👨‍🏫 Concept 1 — nested list kya hai

> **📖 Technical definition — Nested list:** A nested list is a list whose elements are themselves lists. It represents two-dimensional (or higher) data such as grids or tables, where an element is reached using multiple indices, for example `grid[row][column]`.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(grid)        # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(grid))   # 3  — 3 rows (har row ek list hai)
```
*"Soch lo ek register: har row ek student, row ke andar uske marks. Bahar wali list = rows, andar wali list = us row ka data."*

### 👨‍🏫 Concept 2 — do index lagते hain `grid[row][col]`
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])       # [1, 2, 3]   — pehli row (poori)
print(grid[0][0])    # 1           — pehli row, pehla item
print(grid[1][2])    # 6           — doosri row, teesra item
print(grid[-1][-1])  # 9           — aakhri row, aakhri item
```
*"Pehla bracket row choose karta hai, doosra us row ke andar column. `grid[1][2]` = 'row 1 mein jao, phir item 2 lo'."*

### 👨‍🏫 Concept 3 — nested loop se ghoomna
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in grid:
    for item in row:
        print(item, end=" ")
    print()          # row ke baad nayi line
```
Output:
```
1 2 3 
4 5 6 
7 8 9 
```
*"Bahar wala loop ek-ek row uthata hai. Andar wala loop us row ke har item par chalta hai. Yeh kal wale nested loops ka asli use hai."*

### 💻 Demo — marks table
```python
students = [
    ["Asha", 85, 90],
    ["Rahul", 78, 88],
    ["Priya", 92, 95],
]

for student in students:
    name = student[0]
    total = student[1] + student[2]
    print(f"{name}: total = {total}")
```
Output:
```
Asha: total = 175
Rahul: total = 166
Priya: total = 187
```

### ❌ Common mistakes
```python
grid = [[1, 2], [3, 4]]
print(grid[2])       # ❌ IndexError — sirf row 0 aur 1 hain
print(grid[0][5])    # ❌ IndexError — row 0 mein sirf index 0,1 hain
```

### 🔗 Agentic link
*"Jab agent ek saath kai documents process karta hai, ya batch mein kai results aate hain, woh aksar 'list of lists' ya 'list of records' hote hain. Rows par loop karna — exactly aaj wala skill — har data pipeline mein chahiye."*

### ✍️ Homework
1. Ek 2x2 grid banao aur `grid[0][1]` aur `grid[1][0]` print karo.
2. 3 students ka naam aur 3 subjects ke marks rakho; har student ka total print karo.
3. Ek 3x3 grid ke saare items nested loop se print karo.

**Answers:**
```python
# 1
grid = [[1, 2], [3, 4]]
print(grid[0][1])    # 2
print(grid[1][0])    # 3

# 2
students = [
    ["Amit", 70, 80, 90],
    ["Sara", 60, 75, 85],
    ["Ravi", 88, 92, 79],
]
for s in students:
    total = s[1] + s[2] + s[3]
    print(f"{s[0]}: {total}")

# 3
grid = [[1,2,3],[4,5,6],[7,8,9]]
for row in grid:
    for item in row:
        print(item, end=" ")
    print()
```

### 🔗 Agli class
*"Agli class — tuples: lists ke 'lock' wale cousin, jo badal nahi sakte. Aur ek bahut cool trick: unpacking."*

---

## CLASS 24 — Tuples & Unpacking

*"List ko hum badal sakte hain. Par kabhi-kabhi hum CHAHTE hain ki data badle hi NAHI — jaise ek coordinate (latitude, longitude) ya ek record. Iske liye Python deta hai TUPLE — ek list jaisa, par locked."*

### 🎯 Today's goal
Tuple banana, uski immutability samajhna, aur unpacking use karna.

### 👨‍🏫 Concept 1 — tuple banana

> **📖 Technical definition — Tuple:** A tuple is an ordered, immutable collection of values. Once created its contents cannot be changed, which makes it suitable for fixed records and for data that should not be modified accidentally.

*"Tuple round brackets `( )` se banta hai (ya bina brackets, sirf commas se)."*
```python
point = (10, 20)
rgb = (255, 128, 0)
person = ("Asha", 17, "Mumbai")

print(point[0])      # 10   — indexing list jaisa hi
print(len(person))   # 3
```

### 👨‍🏫 Concept 2 — immutability (badal nahi sakte)

> **📖 Technical definition — Immutability:** An immutable object is one whose state cannot be changed after it is created. Any operation that appears to modify it actually produces a new object, leaving the original unchanged.

```python
point = (10, 20)
point[0] = 99        # ❌ TypeError — tuple badla nahi jaa sakta
```
*"Yeh ERROR hai, aur yeh GOOD hai! Kyun? Kyunki kuch data ko galti se badalne se bachana zaroori hai. Tuple ek 'guarantee' hai: yeh values fixed hain. List 'badal sakti hai', tuple 'fixed hai'. Jab data nahi badalna chahiye, tuple use karo."*

| List `[ ]` | Tuple `( )` |
|---|---|
| Badal sakti hai (mutable) | Fix hai (immutable) |
| Cheezein add/remove hoti rahein | Data ek record jaisa fixed ho |
| `messages.append(...)` | `(latitude, longitude)` |

### 👨‍🏫 Concept 3 — unpacking (ek saath kai variables mein kholna)

> **📖 Technical definition — Unpacking:** Unpacking assigns the individual elements of an iterable to multiple variables in a single statement. The number of target variables must match the number of elements (unless a starred `*` variable is used to capture the rest).

*"Yeh super clean feature hai. Ek tuple (ya list) ko seedhe kai variables mein khol sakte ho:"*
```python
point = (10, 20)
x, y = point          # x ko 10, y ko 20 mil gaya!
print(x)              # 10
print(y)              # 20

person = ("Asha", 17, "Mumbai")
name, age, city = person
print(f"{name} is {age}, from {city}")
```
*"Left side ke variables count, right side ke values count se match hona chahiye."*

### 👨‍🏫 Concept 4 — swap trick (do values aapas mein badlo)
```python
a = 5
b = 10
a, b = b, a           # ek line mein swap!
print(a, b)           # 10 5
```
*"Doosri languages mein iske liye ek temp variable chahiye hota. Python mein bas ek line. Yeh tuple unpacking ki khoobsurti hai."*

### 💻 Demo — function jaisa multi-return (preview)
```python
def min_max(numbers):
    return min(numbers), max(numbers)   # do values ek tuple mein return

low, high = min_max([4, 9, 1, 7])      # unpack
print(f"Lowest: {low}, Highest: {high}")   # Lowest: 1, Highest: 7
```
*"Functions hum next week detail mein karenge — par dekho, ek function do values laut sakta hai (tuple ke roop mein), aur hum unhe unpack kar lete hain. Bahut common pattern."*

### ❌ Common mistakes
```python
single = (5)        # ❌ yeh tuple NAHI, sirf number 5 hai!
single = (5,)       # ✅ ek-item tuple ke liye comma zaroori hai

a, b = (1, 2, 3)    # ❌ ValueError — 3 values, 2 variables (count match nahi)
```

### 🔗 Agentic link
*"Agent mein bahut data 'records' hote hain jo badalne nahi chahiye — jaise ek message ka `(role, content)` pair, ya config settings. Tuples yeh fix rakhte hain. Aur unpacking se hum tools se aaye multiple results saaf-saaf alag kar lete hain."*

### ✍️ Homework
1. Ek tuple banao `("Rahul", 17, "Delhi")` aur teeno values unpack karke print karo.
2. Do variables ko swap karo bina temp variable ke.
3. Try karo tuple ka koi item badalne ki — error padho aur ek line likho kyun aaya.

**Answers:**
```python
# 1
person = ("Rahul", 17, "Delhi")
name, age, city = person
print(name, age, city)      # Rahul 17 Delhi

# 2
x, y = 1, 2
x, y = y, x
print(x, y)                 # 2 1

# 3
t = (1, 2, 3)
# t[0] = 99   # TypeError: tuples immutable hain, badle nahi jaa sakte
```

### 🔗 Agli class
*"Agli class — strings ki deep skills: text ko todna, jodna, search karna. Yeh seedha AI prompts se judta hai."*

---

## CLASS 25 — Advanced Strings (Practice Class)

*"Pichli baar strings ki basics ki thi. Aaj PRO level: text ko precisely todna, jodna, aur usme khojna. Yaad rakho — AI ka sab kuch text hai, toh text master = AI ka aadha kaam."*

### 🎯 Today's goal
String methods `.find/.join/.startswith/.endswith/.count`, aur deep slicing.

### 👨‍🏫 Concept 1 — string bhi ek sequence hai!

> **📖 Technical definition — Sequence:** A sequence is any ordered collection of elements that supports indexing, slicing, length, and iteration. Lists, tuples, and strings are all sequences; a string is specifically an immutable sequence of characters.

*"Bada raaz: string bhi list jaisa hi index aur slice hoti hai — har character ek item jaisा hai."*
```python
word = "PYTHON"
#       012345

print(word[0])       # P
print(word[-1])      # N
print(word[0:3])     # PYT
print(word[::-1])    # NOHTYP   (ulta — list jaise hi)
print(len(word))     # 6
```

### 👨‍🏫 Concept 2 — `.split()` aur `.join()` (todna aur jodna)

> **📖 Technical definition — `split()` and `join()`:** `.split()` breaks a string into a list of substrings using a separator. `.join()` is the inverse: it concatenates the items of an iterable of strings into a single string, placing the separator string between each item.

```python
sentence = "I love Python"
words = sentence.split()        # space par todo → list
print(words)                    # ['I', 'love', 'Python']

csv = "apple,banana,mango"
fruits = csv.split(",")         # comma par todo
print(fruits)                   # ['apple', 'banana', 'mango']

# join — list ko wapas string banao
joined = " ".join(words)        # space se jodo
print(joined)                   # I love Python
dashed = "-".join(fruits)       # dash se jodo
print(dashed)                   # apple-banana-mango
```
*"`.split()` string → list. `.join()` list → string. Yeh do ulte kaam hain. `"glue".join(list)` ka matlab — list ke items ko 'glue' se jodo."*

### 👨‍🏫 Concept 3 — search methods
```python
text = "I love Python programming"

print(text.find("Python"))      # 7    — kis index par milta hai (-1 agar na mile)
print(text.count("o"))          # 3    — kitni baar 'o' aata hai
print(text.startswith("I"))     # True
print(text.endswith("ing"))     # True
print("Python" in text)         # True — sabse simple member check
```
*"`.find()` position deta hai (na mile toh -1). `in` sirf haan/naa deta hai — agar bas check karna ho toh `in` zyada simple hai."*

### 💻 Demo — input clean karke process karo
```python
raw = "  Hello, World, Python  "
cleaned = raw.strip()                       # bahar ke spaces gaye
parts = cleaned.split(",")                  # comma par todo
parts = [p.strip() for p in parts]          # har piece ke spaces bhi saaf
print(parts)                                # ['Hello', 'World', 'Python']
print(" | ".join(parts))                    # Hello | World | Python
```
*"Yeh ek real text-cleaning pipeline hai: strip → split → har piece strip → join. AI input handle karne ka asli tareeka."*

### 💻 Practice problems (saath karte hain)
```python
# 1) String ulta karo
text = "hello"
print(text[::-1])               # olleh

# 2) Vowels gino
text = "education"
count = 0
for char in text:
    if char in "aeiou":
        count = count + 1
print(count)                    # 5

# 3) Palindrome check (aage-peeche same?)
word = "madam"
if word == word[::-1]:
    print("Palindrome")         # Palindrome
else:
    print("Not a palindrome")
```

### ❌ Common mistakes
```python
text = "hello"
text[0] = "H"        # ❌ TypeError — strings bhi immutable hain (tuple jaise)
# sahi: naya string banao → "H" + text[1:]  → "Hello"

print("abc".find("z"))   # -1 (mila nahi) — error nahi, par -1 ko handle karna
```

### 🔗 Agentic link
*"AI model ka jawaab aksar messy text hota hai. Hum `.split()` se use todte hain, `.find()`/`in` se keywords dhoondhte hain, `.strip()` se saaf karte hain, aur `.join()` se dobara banate hain. Jaise model ke output mein se code block ya JSON nikalna — yeh saari skills aaj wali hain. Next week regex se aur powerful karenge."*

### ✍️ Homework
1. User se sentence lo, usme kitne words hain print karo (`.split()` + `len`).
2. Ek comma-separated string ko list mein todo, phir " - " se dobara jodo.
3. Check karo "level" aur "python" palindrome hain ya nahi.

**Answers:**
```python
# 1
sentence = input("Enter a sentence: ")
print(f"Words: {len(sentence.split())}")

# 2
data = "red,green,blue"
parts = data.split(",")
print(" - ".join(parts))        # red - green - blue

# 3
for word in ["level", "python"]:
    if word == word[::-1]:
        print(f"{word}: Palindrome")
    else:
        print(f"{word}: Not a palindrome")
# level: Palindrome
# python: Not a palindrome
```

### 🏁 Week 3 wrap-up*"Is week aapne data ko GROUP karna seekha:*
- *Lists banana, index, slice (Class 21)*
- *List methods — add/remove/sort (Class 22)*
- *Nested lists — tables aur grids (Class 23)*
- *Tuples — locked records + unpacking (Class 24)*
- *Advanced strings — text master (Class 25)*

*Ab aap ek box mein bahut saara data rakh sakte ho aur usse khel sakte ho. Yeh agent ki memory ka foundation hai. Next week — dictionaries, jo bilkul LLM message ki shakal hain! Agli class mein milte hain!"*

### 📝 Weekend revision task
Ek program banao jo: ek list of student-tuples `[("Asha", 85), ("Rahul", 90)]` le, har ek ko print kare unpacking se, aur sabse zyada marks waale ka naam bataye. Bina notes ke karo.

---

## 🎤 Industry Interview Questions — Week 3

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between a list and a tuple, and when do you choose each?**

A list is mutable (you can add, remove, and change items) and is used for a collection that grows or changes. A tuple is immutable (fixed once created) and is used for a fixed record whose shape has meaning, like a coordinate `(x, y)` or a `(name, marks)` row. Because tuples are immutable and hashable, they can be used as dictionary keys or set members; lists cannot. Immutability also signals intent to other developers: "this should not change."

**Q2. Explain slicing, including negative indices and step. What does `s[::-1]` do?**

Slicing is `sequence[start:stop:step]`, returning a new sequence from `start` up to (but not including) `stop`. Omitted parts default to the beginning, the end, and step `1`. Negative indices count from the end (`s[-1]` is the last item). A negative step walks backwards, so `s[::-1]` reverses the whole sequence. Slicing never mutates the original — it produces a copy of that slice.

**Q3. What is the difference between a shallow copy and a deep copy for a nested list?**

`list.copy()` (or `list[:]`) makes a *shallow* copy: a new outer list, but the inner objects are still shared references. So mutating a nested element affects both copies. `copy.deepcopy()` recursively copies everything, so the new structure is fully independent. This matters whenever you have lists of lists (or lists of dicts) — for example duplicating an agent's message history before editing it.

**Q4. What is the difference between `append()`, `extend()`, and `+` on lists?**

`append(x)` adds `x` as a single element (so appending a list nests it). `extend(iterable)` adds each element of the iterable individually, growing the list in place. Both mutate the original list and return `None`. The `+` operator creates and returns a *new* list without changing the operands, which is cleaner functionally but uses more memory for large lists.

**Q5. Strings are immutable in Python — what does that mean in practice?**

You cannot change a character in place (`s[0] = "H"` raises an error). Every "modifying" method — `.upper()`, `.strip()`, `.replace()` — returns a *new* string and leaves the original untouched, so you must capture the result (`s = s.strip()`). A practical consequence: building a big string by repeated `+=` in a loop is inefficient (it creates a new string each time); use `"".join(list_of_parts)` instead.
