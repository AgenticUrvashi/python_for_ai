# WEEK 5 — Functions Core (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week se asli engineering shuru. Functions = code ke reusable blocks jise aap ek baar likho aur baar-baar use karo. Yeh SABSE important hai agentic AI ke liye, kyunki ek agent ka har 'tool' ek function hi hota hai. Is week ke end tak aap apna pehla tool likhne ke layak ho jaoge."*

---

## CLASS 31 — Defining & Calling Functions

*"Ab tak humne calculator, guessing game banaye. Par socho aapko 10 jagah area calculate karna hai — kya 10 baar formula likhoge? Nahi! Ek baar ek FUNCTION banao, phir bas naam se bula lo. 'Likho ek baar, use karo hazaar baar' — yahi functions ka motto hai."*

### 🎯 Today's goal
`def` se function banana, parameters dena, aur `return` se value wapas paana.

### 👨‍🏫 Concept 1 — function banana aur bulana

> **📖 Technical definition — Function:** A function is a named, reusable block of code defined with `def` that runs only when it is called. It can accept inputs, perform a task, and optionally send back a result.

```python
def greet():
    print("Hello! Welcome to Python")

greet()        # function ko 'call' (bulana) karna
greet()        # dobara bula sakte ho
```
Output:
```
Hello! Welcome to Python
Hello! Welcome to Python
```
*"`def` se function shuru hota hai, phir naam, phir `()`, phir `:`. Andar ka code (indented) tab tak nahi chalta jab tak aap function ko `greet()` se BULAO nahi. Banana aur bulana — do alag cheezein."*

### 👨‍🏫 Concept 2 — parameters (function ko input do)

> **📖 Technical definition — Parameter vs argument:** A parameter is a named variable listed in a function's definition that receives an input. An argument is the actual value supplied for that parameter when the function is called.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Asha")      # Hello, Asha!
greet("Rahul")     # Hello, Rahul!
```
*"`name` ek PARAMETER hai — ek box jo call ke time bhari jaati hai. Jo value aap bhejte ho (`"Asha"`) use ARGUMENT bolte hain. Ek function alag-alag inputs ke saath alag kaam karta hai."*

### 👨‍🏫 Concept 3 — `return` (value wapas bhejo) — sabse important

> **📖 Technical definition — `return`:** The `return` statement ends a function's execution and sends a value back to the caller, where it can be stored or reused. A function with no `return` (or a bare `return`) yields `None`. This differs from `print()`, which only displays text and returns nothing usable.

*"`print` sirf screen par dikhata hai. `return` value ko WAPAS bhejta hai taaki aap use aage istemaal kar sako. Yeh BAHUT bada difference hai."*
```python
def add(a, b):
    return a + b

result = add(5, 3)         # return ki gayi value 'result' mein aa gayi
print(result)              # 8
print(add(10, 20) + 100)   # 130  — return value ko aage use kiya
```
*"Dekho `add` ne kuch print nahi kiya — usne value RETURN ki, jise humne aage maths mein use kiya. Functions usually return karte hain, print nahi. Yeh professional soch hai."*

### 👨‍🏫 Concept 4 — return vs print (ek demo se clear)
```python
def add_print(a, b):
    print(a + b)           # sirf dikhata hai

def add_return(a, b):
    return a + b           # value deta hai

x = add_print(2, 3)        # screen par 5 dikha
print(x)                   # None  — kyunki return kuch nahi kiya!

y = add_return(2, 3)       # screen par kuch nahi
print(y)                   # 5     — value mili, use kar sakte ho
```
*"Yeh sabse bada beginner confusion hai. Yaad rakho: **`return` se value milti hai jise aage use kar sako; `print` sirf aankhon ke liye hai.** Tools ke liye HAMESHA `return`."*

### 💻 Demo — area function
```python
def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 3))      # 15
print(rectangle_area(10, 2))     # 20

# return value ko aage use karo
total = rectangle_area(4, 4) + rectangle_area(2, 3)
print(total)                     # 22
```

### ❌ Common mistakes
```python
def add(a, b):
    return a + b
add(2, 3)              # ❌ value return hui par kahin store/print nahi — kho gayi
print(add(2, 3))       # ✅ ab dikhega

def greet(name):
    print(f"Hi {name}")
greet()                # ❌ TypeError — 'name' argument missing
```

### 🔗 Agentic link
*"Yeh week ka core idea: **ek agent ka har tool ek function hai.** `get_weather(city)`, `calculator(expression)`, `search(query)` — sab functions jo input lete hain aur result RETURN karte hain. Aaj aapne tool banane ka pehla din shuru kiya."*

### ✍️ Homework
1. Ek function `square(n)` jo number ka square return kare.
2. Ek function `greet(name, city)` jo "Hi NAME from CITY" return kare (print nahi, return).
3. Ek function `bmi(weight, height)` jo BMI return kare (`weight / height**2`).

**Answers:**
```python
# 1
def square(n):
    return n ** 2
print(square(5))             # 25

# 2
def greet(name, city):
    return f"Hi {name} from {city}"
print(greet("Asha", "Mumbai"))    # Hi Asha from Mumbai

# 3
def bmi(weight, height):
    return weight / height ** 2
print(round(bmi(60, 1.7), 1))     # 20.8
```

### 🔗 Agli class
*"Agli class — functions ko aur flexible banayenge: default values aur keyword arguments. Yeh seedhe AI tool-calling se judta hai."*

---

## CLASS 32 — Defaults & Keyword Arguments

*"Pichli class mein function banaya. Aaj use SMART banayenge: kuch inputs optional honge (default values), aur hum inputs ko NAAM se de payenge — jo exactly LLMs tools ko call karne ke liye karte hain."*

### 🎯 Today's goal
Default parameter values, aur positional vs keyword arguments.

### 👨‍🏫 Concept 1 — default values (optional input)

> **📖 Technical definition — Default parameter value:** A default value is a value assigned to a parameter in the function definition. It is used automatically when the caller does not supply an argument for that parameter, making the parameter optional. Parameters with defaults must come after those without.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Asha"))              # Hello, Asha!   — default use hua
print(greet("Rahul", "Hi"))       # Hi, Rahul!     — humne diya toh woh use hua
```
*"`greeting="Hello"` ka matlab: agar koi value na de, toh 'Hello' use karo. Isse function flexible ho jaata hai — common case easy, special case bhi possible."*

### 👨‍🏫 ⚠️ Rule — defaults hamesha BAAD mein
```python
def f(a=1, b):     # ❌ SyntaxError — default wale parameter baad mein aane chahiye
    ...
def f(b, a=1):     # ✅ pehle bina-default, phir default wale
    ...
```

### 👨‍🏫 Concept 2 — positional vs keyword arguments

> **📖 Technical definition — Positional vs keyword arguments:** Positional arguments are matched to parameters by their order. Keyword arguments are matched by explicitly naming the parameter (`name=value`), so their order does not matter. In a call, positional arguments must appear before keyword arguments.

```python
def book_ticket(source, destination, seats):
    return f"{seats} seats from {source} to {destination}"

# positional — order se match
print(book_ticket("Mumbai", "Delhi", 2))

# keyword — naam se match (order matter nahi karta!)
print(book_ticket(destination="Delhi", source="Mumbai", seats=2))
```
*"Positional = position se value milti hai (pehli value pehle parameter ko). Keyword = aap naam likhte ho `seats=2`, toh order ki tension nahi. Keyword arguments code ko padhne mein bahut clear banate hain."*

### 👨‍🏫 Concept 3 — dono mix (positional pehle)
```python
def order(item, qty=1, size="medium"):
    return f"{qty} {size} {item}"

print(order("pizza"))                    # 1 medium pizza
print(order("pizza", 2))                 # 2 medium pizza
print(order("pizza", size="large"))      # 1 large pizza   — qty default, size keyword
print(order("coke", 3, "small"))         # 3 small coke
```
*"Rule: jab dono use karo, positional arguments pehle, keyword baad mein. `order("pizza", size="large")` — item positional, size keyword. Yeh super common hai."*

### 💻 Demo — flexible greeting tool
```python
def make_message(text, role="user"):
    return {"role": role, "content": text}

print(make_message("Hello"))                      # {'role': 'user', 'content': 'Hello'}
print(make_message("You are helpful", role="system"))
# {'role': 'system', 'content': 'You are helpful'}
```
*"Dekha? Yeh function ek LLM message banata hai (Week 4 wali dict shape!). `role` ka default 'user' hai, par system message ke liye hum `role="system"` de dete hain. Yeh real agent code hai."*

### ❌ Common mistakes
```python
def f(a, b=2, c):     # ❌ default ke baad bina-default nahi aa sakta
    ...

book_ticket(source="Mumbai", "Delhi", 2)   # ❌ keyword ke baad positional nahi
```

### 🔗 Agentic link
*"Yeh BAHUT important hai: **LLM tools ko unke ARGUMENT NAAM se call karta hai**, jaise `get_weather(city="Mumbai")`. Yeh exactly keyword arguments hain. Aur default values se tools ke optional settings handle hote hain (jaise `units="celsius"`). Aaj aapne tool-calling ki nayi nazdiki banai."*

### ✍️ Homework
1. `power(base, exp=2)` jo default square kare, par exp dene par woh power kare.
2. `intro(name, age, city="India")` banao; ek baar city ke saath, ek baar bina, call karo.
3. Ek function ko keyword arguments se call karke dikhao (order badal kar).

**Answers:**
```python
# 1
def power(base, exp=2):
    return base ** exp
print(power(5))          # 25
print(power(2, 3))       # 8

# 2
def intro(name, age, city="India"):
    return f"{name}, {age}, from {city}"
print(intro("Asha", 17))                # Asha, 17, from India
print(intro("Rahul", 18, "Delhi"))      # Rahul, 18, from Delhi

# 3
print(intro(age=20, name="Priya", city="Pune"))   # Priya, 20, from Pune
```

### 🔗 Agli class
*"Agli class — `*args` aur `**kwargs`: functions jo KOI BHI number of arguments le sakein. Thoda jadui lagta hai, par bahut kaam ka."*

---

## CLASS 33 — *args / **kwargs

*"Kabhi-kabhi humein nahi pata kitne inputs aayenge. Jaise `sum()` — 2 ya 10 ya 100 numbers. Iske liye Python deta hai `*args` (jitne marzi positional) aur `**kwargs` (jitne marzi keyword). Star (`*`) magic hai."*

### 🎯 Today's goal
`*args` se kai positional, aur `**kwargs` se kai keyword arguments lena.

### 👨‍🏫 Concept 1 — `*args` (jitne marzi values)

> **📖 Technical definition — `*args`:** A parameter written with a single asterisk collects any number of extra positional arguments into a tuple, letting a function accept a variable number of positional inputs.

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2))           # 3
print(total(1, 2, 3, 4, 5))  # 15
print(total())               # 0
```
*"`*numbers` saari di gayi values ko ek TUPLE mein ikattha kar leta hai. Andar `numbers` ek tuple ban jaata hai `(1,2,3,4,5)`. Naam `args` convention hai, par star (`*`) asli magic hai. Aap kitni bhi values bhejo, sab `numbers` mein aa jaati hain."*

### 👨‍🏫 Concept 2 — `**kwargs` (jitne marzi naam-wali values)

> **📖 Technical definition — `**kwargs`:** A parameter written with a double asterisk collects any number of extra keyword arguments into a dictionary, mapping each argument name to its value, so a function can accept a variable number of named inputs.

```python
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Asha", age=17, city="Mumbai")
```
Output:
```
name: Asha
age: 17
city: Mumbai
```
*"`**details` saare keyword arguments ko ek DICTIONARY mein ikattha karta hai. Andar `details` ek dict ban jaata hai. `*` tuple banata hai, `**` dict banata hai — yaad rakhne ka aasan tareeka."*

### 👨‍🏫 Concept 3 — sab ek saath (order yaad rakho)
```python
def describe(title, *items, **options):
    print(f"Title: {title}")
    print(f"Items: {items}")
    print(f"Options: {options}")

describe("Cart", "milk", "bread", discount=10, gift=True)
```
Output:
```
Title: Cart
Items: ('milk', 'bread')
Options: {'discount': 10, 'gift': True}
```
*"Order hamesha: normal parameters → `*args` → `**kwargs`. Yeh order Python ka rule hai."*

### 💻 Demo — average function
```python
def average(*nums):
    if len(nums) == 0:          # khaali call se bachao
        return 0
    return sum(nums) / len(nums)

print(average(10, 20, 30))      # 20.0
print(average(5))               # 5.0
print(average())                # 0
```

### ❌ Common mistakes
```python
def f(**kwargs, *args):   # ❌ galat order — *args pehle, **kwargs baad mein
    ...

def total(*numbers):
    return sum(number)    # ❌ NameError — variable 'numbers' hai, 'number' nahi
```

### 🔗 Agentic link
*"Agent frameworks tools ko 'wrap' karne ke liye `*args, **kwargs` use karte hain — taaki ek wrapper kisi bhi tool ko, kisi bhi arguments ke saath, call kar sake. Aur config ko pass-through karne mein `**kwargs` se settings aage bhej dete hain. Yeh flexible 'glue' code har framework mein hai."*

### ✍️ Homework
1. `multiply_all(*nums)` jo saare numbers ka product return kare.
2. `make_config(**settings)` jo saari settings ek dict ke roop mein print kare.
3. `greet_all(*names)` jo har naam ko "Hello NAME" print kare (loop se).

**Answers:**
```python
# 1
def multiply_all(*nums):
    result = 1
    for n in nums:
        result = result * n
    return result
print(multiply_all(2, 3, 4))     # 24

# 2
def make_config(**settings):
    print(settings)
make_config(theme="dark", size=12)   # {'theme': 'dark', 'size': 12}

# 3
def greet_all(*names):
    for name in names:
        print(f"Hello {name}")
greet_all("Asha", "Rahul", "Priya")
```

### 🔗 Agli class
*"Agli class — ek CHUPA hua bug jo har Python programmer ko ek baar zaroor pakadta hai: default value mein list dena. Aur use safely fix karna."*

---

## CLASS 34 — The Mutable-Default Trap & Sentinels

*"Aaj ka lesson chhota par BAHUT important hai — ek bug jo dikhta nahi par chupke se data corrupt karta hai. Jo engineer ise jaanta hai, woh ghante bachata hai. Yeh interview mein bhi poocha jaata hai."*

### 🎯 Today's goal
Mutable default argument trap samajhna, aur use `None`/sentinel se fix karna.

### 👨‍🏫 ⚠️ Concept 1 — the bug (default list)

> **📖 Technical definition — Mutable default argument:** A default argument value is created once, when the function is defined, and reused across all calls. If that default is a mutable object (like a list or dict), modifications persist between calls, causing shared-state bugs. The fix is to default to `None` and create a fresh object inside the function.

```python
def add_item(item, cart=[]):      # ❌ DANGER: default mein list
    cart.append(item)
    return cart

print(add_item("milk"))     # ['milk']            (theek lagta hai)
print(add_item("bread"))    # ['milk', 'bread']   😱 milk kahan se aaya??
print(add_item("eggs"))     # ['milk', 'bread', 'eggs']  😱😱
```
*"Aap soch rahe the har call ki nayi khaali cart milegi. Par NAHI! Woh default list SIRF EK BAAR banti hai (jab function define hota hai), aur har call uss SAME list ko use karti hai. Toh values jamti rehti hain. Yeh classic Python trap hai."*

### 👨‍🏫 Concept 2 — the fix (`None` use karo)
```python
def add_item(item, cart=None):    # ✅ default None
    if cart is None:
        cart = []                 # har call mein NAYI list
    cart.append(item)
    return cart

print(add_item("milk"))     # ['milk']
print(add_item("bread"))    # ['bread']   ✅ ab har call fresh
print(add_item("eggs"))     # ['eggs']    ✅
```
*"Rule (pathar par likh lo): **default value mein kabhi list/dict/set mat do.** Hamesha `None` do, aur function ke andar check karke nayi banao. Yaad rakho `is None` (Class 30 se) — yahi sahi check hai."*

### 👨‍🏫 Concept 3 — "diya hi nahi" vs "None diya" (sentinel idea)

> **📖 Technical definition — Sentinel:** A sentinel is a unique, purpose-built object (commonly created with `object()`) used as a default to represent "no value supplied." Because it is distinct from every other value, it lets a function distinguish an omitted argument from one explicitly passed as `None`.

*"Kabhi-kabhi `None` khud ek valid value hota hai, aur humein farak karna hai: 'user ne value DI HI NAHI' vs 'user ne jaan-boojh kar None diya'. Iske liye ek SENTINEL banate hain — ek special unique object jiska matlab 'kuch diya hi nahi'."*
```python
_MISSING = object()      # ek unique 'sentinel' — sirf 'not given' ka matlab

def update(value=_MISSING):
    if value is _MISSING:
        print("No value was given at all")
    elif value is None:
        print("User explicitly passed None")
    else:
        print(f"Got: {value}")

update()           # No value was given at all
update(None)       # User explicitly passed None
update(42)         # Got: 42
```
*"`object()` ek bilkul unique cheez banata hai jo kisi aur cheez ke barabar nahi. Isse hum 'omitted' aur 'None' ko alag bata sakte hain. Yeh standard, 100% reliable Python idiom hai — har bade codebase mein milega."*

> **Teacher accuracy note:** Sentinel ke liye `_MISSING = object()` waala pattern Python ki sabse safe aur sab jagah chalne wali technique hai. AI tool-params mein 'field bheja hi nahi' vs 'field None bheja' ka farak isi se karte hain.

### 💻 Demo — safe history appender
```python
def add_message(text, history=None):
    if history is None:
        history = []
    history.append({"role": "user", "content": text})
    return history

chat1 = add_message("Hi")
chat2 = add_message("Hello")         # alag conversation
print(chat1)     # [{'role': 'user', 'content': 'Hi'}]
print(chat2)     # [{'role': 'user', 'content': 'Hello'}]  ✅ alag-alag, no leak
```

### ❌ Common mistakes
```python
def f(items=[]):          # ❌ shared-state bug
    items.append(1)
    return items

def f(items=None):        # ✅ sahi
    if items is None:
        items = []
    ...
```

### 🔗 Agentic link
*"Yeh agents mein ek GHATAK bug hai: agar tool ka default `messages=[]` ho, toh do alag conversations galti se ek hi history share kar lenge — ek user ki baat doosre ko dikh sakti hai (privacy/correctness disaster). Aur sentinel se hum tool params mein 'omitted vs None' ka farak karte hain. Yeh bilkul professional skill hai."*

### ✍️ Homework
1. `add_to_list` likho jo default `None` use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.
2. Jaan-boojh kar `def f(x=[])` waala bug banao, 3 call karke bug dikhao.
3. Ek sentinel `_MISSING` banake ek function likho jo "given vs not given" bataye.

**Answers:**
```python
# 1
def add_to_list(item, data=None):
    if data is None:
        data = []
    data.append(item)
    return data
print(add_to_list("a"))    # ['a']
print(add_to_list("b"))    # ['b']
print(add_to_list("c"))    # ['c']

# 2
def buggy(x=[]):
    x.append(1)
    return x
print(buggy())    # [1]
print(buggy())    # [1, 1]  (bug!)

# 3
_MISSING = object()
def check(val=_MISSING):
    return "not given" if val is _MISSING else f"given: {val}"
print(check())       # not given
print(check(5))      # given: 5
```

### 🔗 Agli class
*"Agli class — week ka review aur practice. Hum apne purane calculator/games ko functions mein refactor karenge — yahi real engineering hai."*

---

## CLASS 35 — Review & Practice

*"Aaj koi naya concept nahi — aaj hum is week ka sab JODENGE aur apne purane code ko behtar banayenge (refactor). Pehle se kaam karta code lekar use saaf, reusable functions mein todna — yeh asli developer ka roz ka kaam hai."*

### 🎯 Today's goal
Functions ke saare concepts pakke karna; purana code functions mein refactor karna.

### 👨‍🏫 Quick recap (poora week ek nazar mein)
```python
# 1) basic function with return
def add(a, b):
    return a + b

# 2) default values
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}"

# 3) *args / **kwargs
def total(*nums):
    return sum(nums)

# 4) safe default (no mutable!)
def collect(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```
*"Yeh 4 patterns aapko function ke 90% cases ke liye taiyar karte hain. Inhe dohrao jab tak bina soche likh na pao."*

### 💻 Demo 1 — calculator ko functions mein refactor

> **📖 Technical definition — Refactoring:** Refactoring is the process of restructuring existing code to improve its readability, organisation, and reusability without changing its external behaviour or output.

*"Yaad hai Week 2 ka menu calculator? Tab sab ek jagah tha. Ab har operation ek function:"*

> **⚠️ Note:** `match/case` ke liye **Python 3.10+** chahiye. Agar aapka Python purana hai, toh `calculate` ke andar `if op == "+": ... elif op == "-": ...` use karo — logic bilkul same rahega.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(a, b, op):
    match op:
        case "+": return add(a, b)
        case "-": return subtract(a, b)
        case "*": return multiply(a, b)
        case "/": return divide(a, b)
        case _:   return "Unknown operation"

print(calculate(10, 5, "+"))     # 15
print(calculate(10, 0, "/"))     # Cannot divide by zero
print(calculate(6, 7, "*"))      # 42
```
*"Dekho kitna saaf ho gaya! Har operation alag, test karne mein aasan, dobara use ho sakta hai. Yeh exactly aap agent tools ke liye karoge — har tool ek alag function."*

### 💻 Demo 2 — grade function
```python
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

# ab list of students par easily use karo
students = {"Asha": 92, "Rahul": 70, "Priya": 81}
for name, marks in students.items():
    print(f"{name}: Grade {get_grade(marks)}")
```
Output:
```
Asha: Grade A
Rahul: Grade C
Priya: Grade B
```
*"Ek function banaya `get_grade`, aur use har student par laga diya. Yeh 'likho ek baar, use karo baar-baar' ki asli taakat hai."*

### ❌ Common mistakes (week ke top traps)
```python
# 1) return bhool jaana
def add(a, b):
    a + b              # ❌ return nahi kiya → function None deta hai

# 2) mutable default
def f(items=[]):       # ❌ shared bug

# 3) print vs return confusion
x = print("hi")        # x ab None hai, "hi" nahi
```

### 🔗 Agentic link
*"Aaj aapne jo kiya — kaam karta code ko saaf functions mein todna — yahi pehla kadam hai apni khud ki 'tools library' banane ka. Next week hum in functions ko typed aur documented banayenge (taaki LLM unhe samajh sake), aur alag file (module) mein organize karenge. Aap fast aage badh rahe ho!"*

### ✍️ Homework
1. Apne purane temperature converter (Week 1) ko ek function `celsius_to_f(c)` mein badlo.
2. Ek function `is_even(n)` jo True/False return kare; 5 numbers par test karo.
3. Number guessing game ke 'compare' part ko ek function `check_guess(guess, secret)` mein nikaalo jo "low"/"high"/"correct" return kare.

**Answers:**
```python
# 1
def celsius_to_f(c):
    return (c * 9 / 5) + 32
print(celsius_to_f(37))      # 98.6

# 2
def is_even(n):
    return n % 2 == 0
for x in [2, 5, 8, 11, 14]:
    print(x, is_even(x))

# 3
def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"
print(check_guess(30, 50))   # low
print(check_guess(70, 50))   # high
print(check_guess(50, 50))   # correct
```

### 🏁 Week 5 wrap-up

*"Yeh week aapne asli engineering shuru ki:*
- *Functions banana + return (Class 31)*
- *Default + keyword arguments — tool-calling ki shakal (Class 32)*
- *`*args`/`**kwargs` — flexible functions (Class 33)*
- *Mutable-default trap + sentinels — ek chupa bug (Class 34)*
- *Refactoring — code ko saaf functions mein todna (Class 35)*

*Ab aap reusable code blocks likh sakte ho — jo har agent tool ka aadhar hai. Next week in functions ko TYPED, DOCUMENTED, aur MODULAR banayenge — taaki LLM tak inhe samajh sake. Bahut badhiya, agli class mein milte hain!"*

### 📝 Weekend revision task
Apne saare Week 1–2 ke programs (converter, calculator, grade-checker) ko functions mein refactor karke ek file `my_tools.py` mein rakho. Yeh aapki pehli tools-library ki shururaat hai!

---

## 🎤 Industry Interview Questions — Week 5

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between `return` and `print` in a function?**

`print` sends text to the console for a human to read; it does not give the value back to the calling code. `return` hands a value back to the caller so it can be stored, reused, or passed on. A function that only `print`s returns `None`, so `total = add(2, 3)` would set `total` to `None` if `add` used `print` instead of `return`. Real, reusable functions (and every agent "tool") must `return` their result.

**Q2. Why must parameters with default values come last, and what is the mutable default argument trap?**

Defaults must follow non-default parameters because otherwise Python can't tell which positional argument fills which parameter. The famous trap is using a mutable default like `def add_item(x, items=[])`: that list is created *once* when the function is defined and shared across all calls, so it accumulates values between calls. The fix is the sentinel pattern: `def add_item(x, items=None): items = [] if items is None else items`.

**Q3. What do `*args` and `**kwargs` do, and what order must parameters be in?**

`*args` collects any extra *positional* arguments into a tuple; `**kwargs` collects any extra *keyword* arguments into a dict. This lets a function accept a variable number of inputs. The required order is: normal/positional parameters, then `*args`, then keyword-only parameters, then `**kwargs`. They're heavily used for wrappers and decorators that must forward arbitrary arguments.

**Q4. What is the difference between positional and keyword arguments, and why prefer keyword arguments?**

Positional arguments are matched by their position (`greet("Asha", 17)`); keyword arguments are matched by name (`greet(name="Asha", age=17)`). Keyword arguments are more readable, order-independent, and self-documenting — especially with boolean flags where `send(retry=True)` is far clearer than `send(True)`. In production APIs, keyword arguments also make it safe to add or reorder parameters later.

**Q5. How are arguments passed in Python — by value or by reference?**

Python uses "pass by object reference" (sometimes called pass-by-assignment): the function receives a reference to the same object. If the object is immutable (int, str, tuple), it appears to behave like pass-by-value — reassigning inside the function doesn't affect the caller. If the object is mutable (list, dict), mutating it *in place* (e.g. `lst.append(x)`) is visible to the caller, while rebinding the name (`lst = [...]`) is not. Knowing this prevents accidental shared-state bugs.
