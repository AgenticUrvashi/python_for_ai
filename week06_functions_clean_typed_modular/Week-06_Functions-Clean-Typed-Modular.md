# WEEK 6 — Functions: Clean, Typed & Modular (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Pichle week functions banaye. Is week unhe PROFESSIONAL banayenge: type hints (taaki galtiyां pakdi jayein aur LLM tools samajh sake), docstrings (tools ka 'manual'), aur modules (code ko files mein organize karna). Week ke end tak aapke paas ek asli tools.py module hoga."*

---

## CLASS 36 — Scope & Closures

*"Ek sawaal: agar function ke ANDAR ek variable banao, kya woh bahar dikhega? Aaj seekhenge ki variables KAHAN 'rehte' hain (scope), aur ek cool trick jisse ek function doosre function ko 'yaad' rakhta hai (closure)."*

### 🎯 Today's goal
Local vs global scope samajhna, aur closures banana.

### 👨‍🏫 Concept 1 — local scope (function ke andar ka rehta hai andar)

> **📖 Technical definition — Scope:** Scope is the region of a program where a name is accessible. A local variable exists only inside the function that creates it, whereas a global variable is defined at the top level of a module and is readable throughout that module.

```python
def my_function():
    x = 10              # 'x' sirf is function ke andar zinda hai
    print(x)

my_function()           # 10
print(x)                # ❌ NameError — 'x' bahar exist nahi karta
```
*"Function ke andar bana variable 'local' hota hai — woh sirf us function ke andar zinda rehta hai, function khatam = variable gayab. Yeh GOOD hai: har function apni alag duniya mein kaam karta hai, ek doosre ko galti se nahi bigaadte."*

### 👨‍🏫 Concept 2 — global scope (bahar wala)
```python
greeting = "Hello"      # global — file mein har jagah dikhta hai

def greet():
    print(greeting)     # bahar wale ko PADH sakte hain

greet()                 # Hello
```
*"Bahar bane variable (global) ko function PADH sakta hai. Par usse BADALNA seedhe allowed nahi:"*
```python
count = 0
def increment():
    count = count + 1   # ❌ error — andar se global ko badalne ki koshish
```

### 👨‍🏫 Concept 3 — `global` keyword (use mat karo, par jaano)
```python
count = 0
def increment():
    global count        # "main bahar wale count ko badal raha hoon"
    count = count + 1

increment()
print(count)            # 1
```
*"`global` chal toh jaata hai, par PROFESSIONALS isse avoid karte hain — kyunki global variables ko kahin se bhi koi badal sakta hai, jisse bugs dhoondhna mushkil ho jaata hai. Behtar tareeka: value return karo aur dobara assign karo. Industry rule: input parameters se lo, return se do — global se nahi."*

### 👨‍🏫 Concept 4 — closures (function jo state yaad rakhe)

> **📖 Technical definition — Closure:** A closure is an inner function that remembers and can access variables from the enclosing function's scope even after the outer function has finished running. It lets a function carry configured state along with it.

*"Ek function doosre function ke andar bana sakte ho, aur andar wala function bahar wale ke variables ko 'yaad' rakhta hai — bhale bahar wala khatam ho jaaye. Ise CLOSURE bolte hain."*
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n        # 'n' ko yaad rakhta hai
    return multiplier        # andar wala function return karo

double = make_multiplier(2)  # n=2 yaad ho gaya
triple = make_multiplier(3)  # n=3 yaad ho gaya

print(double(5))             # 10   (5 * 2)
print(triple(5))             # 15   (5 * 3)
```
*"`make_multiplier(2)` ne ek function banaya jo hamesha 2 se multiply karta hai. `n` us function ke andar 'band' ho gaya — isiliye 'closure'. Yeh advanced lagta hai par bahut powerful hai, aur next week decorators ki neev hai."*

### ❌ Common mistakes
```python
def f():
    y = 5
print(y)            # ❌ NameError — y local tha, bahar nahi hai

count = 0
def add():
    count += 1      # ❌ UnboundLocalError — global keyword ke bina badalne ki koshish
```

### 🔗 Agentic link
*"Closures 'tool factories' banane mein use hote hain — ek function jo configured tools banaye (jaise `make_api_tool(api_key)` jo us key ko yaad rakhe). Aur scope samajhna zaroori hai taaki agent ka state galti se leak na ho. Next week decorators (closures par bane) se tools ko retry/logging dete hain."*

### ✍️ Homework
1. Ek function ke andar variable banao, bahar print karke error dekho.
2. `make_adder(n)` closure banao jo `n` add kare; `add5 = make_adder(5)` test karo.
3. `make_counter()` banao jo har call par badhta number de (closure se).

**Answers:**
```python
# 2
def make_adder(n):
    def adder(x):
        return x + n
    return adder
add5 = make_adder(5)
print(add5(10))         # 15

# 3
def make_counter():
    count = 0
    def counter():
        nonlocal count      # andar wale function ka outer-local badalne ke liye
        count = count + 1
        return count
    return counter
c = make_counter()
print(c())              # 1
print(c())              # 2
print(c())              # 3
```
*"`nonlocal` `global` jaisा hai par 'outer function' ke variable ke liye — closures mein state badalne ka sahi tareeka."*

### 🔗 Agli class
*"Agli class — recursion: ek function jo KHUD ko bulata hai. Dimaag thoda ghoomega, par bahut elegant hai."*

---

## CLASS 37 — Recursion

*"Aaj ek mind-bending idea: ek function jo APNE AAP ko call karta hai. Soch lo do aamne-saamne lage sheeshe — ek ke andar doosra, anant tak. Programming mein ise RECURSION bolte hain, aur yeh nested cheezein (jaise folders ke andar folders) handle karne ke liye perfect hai."*

### 🎯 Today's goal
Recursion samajhna: base case + recursive case.

### 👨‍🏫 Concept 1 — recursion ke 2 zaroori hisse

> **📖 Technical definition — Recursion:** Recursion is a technique in which a function solves a problem by calling itself on a smaller version of that problem. It requires a base case that stops the calls and a recursive case that reduces the problem toward the base case.

*"Har recursive function ko DO cheezein chahiye, warna woh hamesha chalta rahega (infinite):"*
1. **Base case** — woh point jahan rukna hai (no more calling).
2. **Recursive case** — function khud ko ek CHHOTI problem ke saath bulata hai.
```python
def countdown(n):
    if n == 0:              # base case — rukne ka point
        print("Done!")
        return
    print(n)
    countdown(n - 1)        # recursive case — chhoti problem (n-1)

countdown(3)
```
Output:
```
3
2
1
Done!
```
*"Dekho: `countdown(3)` print karta hai 3, phir `countdown(2)` bulata hai, jo 2 print karke `countdown(1)`... jab tak n=0 (base case) par ruk na jaye. Base case sabse zaroori hai — bina iske infinite loop."*

### 👨‍🏫 Concept 2 — factorial (classic example)
*"Factorial: 5! = 5 × 4 × 3 × 2 × 1. Recursion se sundar dikhta hai:"*
```python
def factorial(n):
    if n <= 1:              # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))        # 120   (5 * 4 * 3 * 2 * 1)
```
*"Socho: `factorial(5)` = 5 × `factorial(4)` = 5 × 4 × `factorial(3)`... aakhir mein 5×4×3×2×1 = 120. Har call problem ko chhota karti hai jab tak base case na aaye."*

### 👨‍🏫 Concept 3 — nested data par recursion (asli use)
```python
def sum_nested(data):
    total = 0
    for item in data:
        if isinstance(item, list):       # agar item khud ek list hai
            total = total + sum_nested(item)   # us list par dobara chalo
        else:
            total = total + item
    return total

print(sum_nested([1, 2, [3, 4, [5, 6]], 7]))    # 28
```
*"`isinstance(item, list)` check karta hai item list hai ya nahi. Agar list hai, hum usi function se uske andar ja kar sum karte hain. Yeh recursion ka asli faayda hai — kitni bhi gehri nesting ho, sambhal leta hai."*

### 👨‍🏫 ⚠️ Concept 4 — kab recursion NAHI use karein
*"Recursion elegant hai par har baar best nahi. Bahut gehri recursion 'RecursionError' de sakti hai (Python ki limit hoti hai, default ~1000 calls). Simple repeat ke liye `for`/`while` loop hi behtar aur tez hota hai. Recursion tab use karo jab data NESTED ho (trees, folders, nested JSON)."*

### ❌ Common mistakes
```python
def bad(n):
    return n * bad(n - 1)   # ❌ base case nahi → RecursionError (infinite)

def factorial(n):
    return n * factorial(n - 1)   # ❌ base case missing — kabhi rukega nahi
```

### 🔗 Agentic link
*"Agents aksar gehre NESTED data se deal karte hain — ek tool ka result jisme aur tool-calls hain, ya nested JSON jisme objects ke andar objects. Recursion se aise structures ko saaf-saaf 'walk' (traverse) karte hain. Yeh nested tool-outputs samajhne mein kaam aata hai."*

### ✍️ Homework
1. Recursion se 5 se 1 tak countdown karo.
2. Recursion se factorial(6) nikaalo.
3. Recursion se ek list `[1,2,3,4,5]` ka sum nikaalo (loop use NA karo).

**Answers:**
```python
# 1
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

# 2
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(6))      # 720

# 3
def list_sum(items):
    if len(items) == 0:
        return 0
    return items[0] + list_sum(items[1:])   # pehla + baaki ka sum
print(list_sum([1, 2, 3, 4, 5]))   # 15
```

### 🔗 Agli class
*"Agli class — docstrings aur type hints: apne functions ko self-explanatory aur typed banana. Yeh AI tools ke liye NON-NEGOTIABLE hai."*

---

## CLASS 38 — Docstrings & Type Hints

*"Aaj ka lesson agentic AI ke liye SABSE important hai is poore week ka. Kyun? Kyunki LLM aapke function ka DOCSTRING padh kar samajhta hai ki tool kya karta hai, aur TYPE HINTS se samajhta hai kaunse arguments chahiye. Bina inke, aapka function ek achha agent-tool nahi ban sakta."*

### 🎯 Today's goal
Type hints (`a: int -> int`) aur docstrings (`"""..."""`) likhna.

### 👨‍🏫 Concept 1 — type hints (kis type ka data?)

> **📖 Technical definition — Type hint:** A type hint is an optional annotation that declares the expected type of a parameter, variable, or return value. Python does not enforce it at runtime, but it documents intent and enables tools (and language models) to check and understand the code.

*"Type hint batata hai ek parameter aur return KIS type ka hona chahiye. Yeh code ko khud-documenting banata hai aur galtiyां pakadne mein madad karta hai."*
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))        # 8
```
*"Padho: `a: int` = 'a ek int hona chahiye'. `-> int` = 'yeh function ek int return karta hai'. Dhyaan: Python inhe FORCE nahi karta (galat type bhejoge toh crash nahi hoga), par yeh dusre developers (aur tools jaise mypy, aur LLMs) ko batata hai kya expected hai."*

**Common types:**
```python
def greet(name: str) -> str:
    return f"Hi {name}"

def average(nums: list[int]) -> float:
    return sum(nums) / len(nums)

def make_user(name: str, age: int) -> dict:
    return {"name": name, "age": age}

def is_adult(age: int) -> bool:
    return age >= 18
```

### 👨‍🏫 Concept 2 — docstrings (function ka manual)

> **📖 Technical definition — Docstring:** A docstring is a string literal placed as the first statement inside a function, class, or module. It documents what the object does and is stored on the object (accessible via `__doc__` or `help()`), so it can be read by developers and tools at runtime.

*"Docstring ek triple-quote string hai function ki PEHLI line par. Yeh batata hai function KYA karta hai. Yeh sirf comment nahi — Python ise yaad rakhta hai aur tools ise padh sakte hain."*
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area (length * width).
    """
    return length * width

print(calculate_area.__doc__)    # Python docstring ko store karta hai
help(calculate_area)             # poora manual dikhata hai
```
*"Format: ek line summary, phir Args (har parameter), phir Returns. Yeh 'Google style' hai — industry mein bahut common."*

### 👨‍🏫 Concept 3 — dono saath (professional function)
*"Ab Concept 1 (type hints) aur Concept 2 (docstring) ko EK saath lagao — yahi ek professional function ka asli roop hai."*
```python
def word_count(text: str) -> int:
    """Count the number of words in a text.

    Args:
        text: The input string to count words in.

    Returns:
        The number of words (separated by spaces).
    """
    return len(text.split())

print(word_count("I love Python"))    # 3
```
*"Yeh ek PERFECT agent-tool hai: clear naam, type hints, aur ek docstring jo LLM ko batata hai kab aur kaise use karein. Ab se aapka HAR function aisa dikhna chahiye."*

### 💻 Demo — refactor with types + docs
```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        Temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(37))    # 98.6
```

### ❌ Common mistakes
```python
# docstring ko comment ki tarah likhna (galat jagah)
def f(x):
    # this counts words   ❌ yeh comment hai, docstring nahi
    return len(x.split())

# sahi: function ke ANDAR pehli line par """..."""
def f(x: str) -> int:
    """Count words."""    # ✅ docstring
    return len(x.split())
```

### 🔗 Agentic link
*"Yeh literally agent-tool banane ka core hai: jab aap LLM ko ek tool dete ho, framework aapke function ka NAAM, TYPE HINTS, aur DOCSTRING se ek 'tool schema' banata hai jo LLM padhta hai. Achha docstring = LLM tool ko sahi use karega. Bura/missing docstring = LLM confuse. Isiliye yeh non-negotiable hai. (Week 17 mein yeh schema khud banayenge!)"*

### ✍️ Homework
Apne `my_tools.py` (Week 5) ke 3 functions mein type hints + Google-style docstrings add karo.

**Sample answer:**
```python
def square(n: int) -> int:
    """Return the square of a number.

    Args:
        n: The number to square.

    Returns:
        n multiplied by itself.
    """
    return n * n

def greet(name: str, greeting: str = "Hi") -> str:
    """Build a greeting message.

    Args:
        name: Person's name.
        greeting: The greeting word (default "Hi").

    Returns:
        A full greeting string.
    """
    return f"{greeting}, {name}!"
```

### 🔗 Agli class
*"Agli class — lambda, map, filter: chhote one-line functions aur unka data par jaadui istemaal."*

---

## CLASS 39 — lambda, map & filter

*"Kabhi-kabhi humein ek chhota, one-time function chahiye — itna chhota ki use naam dena bhi zyada lagta hai. Iske liye Python deta hai `lambda`. Aur `map`/`filter` se hum poori list par ek function chala sakte hain. Aapne `lambda` Week 4 mein sorting mein dekha tha — aaj poora samajhenge."*

### 🎯 Today's goal
`lambda`, `map()`, aur `filter()` use karna.

### 👨‍🏫 Concept 1 — lambda (mini one-line function)

> **📖 Technical definition — Lambda:** A lambda is a small, anonymous function defined in a single expression. It takes arguments and returns the value of that expression automatically, without a name or an explicit `return` statement.

```python
# normal function
def square(x):
    return x ** 2

# wahi cheez lambda se
square = lambda x: x ** 2

print(square(5))        # 25
```
*"`lambda x: x ** 2` ka matlab: 'ek function jo x leta hai aur x**2 return karta hai.' Koi `def`, koi naam, koi `return` keyword nahi — bas ek line. Lambda chhote, one-time kaam ke liye hai. Bada logic ho toh normal `def` use karo."*

### 👨‍🏫 Concept 2 — `map()` (har item par function lagao)

> **📖 Technical definition — `map()` and `filter()`:** `map()` applies a given function to every item of an iterable and yields the transformed results. `filter()` keeps only the items for which a given function returns a truthy value. Both return lazy iterators, so wrap them in `list()` to see the values.

```python
nums = [1, 2, 3, 4]

squared = list(map(lambda x: x ** 2, nums))
print(squared)          # [1, 4, 9, 16]
```
*"`map(function, list)` us function ko list ke HAR item par lagata hai. (Yaad rakho `list(...)` lagana padta hai result dekhne ke liye.) Yeh ek comprehension `[x**2 for x in nums]` jaisा hi kaam hai — dono theek hain, comprehension aksar zyada padhne layak hota hai."*

### 👨‍🏫 Concept 3 — `filter()` (sirf woh items jo pass karein)
```python
nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)            # [2, 4, 6]
```
*"`filter(function, list)` sirf woh items rakhta hai jinpar function True dे. Yahan even numbers bache. Yeh `[x for x in nums if x % 2 == 0]` jaisा hi hai."*

### 👨‍🏫 Concept 4 — functions ko argument ki tarah pass karna
*"Bada idea: Python mein function bhi ek VALUE hai — use variable mein rakh sakte ho, ya doosre function ko de sakte ho."*
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 5))    # 50
print(apply(len, "hello"))           # 5   — built-in function bhi pass kar sakte ho
```
*"Yeh 'function ko function mein bhejna' agent pipelines mein bahut kaam aata hai — jaise har result par koi processing function lagana."*

### 💻 Demo — sorting with lambda (Week 4 ka connect)
```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78},
]

# marks ke hisaab se (lambda key)
top = sorted(students, key=lambda s: s["marks"], reverse=True)
print(top[0]["name"])    # Rahul

# sirf 80+ waale (filter)
high = list(filter(lambda s: s["marks"] >= 80, students))
print([s["name"] for s in high])    # ['Asha', 'Rahul']
```

### ❌ Common mistakes
```python
result = map(lambda x: x*2, [1,2,3])
print(result)           # ❌ <map object ...> — list() lagana bhool gaye
print(list(result))     # ✅ [2, 4, 6]

# lambda mein lambा logic ghusaana — padhna mushkil
f = lambda x: (x*2 if x > 0 else -x) + (x**2)   # ❌ ab normal def behtar hai
```

### 🔗 Agentic link
*"`sorted(key=lambda ...)` se hum search/retrieval results ko relevance-score se rank karte hain. `filter` se kam-confidence results hata dete hain. Aur 'functions as arguments' wala idea har pipeline mein hai — jaise har tool-output par ek post-processor function lagana."*

### ✍️ Homework
1. `map` + lambda se `[1,2,3,4]` ke har number ka cube banao.
2. `filter` + lambda se `[3,8,1,9,4]` mein se sirf 5 se bade rakho.
3. Words ki list `["hi","hello","hey","welcome"]` mein se sirf 4+ letter waale `filter` se rakho.

**Answers:**
```python
# 1
print(list(map(lambda x: x ** 3, [1, 2, 3, 4])))     # [1, 8, 27, 64]

# 2
print(list(filter(lambda x: x > 5, [3, 8, 1, 9, 4]))) # [8, 9]

# 3
words = ["hi", "hello", "hey", "welcome"]
print(list(filter(lambda w: len(w) >= 4, words)))     # ['hello', 'welcome']
```

### 🔗 Agli class
*"Agli class — week ka finale: code ko alag FILES (modules) mein todna aur import karna, plus `pip` se packages install karna. Phir hum apna pehla real tools-module banayenge!"*

---

## CLASS 40 — Modules & pip (Project Class)

*"Ab tak sab ek file mein tha. Par real projects mein code KAI files mein bata hota hai — har file ek kaam. Aaj hum code ko 'modules' mein todna seekhenge, ek doosre se import karna, aur `pip` se duniya bhar ke ready-made code install karna. Phir apna pehla tools-module banayenge."*

### 🎯 Today's goal
`import`, apna module banana, `if __name__ == "__main__"`, aur `pip` basics.

### 👨‍🏫 Concept 1 — built-in modules import karna

> **📖 Technical definition — Module and `import`:** A module is a single `.py` file containing reusable Python code (functions, classes, variables). The `import` statement loads a module so its contents can be used in another file, keeping code organised across multiple files.

*"Python ke saath bahut saare ready-made 'modules' aate hain. `import` se unhe use karte hain."*
```python
import math
print(math.sqrt(16))        # 4.0
print(math.pi)              # 3.141592653589793

import random
print(random.randint(1, 6)) # ek dice roll (1-6)

from datetime import datetime
print(datetime.now())       # abhi ki date aur time
```
*"`import math` poora module laata hai (`math.sqrt`). `from datetime import datetime` sirf ek cheez laata hai (seedhe `datetime`). Dono theek hain."*

### 👨‍🏫 Concept 2 — apna module banao
*"Koi bhi `.py` file ek module hai! Ek file ke functions doosri file mein use kar sakte ho."*

**File 1: `tools.py`**
```python
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"
```

**File 2: `main.py`** (same folder mein)
```python
import tools

print(tools.add(5, 3))          # 8
print(tools.greet("Asha"))      # Hello, Asha!

# ya sirf zaroori cheezein import karo:
from tools import add
print(add(10, 20))              # 30
```
*"`import tools` aapki `tools.py` file ke functions le aata hai. Yeh code ko organized rakhta hai — ek file tools ke liye, ek main program ke liye."*

### 👨‍🏫 Concept 3 — `if __name__ == "__main__":`

> **📖 Technical definition — `if __name__ == "__main__"`:** Python sets a module's `__name__` to `"__main__"` when it is run directly, and to the module's name when it is imported. Guarding code with this check makes that code run only on direct execution, not when the file is imported elsewhere.

*"Yeh ajeeb dikhne wali line bahut important hai. Yeh ensure karti hai ki kuch code SIRF tab chale jab file SEEDHE run ho, IMPORT hone par nahi."*
```python
# tools.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    # yeh sirf tab chalega jab aap 'python tools.py' karo
    # 'import tools' karne par yeh NAHI chalega
    print("Testing add:", add(2, 3))
```
*"Soch lo: jab aap `python tools.py` chalate ho, Python `__name__` ko `"__main__"` set karta hai, toh test code chalta hai. Par jab koi `import tools` karta hai, `__name__` `"tools"` hota hai, toh test code skip ho jaata hai. Isse aap apni file ko test bhi kar sakte ho AUR import bhi — bina test code dusron ko pareshan kiye."*

### 👨‍🏫 Concept 4 — `pip` (duniya bhar ka code install karo)

> **📖 Technical definition — `pip`:** `pip` is Python's package installer. It downloads and installs third-party packages (and their dependencies) from the Python Package Index, making external, ready-made code available to `import` in your project.

*"`pip` Python ka package installer hai. Internet par lakhon ready-made packages hain. Terminal mein:"*
```bash
pip install requests
```
*"Yeh `requests` package install karta hai (web se data laane ke liye — Week 15 mein use karenge). Install ke baad use kar sakte ho:"*
```python
import requests       # ab yeh available hai
```
*"⚠️ Note: hum proper way (virtual environments) Week 12 mein seekhenge. Abhi bas concept samjho ki pip se bahar ka code aata hai."*

### 🛠️ Mini Project — `tools.py` module (pre-agent tool library!)
*"Yeh aapki pehli asli tools-library hai — typed, documented functions ek alag file mein. Bilkul wahi shakal jo agent tools ki hoti hai."*

**File: `tools.py`**
```python
from datetime import datetime


def add(a: float, b: float) -> float:
    """Add two numbers and return the result.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def get_current_time() -> str:
    """Return the current date and time as a string.

    Returns:
        Current time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def word_count(text: str) -> int:
    """Count the number of words in a text.

    Args:
        text: The input string.

    Returns:
        Number of words separated by spaces.
    """
    return len(text.split())


if __name__ == "__main__":
    # quick self-test (sirf seedhe run karne par)
    print(add(2, 3))                  # 5
    print(get_current_time())
    print(word_count("hello world"))  # 2
```

**File: `main.py`**
```python
from tools import add, get_current_time, word_count

print("Sum:", add(10, 5))
print("Time:", get_current_time())
print("Words:", word_count("Python is awesome"))
```
*"Run karo `python main.py`. Aapne abhi ek module banaya, import kiya, aur use kiya — bilkul ek real engineer ki tarah. Yeh teen functions Week 17 mein asli agent tools ban jayenge!"*

### ❌ Common mistakes
```python
import tools
print(add(2, 3))        # ❌ NameError — 'tools.add' ya 'from tools import add' chahiye

# file ka naam galat — module ka naam = file ka naam (bina .py)
import tool             # ❌ ModuleNotFoundError agar file 'tools.py' hai
```

### 🔗 Agentic link
*"Yeh project literally aapki pre-agent tool library hai. Real agents mein, tools aise hi ek alag file/module mein rehte hain — har ek typed aur documented. Aapka `tools.py` woh foundation hai jis par hum poore course mein build karenge. Yeh ek bahut bada milestone hai!"*

### ✍️ Homework
1. `tools.py` mein ek aur function add karo: `is_palindrome(text: str) -> bool` (typed + docstring).
2. `main.py` se use import karke 2 words par test karo.
3. `math` module use karke ek `circle_area(radius)` function `tools.py` mein add karo.

**Answers:**
```python
# tools.py mein add karo:
import math

def is_palindrome(text: str) -> bool:
    """Check if a text reads the same forwards and backwards."""
    return text == text[::-1]

def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius."""
    return math.pi * radius ** 2

# main.py:
from tools import is_palindrome, circle_area
print(is_palindrome("madam"))     # True
print(is_palindrome("python"))    # False
print(round(circle_area(7), 2))   # 153.94
```

### 🏁 Week 6 wrap-up*"Yeh week aapne functions ko PROFESSIONAL banaya:*
- *Scope & closures — variables kahan rehte hain (Class 36)*
- *Recursion — khud ko bulane wale functions (Class 37)*
- *Type hints & docstrings — AI tools ke liye must (Class 38)*
- *lambda, map, filter — chhote functions ka jaadu (Class 39)*
- *Modules & pip + tools.py module (Class 40)*

*Ab aapke paas ek asli, typed, documented tools-module hai! Yeh ek HUGE milestone hai. Ab tak aapne poora 'procedural Python' cover kar liya. Next week ek nayi duniya — OBJECT-ORIENTED PROGRAMMING (OOP), jahan agents aur tools 'objects' bante hain. Thoda dimaag lagega, par hum slow chalenge. Shabaash!"*

### 📝 Weekend revision task
Apne `tools.py` ko 5 functions tak le jao, har ek type hints + docstring ke saath, aur `if __name__ == "__main__"` block mein har ek ka ek self-test likho. Yeh aapka portfolio piece ban raha hai!

---

## 🎤 Industry Interview Questions — Week 6

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. Explain Python's LEGB scope rule and what the `global` keyword does.**

When you use a name, Python looks it up in this order: **L**ocal (inside the current function), **E**nclosing (any outer functions), **G**lobal (module level), then **B**uilt-in. The first match wins. By default, assigning to a name inside a function creates a *local* variable; the `global` keyword tells Python to bind the module-level name instead. `global` is generally discouraged because shared mutable global state makes code hard to reason about and test — prefer passing values in and returning them out.

**Q2. What is a closure, and give a real use case.**

A closure is an inner function that "remembers" variables from its enclosing scope even after the outer function has returned. It lets you carry state without a class. A common use is a configurable function factory — e.g. `make_multiplier(n)` returns a function that multiplies by `n` — or a counter that keeps its running total. Decorators are built on closures.

**Q3. Do type hints change how the program runs at runtime?**

No. Python does not enforce type hints at runtime — `def f(x: int)` will still accept a string and run. Hints are metadata used by static checkers (`mypy`), IDEs (autocomplete, error highlighting), documentation, and libraries like Pydantic and FastAPI that *choose* to read and enforce them. They matter enormously for AI tool-calling: type hints plus docstrings are exactly what gets converted into the JSON schema an LLM uses to call your function correctly.

**Q4. What does `if __name__ == "__main__":` do and why use it?**

When a file is run directly, Python sets its `__name__` to `"__main__"`; when the file is *imported* as a module, `__name__` is the module's name. Putting your script/entry code under `if __name__ == "__main__":` means that code runs only when the file is executed directly, not when it's imported. This lets a file act as both a reusable module and a runnable script, and keeps test/demo code from firing on import.

**Q5. What is the difference between `lambda`, `map`, and `filter`, and when should you avoid `lambda`?**

A `lambda` is a small anonymous one-expression function, often passed as an argument (e.g. the `key=` in `sorted`). `map(fn, iterable)` applies a function to every element; `filter(fn, iterable)` keeps only elements for which the function is truthy. Avoid `lambda` when the logic is non-trivial or reused — a named `def` is more readable and debuggable — and in modern Python a comprehension is often clearer than `map`/`filter` with a lambda.
