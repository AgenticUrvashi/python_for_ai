# WEEK 11 — Advanced Python for AI (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> 🟡 **Pacing note:** *"Yeh week thoda advanced hai — generators aur decorators pehli baar dimaag ghumate hain. SLOW chalo, examples baar-baar dohrao. Yeh exact idioms aap HAR agent codebase mein dekhoge, isliye mehnat zaroori hai."*
>
> **Week promise:** *"Is week woh 'pro' Python seekhenge jo har AI codebase mein milta hai: generators (LLM streaming ka raaz), decorators (@tool, @retry), context managers, dataclasses, aur typing. Week ke end tak aap real agent-code padh aur likh paoge."*

---

## CLASS 61 — Generators & yield

*"Ek sawaal: agar aapko 10 lakh numbers chahiye, kya sab ek saath list mein banaoge? Woh poori RAM kha jaayega! Generators ek-ek karke values 'banate' hain, jab zaroorat ho — sab ek saath nahi. Aur sabse cool: LLM ka jo token-by-token streaming hota hai, woh ek generator hi hai."*

### 🎯 Today's goal
`yield` se generators banana, aur iterables vs iterators samajhna.

### 👨‍🏫 Concept 1 — problem: list sab kuch ek saath banati hai
```python
def first_n_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result               # poori list — sab memory mein

print(first_n_squares(5))       # [0, 1, 4, 9, 16]
# n = 10 crore hota toh? RAM khatam!
```

### 👨‍🏫 Concept 2 — generator (`yield`) — ek-ek karke do

> **📖 Technical definition — Generator:** A generator is a special function that uses `yield` to produce a sequence of values lazily, one at a time, pausing its state between values. It computes each value only on demand, using far less memory than building a full list.

```python
def first_n_squares(n):
    for i in range(n):
        yield i ** 2            # 'return' nahi — 'yield' (ek value do, ruko)

squares = first_n_squares(5)
print(squares)                  # <generator object ...>  — abhi values bani nahi!

for sq in squares:              # ab ek-ek karke banti hain
    print(sq)                   # 0, 1, 4, 9, 16
```
*"`yield` `return` jaisा hai par jaadui: function PAUSE ho jaata hai aur ek value deta hai, phir agli baar wahin se chalu hota hai. Values 'on demand' banti hain — sirf jab loop maange. Memory bachti hai, kitna bhi bada ho."*

### 👨‍🏫 Concept 2.5 — Iterables, Iterators & Generators (dono mein farak)

> **📖 Technical definitions:**
> - **Iterable:** An Iterable is any Python object (like a list, tuple, or string) that can be looped over in a `for` loop. It contains data in memory but does not track its own iteration state or current position. Passing an Iterable to `iter(x)` creates and returns a new Iterator object.
> - **Iterator:** An Iterator is a stateful stream object that remembers its current position during iteration. It fetches the next item one-at-a-time whenever `next(iterator)` is called. When no elements remain, calling `next()` raises a `StopIteration` exception.
> - **Generator:** A Generator is a special type of function that uses `yield` to return values lazily one at a time. Calling a generator function automatically returns a specialized Iterator object without storing all items in memory at once. It pauses execution at `yield` and resumes seamlessly when the next item is requested, making it ideal for LLM token streaming.

```python
# Iterable (list, tuple, string) — items ka collection
numbers = [1, 2, 3]         # Iterable

# Iterator — stateful stream jo next() se ek-ek element deta hai
it = iter(numbers)          # iter() se Iterator milta hai
print(next(it))             # 1
print(next(it))             # 2
print(next(it))             # 3
# print(next(it))           # StopIteration error! (stream khatam)
```

#### 📊 Summary Table

| Concept | Memory Behavior | State Tracking | How it is Created |
| :--- | :--- | :--- | :--- |
| **Iterable** | Stores all elements in memory at once | Does not track current position | Defined as `[1, 2, 3]`, tuples, strings |
| **Iterator** | Fetches items one at a time on demand | Remembers current position; advances via `next()` | Created via `iter(iterable)` |
| **Generator** | Computes values lazily on demand | Pauses and resumes function state at `yield` | Function written with `yield` |

*"`Iterable` = sequence jisme items hain. `Iterator` = pointer/stream jo state track karta hai. Generator function calling se ek **Iterator** object banta hai!"*

### 👨‍🏫 Concept 3 — yield ka 'pause/resume' (key idea)
```python
def counter():
    print("Start")
    yield 1
    print("Resumed after 1")
    yield 2
    print("Resumed after 2")
    yield 3

gen = counter()
print(next(gen))    # Start \n 1       — pehli yield tak chala, ruka
print(next(gen))    # Resumed after 1 \n 2   — wahin se chala
print(next(gen))    # Resumed after 2 \n 3
```
*"`next()` generator ko agli `yield` tak chalata hai, phir woh RUK jaata hai (state yaad rakhta hai). Yeh 'pause aur resume' hi generators ka dil hai. Streaming exactly aise kaam karta hai."*

### 👨‍🏫 Concept 4 — generator expression (one-line)
```python
# list comprehension — sab ek saath (square brackets)
squares_list = [x ** 2 for x in range(5)]       # [0, 1, 4, 9, 16]

# generator expression — on demand (round brackets!)
squares_gen = (x ** 2 for x in range(5))        # <generator object>
print(sum(squares_gen))                          # 30  — ek-ek karke add hue
```
*"Bas `[ ]` ko `( )` se badlo, aur comprehension ek generator ban jaata hai — lazy aur memory-friendly. `sum()`, `max()` jaise functions ke saath perfect."*

### 💻 Demo — fake token streamer (LLM jaisा!)
```python
import time

def stream_response(text):
    """LLM jaisा — ek-ek word 'stream' karo."""
    for word in text.split():
        yield word
        time.sleep(0.1)         # asli LLM jaisा thoda delay

for token in stream_response("Hello I am an AI agent"):
    print(token, end=" ", flush=True)       # words aate hi dikhte hain
# Hello I am an AI agent  (ek-ek karke aate hue)
```
*"Dekho — yeh BILKUL waise hai jaise ChatGPT jawaab 'type' karta dikhta hai, ek-ek word. Woh ek generator hai jo tokens yield karta hai. Aapne abhi LLM streaming ka core samajh liya!"*

### ❌ Common mistakes
```python
def gen():
    yield 1
    yield 2
g = gen()
print(g)            # ❌ <generator object> — values dekhne ke liye loop ya list() karo
print(list(g))      # ✅ [1, 2]
print(list(g))      # ❌ [] — generator ek baar use hone ke baad khaali (dobara nahi chalta)
```

### 🔗 Agentic link
*"Yeh week ka sabse bada idea: **LLM responses generators se stream hote hain.** Model ek-ek token yield karta hai, aur aap unhe aate hi dikhate ho (real-time feel). Bina generators ke, aapko poora jawaab ruk kar wait karna padta. Aaj aapne streaming ka asli mechanism seekha — Week 16 mein isse real LLM par lagayenge."*

### ✍️ Homework
1. Ek generator `even_numbers(n)` jo pehle n even numbers yield kare.
2. Ek generator `countdown(n)` jo n se 1 tak yield kare.
3. Generator expression se 1-100 ke squares ka sum nikaalo.

**Answers:**
```python
# 1
def even_numbers(n):
    for i in range(n):
        yield i * 2
print(list(even_numbers(5)))     # [0, 2, 4, 6, 8]

# 2
def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(list(countdown(5)))        # [5, 4, 3, 2, 1]

# 3
print(sum(x ** 2 for x in range(1, 101)))    # 338350
```

### 🔗 Agli class
*"Agli class — DECORATORS: ek function ko 'lapet' kar usme nayi power daalna, bina use chhede. `@tool`, `@retry`, `@timer` — sab decorators hain."*

---

## CLASS 62 — Decorators

*"Decorator ek aisा function hai jo doosre function ko 'lapet' (wrap) kar use extra power deta hai — bina original code badle. Soch lo ek gift ko wrapping paper mein lapetna — gift wahi, par upar kuch naya add ho gaya. `@timer`, `@retry`, `@tool` — yeh sab decorators hain, aur har framework mein milte hain."*

### 🎯 Today's goal
Decorators samajhna aur banana (closures par based — Week 6 yaad hai?).

### 👨‍🏫 Concept 1 — functions value hain (revision)
*"Pehle yaad karo: Python mein function bhi ek value hai. Use variable mein rakh sakte ho, doosre function ko de sakte ho, aur ek function doosra function return kar sakta hai (closures, Week 6)."*
```python
def greet():
    return "Hello"

say = greet          # function ko variable mein rakha (brackets nahi!)
print(say())         # Hello
```

### 👨‍🏫 Concept 2 — decorator ka basic dhaancha

> **📖 Technical definition — Decorator:** A decorator is a function that takes another function (or class) and returns a modified version, wrapping it with extra behaviour without changing its original code. The `@decorator` syntax applies it to the function defined beneath it.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()                          # original function chalao
        print("After the function")
    return wrapper

def say_hello():
    print("Hello!")

# manually wrap karo
decorated = my_decorator(say_hello)
decorated()
# Before the function
# Hello!
# After the function
```
*"`my_decorator` ek function leta hai, use ek `wrapper` ke andar lapet-ta hai (jo pehle/baad mein extra kaam karta hai), aur wrapper return karta hai. Original `say_hello` waise ka waise, par ab uske aage-peeche extra cheezein."*

### 👨‍🏫 Concept 3 — `@` syntax (sundar shortcut)
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator               # yeh shortcut hai 'say_hello = my_decorator(say_hello)' ka
def say_hello():
    print("Hello!")

say_hello()                 # ab automatically wrapped!
# Before \n Hello! \n After
```
*"`@my_decorator` likhna bilkul wahi hai jo `say_hello = my_decorator(say_hello)`. Bas saaf aur sundar. Yeh `@` aapne frameworks mein bahut dekha hoga — ab pata hai woh kya karta hai!"*

### 👨‍🏫 Concept 4 — arguments wale functions ko wrap karna (`*args, **kwargs`)
```python
import functools

def timer(func):
    @functools.wraps(func)              # original ka naam/docstring bachata hai
    def wrapper(*args, **kwargs):       # KOI bhi arguments accept karo
        import time
        start = time.time()
        result = func(*args, **kwargs)  # original ko uske arguments ke saath chalao
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result                   # original ka result wapas do
    return wrapper

@timer
def slow_add(a, b):
    import time
    time.sleep(0.5)
    return a + b

print(slow_add(2, 3))
# slow_add took 0.50xx s
# 5
```
*"`*args, **kwargs` (Week 5!) se wrapper KISI bhi function ko, kisi bhi arguments ke saath wrap kar sakta hai. `functools.wraps` original ka naam safe rakhta hai (best practice). Aur `return result` zaroori hai — warna original ka jawaab kho jaata hai."*

### 💻 Demo — @logger decorator
```python
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def multiply(a, b):
    return a * b

multiply(4, 5)
# Calling multiply with (4, 5)
# multiply returned 20
```

### ❌ Common mistakes
```python
def deco(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)       # ❌ return bhool gaye → result None ho jaata hai
    return wrapper

def deco(func):
    def wrapper():                  # ❌ args accept nahi kiye → arguments wale func crash
        return func()
    return wrapper
```

### 🔗 Agentic link
*"Decorators agent code mein HAR JAGAH hain: `@tool` ek function ko agent-tool register karta hai, `@retry` (Week 9 ka retry, decorator version!) failures handle karta hai, `@timer`/`@logger` performance track karte hain, `@lru_cache` results cache karta hai. Ab jab aap `@something` dekhoge, aapko pata hoga andar kya ho raha hai. Yeh ek bada level-up hai."*

### ✍️ Homework
1. Ek `@uppercase` decorator banao jo function ke string-result ko uppercase kare.
2. Ek `@count_calls` decorator jo gine function kitni baar call hua.
3. `@timer` ko ek function par lagao jo loop chalata hai.

**Answers:**
```python
import functools
# 1
def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper
@uppercase
def greet(name):
    return f"hello {name}"
print(greet("asha"))        # HELLO ASHA

# 2
def count_calls(func):
    func.calls = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func.calls += 1
        print(f"Call #{func.calls}")
        return func(*args, **kwargs)
    return wrapper
@count_calls
def hi():
    return "hi"
hi(); hi()      # Call #1, Call #2
```

### 🔗 Agli class
*"Agli class — context managers (`with` khud banana) aur better collections (Counter, defaultdict, namedtuple). Roz kaam aane wale tools."*

---

## CLASS 63 — Context Managers & collections

*"`with open(...)` yaad hai? Woh ek 'context manager' hai — automatically file band karta hai. Aaj seekhenge apne khud ke `with` blocks banana, aur kuch super-handy containers jo `collections` module mein hain."*

### 🎯 Today's goal
Apna context manager banana, aur `Counter`, `defaultdict`, `namedtuple` use karna.

### 👨‍🏫 Concept 1 — context manager kya karta hai

> **📖 Technical definition — Context manager:** A context manager is an object used with the `with` statement that runs setup code on entry and guaranteed cleanup code on exit, even if an error occurs. It is commonly created with the `@contextmanager` decorator, where code before `yield` is setup and code after it is cleanup.

*"`with` block ki khoobi: woh setup aur cleanup APNE AAP karta hai — chahe error aaye ya na aaye. `with open` file kholta hai aur GUARANTEED band karta hai. Hum apne aise blocks bana sakte hain."*

### 👨‍🏫 Concept 2 — `contextmanager` se apna banao
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.time()         # setup (with se pehle)
    yield                       # yahan with-block ka code chalta hai
    end = time.time()           # cleanup (with ke baad)
    print(f"{label} took {end - start:.4f}s")

with timer("My task"):
    total = sum(range(1000000))
# My task took 0.0xxx s
```
*"`yield` se PEHLE wala code `with` shuru hote hi chalता hai (setup), `yield` ke BAAD wala block khatam hone par (cleanup). Yeh exactly woh pattern hai jo file kholne/band karne mein use hota hai. Yahan humne timing measure kiya."*

### 👨‍🏫 Concept 3 — `Counter` (cheezein gino)

> **📖 Technical definition — `collections` containers:** The `collections` module offers specialised containers: `Counter` tallies how often each element appears, `defaultdict` supplies a default value for missing keys instead of raising `KeyError`, and `namedtuple` creates a tuple whose fields are accessible by name.

```python
from collections import Counter

words = "apple banana apple cherry banana apple".split()
counts = Counter(words)
print(counts)                   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counts["apple"])          # 3
print(counts.most_common(2))    # [('apple', 3), ('banana', 2)]  — top 2
```
*"`Counter` automatically items gin-ta hai — manually dict banane se bahut aasan. `most_common(n)` top-n frequent items deta hai. Word-frequency, token-counting ke liye perfect."*

### 👨‍🏫 Concept 4 — `defaultdict` (missing key par crash nahi)
```python
from collections import defaultdict

# normal dict — missing key par KeyError
# defaultdict — missing key par default value

groups = defaultdict(list)      # missing key → khaali list
groups["fruits"].append("apple")    # 'fruits' nahi tha, par crash nahi — khaali list bani
groups["fruits"].append("banana")
groups["veggies"].append("carrot")
print(dict(groups))    # {'fruits': ['apple', 'banana'], 'veggies': ['carrot']}
```
*"`defaultdict(list)` se jab koi nayi key access karo, woh apne aap khaali list bana deta hai — `if key in dict` check ki zaroorat nahi. Data ko groups mein baant-ne ke liye lifesaver."*

### 👨‍🏫 Concept 5 — `namedtuple` (naam wala tuple)
```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)          # 10    — index ke bajaye NAAM se access!
print(p.y)          # 20
print(p)            # Point(x=10, y=20)
```
*"Normal tuple mein `p[0]`, `p[1]` likhna padta. `namedtuple` se `p.x`, `p.y` — readable. Yeh ek halka-phalka class jaisा hai chhote records ke liye (par next class ka `@dataclass` aksar behtar hai)."*

### ❌ Common mistakes
```python
from contextlib import contextmanager
@contextmanager
def bad():
    print("setup")
    # ❌ yield bhool gaye → 'with' kaam nahi karega

from collections import Counter
c = Counter([1, 2, 2])
print(c[5])         # 0 (KeyError nahi — missing par 0 deta hai, yeh feature hai)
```

### 🔗 Agentic link
*"Context managers se hum agent ke 'sessions' manage karte hain (API client kholo, kaam karo, band karo — guaranteed). `Counter` se tokens/word-frequency tally karte hain. `defaultdict` se results ko categories mein group karte hain (jaise har tool ke results alag). Yeh roz kaam aane wale tools hain."*

### ✍️ Homework
1. Apna context manager `@contextmanager` se banao jo "Enter"/"Exit" print kare.
2. Ek sentence mein har word ki frequency `Counter` se nikaalo.
3. `defaultdict(list)` se students ko unki grade ke hisaab se group karo.

**Answers:**
```python
from contextlib import contextmanager
from collections import Counter, defaultdict
# 1
@contextmanager
def section():
    print("Enter")
    yield
    print("Exit")
with section():
    print("Inside")
# Enter / Inside / Exit

# 2
print(Counter("the cat sat on the mat".split()))
# Counter({'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1})

# 3
students = [("Asha", "A"), ("Rahul", "B"), ("Priya", "A")]
groups = defaultdict(list)
for name, grade in students:
    groups[grade].append(name)
print(dict(groups))     # {'A': ['Asha', 'Priya'], 'B': ['Rahul']}
```

### 🔗 Agli class
*"Agli class — dataclasses (boilerplate-free classes), functools (lru_cache, partial), aur enum. Yeh aapke agent objects ko saaf banayenge."*

---

## CLASS 64 — dataclasses, functools & enum

*"Yaad hai class banane mein kitna `self.x = x` likhna padta tha? Aaj `@dataclass` se woh sab AUTOMATIC ho jaayega. Plus `lru_cache` (results cache karke speed), aur `enum` (fixed choices). Yeh teeno agent code ko saaf aur tez banate hain."*

### 🎯 Today's goal
`@dataclass`, `functools.lru_cache`/`partial`, aur `enum` use karna.

### 👨‍🏫 Concept 1 — `@dataclass` (boilerplate khatam)

> **📖 Technical definition — Dataclass:** A dataclass is a class decorated with `@dataclass` that automatically generates boilerplate methods (like `__init__`, `__repr__`, and `__eq__`) from its type-annotated attributes, giving a concise way to define classes that mainly store data.

*"Normal class mein `__init__`, `__repr__`, `__eq__` sab khud likhna padta. `@dataclass` yeh sab APNE AAP bana deta hai — bas attributes likho."*
```python
from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

msg = Message("user", "Hello")
print(msg)              # Message(role='user', content='Hello')   — __repr__ free!
print(msg.role)         # user
print(msg == Message("user", "Hello"))    # True  — __eq__ free!
```
*"Bas `@dataclass` aur type-annotated attributes likho — Python `__init__`, `__repr__` (Class 46!), aur `__eq__` (Class 47!) sab khud bana deta hai. Week 8 ki saari mehnat ek line mein! Agent objects (Message, ToolCall) ke liye perfect."*

### 👨‍🏫 Concept 2 — dataclass with defaults & methods
```python
from dataclasses import dataclass, field

@dataclass
class Agent:
    name: str
    model: str = "gpt"                          # default value
    tools: list = field(default_factory=list)   # safe mutable default!

    def add_tool(self, tool):
        self.tools.append(tool)

a = Agent("Jarvis")
a.add_tool("calculator")
print(a)        # Agent(name='Jarvis', model='gpt', tools=['calculator'])
```
*"Default value seedhe likho (`model: str = "gpt"`). Par mutable default (list) ke liye `field(default_factory=list)` use karo — yaad hai Week 5 ka mutable-default trap? Dataclass usse `default_factory` se safely handle karta hai."*

### 👨‍🏫 Concept 3 — `functools.lru_cache` (results yaad rakho)

> **📖 Technical definition — `lru_cache`:** `lru_cache` is a decorator that caches (memoizes) a function's return values keyed by its arguments. When the same arguments are seen again, the stored result is returned instantly instead of recomputing, avoiding repeated expensive work.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def slow_square(n):
    print(f"Computing {n}...")      # sirf pehli baar dikhega
    return n ** 2

print(slow_square(4))       # Computing 4... \n 16
print(slow_square(4))       # 16    — "Computing" NAHI dikha, cache se aaya!
```
*"`@lru_cache` function ke results yaad rakhta hai. Same input dobara → calculate nahi karta, cache se turant deta hai. Yeh slow ya mehnga kaam (jaise API calls) dobara karne se bachata hai — paisa aur time dono bachte hain."*

### 👨‍🏫 Concept 4 — `functools.partial` (pre-filled function)
```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)      # exp ko 2 pe fix kar do
cube = partial(power, exp=3)

print(square(5))        # 25
print(cube(2))          # 8
```
*"`partial` ek function ke kuch arguments pehle se bhar deta hai, ek naya simpler function banakar. Configured tools banane mein kaam aata hai."*

### 👨‍🏫 Concept 5 — `enum` (fixed choices)

> **📖 Technical definition — Enum:** An enum (enumeration) is a class of named, fixed constant values. It gives a set of related choices meaningful names (accessed as `Enum.MEMBER`), preventing invalid values and typos compared to using raw strings or numbers.

```python
from enum import Enum

class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

print(Role.USER)            # Role.USER
print(Role.USER.value)      # user
# fixed choices — typo se bachao
msg_role = Role.SYSTEM.value
```
*"`Enum` fixed choices banata hai. `"user"`, `"assistant"` jaise strings ko baar-baar type karne ke bajaye `Role.USER` use karo — typo nahi hoga, aur IDE auto-complete deta hai. LLM message roles ke liye perfect."*

### ❌ Common mistakes
```python
from dataclasses import dataclass
@dataclass
class Bad:
    items: list = []        # ❌ mutable default — field(default_factory=list) use karo

@dataclass
class Point:
    x                       # ❌ type annotation chahiye: x: int
```

### 🔗 Agentic link
*"Yeh teeno agent code mein core hain: `@dataclass` se `Message`, `ToolCall`, `AgentState` jaise saaf objects (Week 17 mein use karenge!). `@lru_cache` se repeat LLM/tool calls cache karke paisa bachao. `enum` se message roles aur tool names type-safe. Yeh modern Python AI code ki shakal hai."*

### ✍️ Homework
1. Ek `@dataclass Book` banao (title, author, year) aur 2 objects compare karo.
2. `@lru_cache` ek fibonacci function par lagao aur speed mehsoos karo.
3. Ek `Status` enum banao (PENDING, DONE, FAILED).

**Answers:**
```python
from dataclasses import dataclass
from functools import lru_cache
from enum import Enum
# 1
@dataclass
class Book:
    title: str
    author: str
    year: int
print(Book("AI", "Asha", 2026) == Book("AI", "Asha", 2026))    # True

# 2
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(30))      # 832040  (cache ke bina yeh slow hota)

# 3
class Status(Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"
print(Status.DONE.value)    # done
```

### 🔗 Agli class
*"Agli class — week ka finale: TYPING deep dive (precise type hints) aur ek project jisme generators, decorators, dataclasses sab milte hain."*

---

## CLASS 65 — Typing Deep Dive (Project Class)

*"Week 6 mein basic type hints kiye (`a: int`). Aaj PRO typing: optional values, kai possible types, function types, aur `TypedDict`. Yeh agent code ko safe aur self-documenting banata hai — aur LLM tool schemas types se hi bante hain."*

### 🎯 Today's goal
`Optional/Union/Any/Callable`, `list[]/dict[]`, `TypedDict`, aur `Protocol` (first pass).

### 👨‍🏫 Concept 1 — collection types (`list[]`, `dict[]`)
```python
def total(nums: list[int]) -> int:
    return sum(nums)

def get_scores() -> dict[str, int]:
    return {"Asha": 85, "Rahul": 90}
```
*"`list[int]` = ints ki list. `dict[str, int]` = string keys, int values waala dict. Yeh batata hai container ke ANDAR kya hai — bahut clear."*

### 👨‍🏫 Concept 2 — `Optional` (value ya None)

> **📖 Technical definition — Optional / Union types:** A union type (written with `|`) declares that a value may be one of several types. `str | None` (also written `Optional[str]`) means the value is either a string or `None`, signalling to callers that a missing result is possible.

```python
def find_user(user_id: int) -> str | None:     # string YA None
    users = {1: "Asha", 2: "Rahul"}
    return users.get(user_id)        # mila toh naam, nahi toh None

result = find_user(1)        # "Asha"
result = find_user(99)       # None
```
*"`str | None` ka matlab 'string ya None'. (Purane code mein `Optional[str]` likhते the — yeh wahi hai.) Yeh batata hai 'shayad value na mile' — caller ko None handle karna yaad rehta hai."*

### 👨‍🏫 Concept 3 — `Union` (kai possible types) — `|`
```python
def process(value: int | str) -> str:      # int YA string
    return str(value).upper()

print(process(42))          # 42
print(process("hello"))     # HELLO
```
*"`int | str` (Union) = 'int ya string'. Jab ek parameter kai types le sakta hai, yeh use document karta hai."*

### 👨‍🏫 Concept 4 — `Callable` (function type)
```python
from typing import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

print(apply(lambda x: x * 2, 5))    # 10
```
*"`Callable[[int], int]` ka matlab 'ek function jo ek int leta hai aur int return karta hai'. Jab aap function ko argument ki tarah pass karte ho (Week 6!), yeh use type karta hai."*

### 👨‍🏫 Concept 4.5 — `Iterator` & `Iterable` (streaming aur loopable types)

> **📖 Technical definition — Iterator & Iterable Types:** `Iterator[T]` represents a generator or iterator object that yields elements of type `T` one at a time. `Iterable[T]` represents any container or stream (list, tuple, generator) that can be iterated over.

```python
from typing import Iterator, Iterable

def generate_tokens() -> Iterator[str]:
    yield "Hello"
    yield "world"

def process_items(items: Iterable[int]) -> int:
    return sum(items)   # list, tuple, ya generator sab accept karega!
```
*"`Iterator[str]` generator function ka return type hota hai jo strings yield karta hai (jaise Mini Project mein `stream_words`). `Iterable[int]` function parameter type karta hai jo kisi bhi loopable container (list, generator, etc.) ko accept kare."*

### 👨‍🏫 Concept 5 — `TypedDict` (dict ki exact shape)

> **📖 Technical definition — `TypedDict`:** A `TypedDict` declares the exact expected shape of a dictionary — which keys must be present and the type of each value — so type checkers can verify dictionary usage while it remains a plain `dict` at runtime.

```python
from typing import TypedDict

class Message(TypedDict):
    role: str
    content: str

msg: Message = {"role": "user", "content": "Hello"}     # type-checked dict!
```
*"`TypedDict` ek dict ki EXACT shape define karta hai — kaunse keys, kaunse types. Yeh LLM messages ke liye perfect hai, kyunki woh dicts hote hain par fixed shape ke. Ab tools (jaise mypy) galat keys pakad sakte hain."*

### 👨‍🏫 Concept 6 — `Protocol` (first pass — duck typing)

> **📖 Technical definition — `Protocol`:** A `Protocol` defines an interface by the methods and attributes an object must have, rather than by its class. Any object that provides those members satisfies the protocol (structural, "duck" typing), enabling flexible type checking.

*"`Protocol` kehta hai 'mujhe parwaah nahi object kaunsi class ka hai — bas usme yeh method hona chahiye'. Yeh flexible typing hai."*
```python
from typing import Protocol

class Runnable(Protocol):
    def run(self) -> str: ...       # bas yeh method chahiye

def execute(tool: Runnable) -> str:
    return tool.run()               # koi bhi object jisme run() ho, chalega

# Calling example (duck typing in action):
class SearchTool:
    def run(self) -> str:
        return "Searching web..."

tool = SearchTool()                 # SearchTool Runnable se inherit NAHI karta!
print(execute(tool))                # Searching web...
```
*"`Protocol` se hum kehte hain 'jisme `run()` hai woh tool hai' — `SearchTool` ne `Runnable` se inherit nahi kiya, fir bhi `execute(tool)` chal gaya kyunki uske paas `.run()` method hai! Yeh structural typing (duck typing) hai. Agent tools ke liye bahut use hota hai."*

### 🛠️ Mini Project — typed streaming tool with decorators
*"Yeh project poora week jodta hai: dataclass (Message), decorator (@timer/@retry), generator (streaming), aur full typing. Yeh real agent-code jaisа dikhta hai."*
```python
import time
import functools
from dataclasses import dataclass
from typing import Callable, Iterator


@dataclass
class Message:
    role: str
    content: str


def timer(func: Callable) -> Callable:
    """Decorator: print how long a function takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[{func.__name__} took {time.time() - start:.3f}s]")
        return result
    return wrapper


@timer
def build_messages(texts: list[str]) -> list[Message]:
    """Turn raw strings into typed Message objects."""
    return [Message(role="user", content=t) for t in texts]


def stream_words(message: Message) -> Iterator[str]:
    """Stream a message's content word-by-word (like an LLM)."""
    for word in message.content.split():
        yield word
        time.sleep(0.05)


# --- demo ---
messages = build_messages(["Hello world", "How are you"])
print(messages)             # [Message(role='user', content='Hello world'), ...]

print("Streaming first message: ", end="")
for token in stream_words(messages[0]):
    print(token, end=" ", flush=True)
print()
```
*"Dekho yeh kitna 'pro' dikhta hai: typed dataclass `Message`, ek `@timer` decorator, ek streaming generator with `Iterator[str]` type. Yeh BILKUL real agent code jaisा hai. Aap ab advanced Python likh rahe ho!"*

### ❌ Common mistakes
```python
def f(x: int) -> str:
    return x            # ❌ int return kiya par '-> str' likha (mypy pakdega)

from typing import Callable
def g(func: Callable[int, int]):    # ❌ Callable[[int], int] — args list mein
    ...
```

### 🔗 Agentic link
*"Yeh week ka taaj: precise types se LLM tool schemas APNE AAP ban sakte hain (Week 17!). `TypedDict` LLM messages ko type karta hai, `Callable` tools ko, `Protocol` 'koi bhi tool jisme run() ho' ko. Aur dataclass+decorator+generator — yeh teeno har agent codebase ki reedh ki haddi hain. Aapne advanced Python jeet liya!"*

### ✍️ Homework
1. Ek function likho with `list[str]` parameter aur `dict[str, int]` return type.
2. Ek function jo `int | None` return kare (mile toh number, nahi toh None).
3. Ek `TypedDict` `User` banao (name: str, age: int).

**Answers:**
```python
from typing import TypedDict
# 1
def count_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}
print(count_lengths(["hi", "bye"]))     # {'hi': 2, 'bye': 3}

# 2
def safe_divide(a: int, b: int) -> int | None:
    if b == 0:
        return None
    return a // b
print(safe_divide(10, 2))   # 5
print(safe_divide(10, 0))   # None

# 3
class User(TypedDict):
    name: str
    age: int
u: User = {"name": "Asha", "age": 17}
print(u["name"])    # Asha
```

### 🏁 Week 11 wrap-up*"Yeh advanced week aapne jeeta:*
- *Generators & yield — LLM streaming ka raaz (Class 61)*
- *Decorators — @tool, @retry, @timer (Class 62)*
- *Context managers + collections (Class 63)*
- *dataclasses, lru_cache, enum (Class 64)*
- *Typing deep dive + pro project (Class 65)*

*Ab aap REAL agent code padh aur likh sakte ho — generators, decorators, typed dataclasses sab samajhte ho. Yeh ek bada milestone hai!*

> 🟢 **Buffer/revision suggestion:** *Apne tools module ko in nayi cheezon se rebuild karo — dataclass objects, @retry decorator, typed functions. Aage badhne se pehle yeh pakka karo.*

*Next week — PROFESSIONAL WORKFLOW: virtual environments, Git, secrets. Real engineer ki tarah kaam karna. Shabaash!"*

### 📝 Weekend revision task
Apne tools module ko upgrade karo: har tool ko ek `@dataclass`, ek `@timer` decorator har function par, aur full type hints. Ek streaming generator bhi add karo. Yeh aapka portfolio piece hai!

---

## 🎤 Industry Interview Questions — Week 11

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is a generator, how does it differ from a list, and why does it matter for LLMs?**

A generator (a function using `yield`, or a generator expression) produces values lazily, one at a time, pausing and resuming its state between values, instead of building the whole sequence in memory like a list. This means constant memory usage even over huge or infinite streams. It maps directly onto LLM *streaming*: tokens arrive and are yielded one by one so the UI can display them in real time, rather than waiting for the whole response.

**Q2. What is a decorator and how does it work?**

A decorator is a function that takes another function and returns a new function that wraps it, adding behavior before/after the original without changing its code. `@my_decorator` above a `def` is just syntactic sugar for `func = my_decorator(func)`. Decorators use closures and typically `*args, **kwargs` to forward arguments, plus `functools.wraps` to preserve the original's name/docstring. Common examples: `@retry`, `@timer`, `@lru_cache`, and the `@tool` decorators used in agent frameworks.

**Q3. What does `@dataclass` give you?**

`@dataclass` auto-generates boilerplate for classes that mainly hold data: `__init__`, `__repr__`, and `__eq__` based on the fields you declare with type hints. You get clean, readable, comparable objects with far less code, plus features like default values, `frozen=True` for immutability, and `field(default_factory=...)` for safe mutable defaults. It's ideal for modeling messages, tool definitions, and config objects.

**Q4. What is `functools.lru_cache` and what are its constraints?**

`@lru_cache` memoizes a function: it stores results keyed by the arguments so repeated calls with the same inputs return instantly instead of recomputing. It's great for expensive pure functions (and to save money by not re-calling an LLM/embedding for identical inputs). Constraints: arguments must be hashable (no lists/dicts), and you must *not* cache functions whose result should change over time or per call (current time, random values, live data) — you'd serve stale results.

**Q5. In typing, what's the difference between `Optional`, `Union`, and a `Protocol`?**

`Optional[X]` means "an `X` or `None`" (shorthand for `Union[X, None]`). `Union[A, B]` (or `A | B`) means the value can be one of several types. A `Protocol` defines *structural* typing ("duck typing" made explicit): any object that has the required methods/attributes satisfies the protocol, without needing to inherit from it — unlike an ABC, which requires explicit subclassing. Protocols are great for typing "anything with a `.run()` method."
