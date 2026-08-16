# WEEK 8 — Pythonic Classes (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Pichle week classes banayi. Is week unhe SAAF aur PROFESSIONAL banayenge: objects ko sundar print karna, compare karna, computed attributes, aur objects ke andar objects (composition). Week ke end tak aap ek Agent ka structural mock banaoge jo Tools rakhega."*

---

## CLASS 46 — __str__ & __repr__

*"Ek sawaal: jab aap apne object ko print karte ho, kya aata hai? Chalo dekhte hain — kuch ajeeb sa `<__main__.Dog object at 0x...>` aata hai. Bekaar! Aaj seekhenge object ko SUNDAR aur USEFUL print karna. Yeh debugging aur logging ke liye must hai."*

### 🎯 Today's goal
`__str__` (user ke liye) aur `__repr__` (developer ke liye) likhna.

### 👨‍🏫 Concept 1 — problem: default print bekaar hai
```python
class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Tommy")
print(d)        # <__main__.Dog object at 0x000001A2...>  😖 useless
```
*"Yeh memory address kisi kaam ka nahi. Hum chahte hain print karne par useful info dikhe."*

### 👨‍🏫 Concept 2 — `__str__` (insaano ke liye sundar)

> **📖 Technical definition — `__str__` and `__repr__`:** These are special ("dunder") methods that define an object's text form. `__str__` returns a readable string for end users (used by `print()` and `str()`), while `__repr__` returns an unambiguous, developer-oriented string for debugging (used by `repr()` and in containers). If only one is defined, `__repr__` acts as the fallback.

*"`__str__` ek special method (dunder = double-underscore) hai. Jab aap object ko `print()` karte ho, Python ise call karta hai. Yeh ek readable string return karta hai."*
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

d = Dog("Tommy", 3)
print(d)            # Tommy (3 years old)   ✅ ab sundar hai!
```
*"`print(d)` automatically `d.__str__()` call karta hai. Ab output saaf aur samajhne layak hai. Yeh end-user ya logs ke liye banao."*

### 👨‍🏫 Concept 3 — `__repr__` (developer/debug ke liye)
*"`__repr__` doosra version hai — yeh developer ke liye 'technical' representation deta hai, jo debugging mein kaam aata hai. Aadarsh: `__repr__` aisा ho ki use copy karke object dobara ban sake."*
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, age {self.age}"

    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

d = Dog("Tommy", 3)
print(d)            # Tommy, age 3              (__str__ — print ke liye)
print(repr(d))      # Dog(name='Tommy', age=3)  (__repr__ — debug ke liye)
dogs = [Dog("A", 1), Dog("B", 2)]
print(dogs)         # [Dog(name='A', age=1), Dog(name='B', age=2)]  (list __repr__ use karti hai)
```
*"Farak: `__str__` = friendly (print ke liye). `__repr__` = exact/technical (debug, lists ke andar). Agar sirf ek likhना ho, `__repr__` likho — woh dono jagah fallback ban jaata hai."*

### 💻 Demo — Message object (agent-flavoured)
```python
class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def __repr__(self):
        return f"Message(role='{self.role}', content='{self.content}')"

msg = Message("user", "Hello AI")
print(msg)          # Message(role='user', content='Hello AI')

history = [Message("user", "Hi"), Message("assistant", "Hello!")]
print(history)      # [Message(...), Message(...)]
```

### ❌ Common mistakes
```python
class Dog:
    def __str__(self):
        print(self.name)        # ❌ print mat karo — RETURN karo string
        # sahi: return self.name

class Dog:
    def __str__(self):
        return self.age         # ❌ age int hai — __str__ ko STRING return karna hai
        # sahi: return str(self.age)
```

### 🔗 Agentic link
*"Agents debugging mein bahut waqt jaata hai — 'agent ne yeh tool kyun chuna?'. Agar aapke Message/ToolCall/AgentState objects mein achhe `__repr__` ho, toh logs padhne mein aasaan ho jaate hain aur aap bugs jaldi pakad lete ho. Readable objects = readable logs = fast debugging."*

### ✍️ Homework
1. `Student` class mein `__str__` add karo jo "NAME scored MARKS" de.
2. `Book` class (title, author) mein `__repr__` add karo.
3. 3 objects ki list banao aur print karke dekho `__repr__` kaise kaam karta hai.

**Answers:**
```python
# 1
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"{self.name} scored {self.marks}"
print(Student("Asha", 85))      # Asha scored 85

# 2 & 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"
books = [Book("Python", "Guido"), Book("AI", "Asha")]
print(books)     # [Book('Python', 'Guido'), Book('AI', 'Asha')]
```

### 🔗 Agli class
*"Agli class — aur dunders: objects ko compare karna (`==`) aur size dena (`len`), plus class-level data sab objects mein share karna."*

---

## CLASS 47 — More Dunders & Attributes

*"Pichli class mein objects ko print karna seekha. Aaj unhe COMPARE karna (`==`), SIZE dena (`len()`), aur ek nayi cheez — data jo SAARE objects mein share ho (class attributes). Dunders Python ko 'magic' banate hain."*

### 🎯 Today's goal
`__eq__`, `__len__`, aur class vs instance attributes.

### 👨‍🏫 Concept 1 — problem: objects compare nahi hote
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)     # False  😖 — same values, par Python ko alag lagte hain
```
*"Default mein Python sochta hai do alag objects hamesha alag hain (chahe values same ho). Hum chahte hain 'same values = equal'."*

### 👨‍🏫 Concept 2 — `__eq__` (apni equality define karo)

> **📖 Technical definition — `__eq__` and `__len__`:** Dunder methods let objects work with built-in operations. `__eq__` defines how the `==` operator compares two objects (usually by comparing their data). `__len__` defines what the built-in `len()` returns for an object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(5, 5)
print(p1 == p2)     # True   ✅ same values = equal
print(p1 == p3)     # False
```
*"`__eq__` Python ko batata hai do objects ko KAISE compare karein. `other` doosra object hai. Ab `==` content ke hisaab se kaam karta hai, jaisा humne define kiya."*

### 👨‍🏫 Concept 3 — `__len__` (object ko size do)
```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

p = Playlist()
p.add("Song A")
p.add("Song B")
print(len(p))       # 2   ✅ len() ab hamare object par chalta hai
```
*"`len(p)` automatically `p.__len__()` call karta hai. Ab hamare custom object par built-in `len()` kaam karta hai — bilkul list jaisा."*

### 👨‍🏫 Concept 4 — class attribute vs instance attribute

> **📖 Technical definition — Class attribute vs instance attribute:** A class attribute is defined on the class itself and shared by all instances. An instance attribute is defined per object (typically in `__init__` via `self`) and holds data unique to that object.

*"**Instance attribute** = har object ka apna (`self.name`). **Class attribute** = SAARE objects mein SHARE hota hai (class ke andar, kisi method ke bahar)."*
```python
class Dog:
    species = "Canis familiaris"    # CLASS attribute — sab dogs ke liye same

    def __init__(self, name):
        self.name = name            # INSTANCE attribute — har dog ka apna

d1 = Dog("Tommy")
d2 = Dog("Bruno")
print(d1.name, d2.name)         # Tommy Bruno     (alag-alag)
print(d1.species, d2.species)   # dono: Canis familiaris  (shared)
```

### 👨‍🏫 Concept 5 — class attribute se counter (common pattern)
```python
class User:
    count = 0                       # class attribute — total users

    def __init__(self, name):
        self.name = name
        User.count += 1             # har naye user par badhao

User("Asha")
User("Rahul")
User("Priya")
print(User.count)       # 3   — kitne users bane
```
*"`User.count` saare objects mein shared hai, isliye total ginne ke liye perfect. Dhyaan: `User.count` (class ka naam) use kiya, `self.count` nahi — kyunki yeh sabका saanjha hai."*

### ❌ Common mistakes
```python
class Box:
    items = []          # ❌ KHATRA: mutable class attribute sab objects mein share hoga!
# do alag boxes ek hi list share kar lenge (Week 5 wala mutable bug, OOP version)
# sahi: self.items = [] __init__ ke andar (har object ki apni list)
```

### 🔗 Agentic link
*"`__eq__` se hum check karte hain do messages/tool-calls same hain ya nahi (deduplication). `__len__` se ek conversation ki length (kitne messages) seedhe `len(conversation)` se milti hai. Aur class attributes se shared config (jaise default model) sab agents mein ek jagah rakhte hain, jabki har agent ka apna state instance attribute hota hai."*

### ✍️ Homework
1. `Money` class (amount) mein `__eq__` add karo taaki same amount equal ho.
2. `Cart` class mein `__len__` add karo jo items ki sankhya de.
3. Ek `Counter` class banao jisme class attribute `total` ho jo har object par badhe.

**Answers:**
```python
# 1
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __eq__(self, other):
        return self.amount == other.amount
print(Money(100) == Money(100))     # True

# 2
class Cart:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def __len__(self):
        return len(self.items)
c = Cart(); c.add("a"); c.add("b")
print(len(c))       # 2

# 3
class Counter:
    total = 0
    def __init__(self):
        Counter.total += 1
Counter(); Counter()
print(Counter.total)    # 2
```

### 🔗 Agli class
*"Agli class — classmethod aur staticmethod: alternative tareeke objects banane ke, aur utility functions. `from_config()` jaise patterns har AI SDK mein hain."*

---

## CLASS 48 — classmethod & staticmethod

*"Ab tak humne objects banaye `__init__` se seedhe. Par kabhi-kabhi humein 'alternative constructors' chahiye — jaise ek dictionary se ya string se object banana. Iske liye `@classmethod` aata hai. Aur jo methods object ke data use nahi karte, woh `@staticmethod` bante hain."*

### 🎯 Today's goal
`@classmethod` (alternative constructors) aur `@staticmethod` (utilities) banana.

### 👨‍🏫 Concept 1 — `@classmethod` (alternative constructor)

> **📖 Technical definition — `@classmethod`:** A class method receives the class itself as its first argument (conventionally `cls`) instead of an instance. It is commonly used to build alternative constructors that create and return a new instance from different input formats.

*"Ek classmethod object ki jagah CLASS ko `cls` ke roop mein leta hai. Yeh aksar 'naye object banane ke alag tareeke' ke liye use hota hai."*
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")     # "Asha,17" ko todo
        return cls(name, int(age))      # naya Person banao

# normal tareeka
p1 = Person("Asha", 17)
# alternative tareeka — string se
p2 = Person.from_string("Rahul,18")
print(p2.name, p2.age)      # Rahul 18
```
*"`cls` ka matlab 'yeh class' (`Person`). `cls(name, int(age))` ek naya Person banata hai. Yeh useful hai jab data alag format mein aata hai (string, dict) aur usse object banana ho."*

### 👨‍🏫 Concept 2 — `from_dict` (super common in AI)
```python
class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    @classmethod
    def from_dict(cls, data):
        return cls(data["role"], data["content"])

    def __repr__(self):
        return f"Message('{self.role}', '{self.content}')"

# API se aaya dict
raw = {"role": "user", "content": "Hello"}
msg = Message.from_dict(raw)
print(msg)      # Message('user', 'Hello')
```
*"Yeh pattern AI mein har jagah hai: API se dict aata hai, hum `from_dict` se use ek saaf object banate hain. Aap yeh poore course mein dekhoge."*

### 👨‍🏫 Concept 3 — `@staticmethod` (utility, object ka data nahi chahiye)

> **📖 Technical definition — `@staticmethod`:** A static method receives neither the instance (`self`) nor the class (`cls`). It is an ordinary function grouped inside a class for logical organisation, called on the class without needing an object.

*"Agar ek method ko na `self` (object) chahiye, na `cls` (class) — woh bas ek helper function hai jo logically class se juda hai — toh `@staticmethod` banao."*
```python
class MathHelper:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def add(a, b):
        return a + b

# object banaye bina seedhe call kar sakte ho
print(MathHelper.is_even(10))   # True
print(MathHelper.add(3, 4))     # 7
```
*"Dekho `is_even` mein na `self` hai na `cls` — yeh sirf ek related utility hai. Object banane ki zaroorat nahi, seedhe class se call karo."*

### 👨‍🏫 Concept 4 — kaunsa kab? (saaf rule)
| Method type | Pehla parameter | Kab use? |
|---|---|---|
| Normal method | `self` | Object ka data chahiye |
| `@classmethod` | `cls` | Naya object banane ka alag tareeka |
| `@staticmethod` | (kuch nahi) | Bas ek related helper, koi data nahi |

### ❌ Common mistakes
```python
class A:
    @classmethod
    def make(self):         # ❌ classmethod mein 'self' nahi, 'cls' likho
        ...

class A:
    @staticmethod
    def helper(self):       # ❌ staticmethod mein 'self' nahi hona chahiye
        ...
```

### 🔗 Agentic link
*"`Agent.from_config(config)` aur `Message.from_dict(data)` jaise classmethods har AI SDK mein milte hain — config file ya API response se objects banane ke liye. Aur staticmethods utility helpers ke liye (jaise token-counting). Yeh real-world OOP patterns hain jo aap roz dekhoge."*

### ✍️ Homework
1. `Date` class banao with `from_string("2026-06-28")` classmethod (year, month, day mein todo).
2. `Temperature` class mein staticmethod `c_to_f(c)` add karo.
3. `User` class mein `from_dict` classmethod banao.

**Answers:**
```python
# 1
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def from_string(cls, text):
        y, m, d = text.split("-")
        return cls(int(y), int(m), int(d))
date = Date.from_string("2026-06-28")
print(date.year, date.month, date.day)      # 2026 6 28

# 2
class Temperature:
    @staticmethod
    def c_to_f(c):
        return (c * 9 / 5) + 32
print(Temperature.c_to_f(37))       # 98.6

# 3
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"])
u = User.from_dict({"name": "Asha", "email": "a@x.com"})
print(u.name)       # Asha
```

### 🔗 Agli class
*"Agli class — `@property`: ek method ko attribute ki tarah use karna, aur computed/validated values. Bahut elegant feature."*

---

## CLASS 49 — property

*"Kabhi-kabhi humein ek 'attribute' chahiye jo asal mein CALCULATE hota hai (jaise area = πr²), ya jise set karte waqt CHECK karna ho. `@property` se hum method ko attribute ki tarah use kar sakte hain — bina `()` ke. Bahut saaf lagta hai."*

### 🎯 Today's goal
`@property` se computed aur validated attributes banana.

### 👨‍🏫 Concept 1 — computed property (apne aap calculate)

> **📖 Technical definition — `@property`:** The `@property` decorator turns a method into a read-only attribute that is accessed without parentheses and computed each time it is read. Adding a matching `@<name>.setter` allows the value to be assigned while running validation logic, combining a simple attribute interface with controlled access.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):                 # method, par property ban gaya
        return 3.14159 * self.radius ** 2

c = Circle(5)
print(c.area)       # 78.53975    — dhyaan: c.area() NAHI, bas c.area
c.radius = 10       # radius badlo
print(c.area)       # 314.159     — area apne aap update ho gaya!
```
*"`@property` ke saath, `area` ek method hai par hum use ATTRIBUTE ki tarah use karte hain (`c.area`, bina brackets). Aur jab radius badalti hai, area apne aap naya calculate hota hai — kyunki woh live compute hota hai, store nahi."*

### 👨‍🏫 Concept 2 — property with validation (setter)
*"Hum property ko set karte waqt bhi rules laga sakte hain — `@property` + `@x.setter` se."*
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):              # getter — value padhne par
        return self._celsius

    @celsius.setter
    def celsius(self, value):       # setter — value set karne par check
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

t = Temperature()
t.celsius = 25          # setter chalta hai (validation pass)
print(t.celsius)        # 25      (getter chalta hai)
t.celsius = -300        # ❌ ValueError: Below absolute zero!
```
*"Dekho: `t.celsius = 25` ek normal attribute jaisा lagta hai, par andar setter validation kar raha hai. User ko simple interface milta hai, par data safe rehta hai. Yeh encapsulation (Week 7) ka elegant version hai."*

### 👨‍🏫 Concept 3 — computed property jod kar
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 6)
print(r.area)           # 24
print(r.perimeter)      # 20
```

### 💻 Demo — Temperature with both units
```python
class Temp:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

t = Temp(37)
print(t.fahrenheit)     # 98.6
t.celsius = 0
print(t.fahrenheit)     # 32.0
```

### ❌ Common mistakes
```python
c = Circle(5)
print(c.area())     # ❌ TypeError — property hai, brackets mat lagao: c.area

# getter aur setter ke naam same hone chahiye
class A:
    @property
    def x(self): return self._x
    @x.setter
    def value(self, v):    # ❌ naam 'x' hona chahiye, 'value' nahi
        self._x = v
```

### 🔗 Agentic link
*"Agents mein computed properties bahut kaam aati hain: jaise `conversation.messages` jo har baar latest list banaye, ya `agent.total_cost` jo abhi tak ke tokens se cost calculate kare. Aur property setters se hum config values validate karte hain (jaise temperature 0-2 ke beech ho). Saaf interface, safe data."*

### ✍️ Homework
1. `Square` class mein `area` property banao.
2. `Person` class mein `age` property + setter jo negative age reject kare.
3. `Circle` mein `diameter` property banao (`2 * radius`).

**Answers:**
```python
# 1
class Square:
    def __init__(self, side):
        self.side = side
    @property
    def area(self):
        return self.side ** 2
print(Square(5).area)       # 25

# 2
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
p = Person(20)
p.age = 25
print(p.age)        # 25

# 3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
print(Circle(7).diameter)   # 14
```

### 🔗 Agli class
*"Agli class — week ka finale: COMPOSITION (objects ke andar objects), aur hum ek Agent banayenge jo Tools rakhega — ek asli agent ka structural mock!"*

---

## CLASS 50 — Composition (Project Class)

*"Inheritance 'IS-A' rishta tha (Dog IS-A Animal). Aaj COMPOSITION: 'HAS-A' rishta. Ek Car HAS-A Engine. Ek Agent HAS-A list of Tools. Bade systems mein composition aksar inheritance se behtar hota hai. Aaj hum ek Agent banayenge jo Tools rakhega — aapka pehla structural agent!"*

### 🎯 Today's goal
Composition ("has-a") samajhna aur ek Agent-with-Tools banana.

### 👨‍🏫 Concept 1 — composition = object ke andar object

> **📖 Technical definition — Composition:** Composition is a design approach where an object is built from other objects that it holds as attributes (a "has-a" relationship), rather than inheriting from them (an "is-a" relationship). It models systems as collaborating parts and is often more flexible than inheritance.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)    # Car ke ANDAR ek Engine object

    def start(self):
        return f"{self.brand}: {self.engine.start()}"

car = Car("Maruti", 80)
print(car.start())              # Maruti: Engine started
print(car.engine.horsepower)    # 80
```
*"Dekho `Car` ke andar ek `Engine` object hai (`self.engine`). Car 'HAS-A' engine. Yeh inheritance nahi — Car, Engine se inherit nahi karti, woh use RAKHTI hai. Yeh real-world ko zyada natural model karta hai."*

### 👨‍🏫 Concept 2 — IS-A vs HAS-A (kab kya?)
| Inheritance (IS-A) | Composition (HAS-A) |
|---|---|
| `Dog` IS-A `Animal` | `Car` HAS-A `Engine` |
| Type ka rishta | Parts ka rishta |
| `class Dog(Animal)` | `self.engine = Engine()` |
*"Rule: agar 'X ek tarah ka Y hai' → inheritance. Agar 'X ke paas Y hai' → composition. Agent ke paas tools HOTE hain (has-a), toh composition perfect hai."*

### 👨‍🏫 Concept 3 — ek object jo kai objects rakhe (list of objects)
```python
class Tool:
    def __init__(self, name):
        self.name = name

class Toolbox:
    def __init__(self):
        self.tools = []             # Toolbox HAS-A list of Tools

    def add_tool(self, tool):
        self.tools.append(tool)

    def list_tools(self):
        for tool in self.tools:
            print(f"- {tool.name}")

box = Toolbox()
box.add_tool(Tool("Hammer"))
box.add_tool(Tool("Screwdriver"))
box.list_tools()
# - Hammer
# - Screwdriver
```

### 🛠️ Mini Project — Agent with Tools (structural mock!)
*"Yeh week ka, balki ab tak ka, sabse important project hai. Hum ek asli Agent ka DHAANCHA banayenge — abstract Tool, kuch concrete tools, aur ek Agent jo unhe rakhta aur chalata hai. Yeh poore course ka core skeleton hai."*

```python
from abc import ABC, abstractmethod


class Tool(ABC):
    """Base class — har tool ka naam, description aur run() hona zaroori."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args):
        ...

    def __repr__(self):
        return f"Tool(name='{self.name}')"


class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("calculator", "Adds two numbers")

    def run(self, a: float, b: float) -> float:
        return a + b


class GreetTool(Tool):
    def __init__(self):
        super().__init__("greet", "Greets a person by name")

    def run(self, name: str) -> str:
        return f"Hello, {name}!"


class Agent:
    """An agent HAS-A list of tools (composition)."""
    def __init__(self, name: str):
        self.name = name
        self.tools = []                 # composition: agent holds tools

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def list_tools(self):
        print(f"{self.name}'s tools:")
        for tool in self.tools:
            print(f"  - {tool.name}: {tool.description}")

    def use_tool(self, tool_name: str, *args):
        for tool in self.tools:
            if tool.name == tool_name:      # naam se sahi tool dhoondho
                return tool.run(*args)
        return f"Tool '{tool_name}' not found"


# --- agent banao aur use karo ---
agent = Agent("Jarvis")
agent.add_tool(CalculatorTool())
agent.add_tool(GreetTool())

agent.list_tools()
# Jarvis's tools:
#   - calculator: Adds two numbers
#   - greet: Greets a person by name

print(agent.use_tool("calculator", 5, 3))    # 8
print(agent.use_tool("greet", "Asha"))       # Hello, Asha!
print(agent.use_tool("unknown"))             # Tool 'unknown' not found
```
*"DEKHO aapne kya banaya! Yeh poore OOP week ka nichod hai: abstraction (`Tool(ABC)`), inheritance (`CalculatorTool(Tool)`), polymorphism (har tool ka apna `run`), aur composition (Agent HAS-A tools). `use_tool` mein woh 'naam se tool dhoondho' wala loop — yeh ASLI agent ka tool-routing hai. Sirf LLM ka brain missing hai, jo hum aage jodenge!"*

### ❌ Common mistakes
```python
class Agent:
    tools = []          # ❌ class attribute — saare agents tools share kar lenge!
    # sahi: self.tools = [] __init__ ke andar (har agent ka apna)

agent.use_tool("calculator", 5)   # ❌ CalculatorTool.run ko 2 numbers chahiye
```

### 🔗 Agentic link
*"Yeh literally ek real agent ka structure hai. Real agents mein: Agent object tools rakhta hai (composition), har tool ek base se inherit karta hai (inheritance), sabka `run()` interface same hai (polymorphism), jise abstraction enforce karta hai. Aaj aapne agent ka KANKAAL (skeleton) khud banaya. Week 17 mein hum isme LLM ka brain daal denge!"*

### ✍️ Homework
1. Upar wale Agent project mein ek teesra tool add karo: `ReverseTool` jo string ulta kare.
2. Use agent mein add karke `use_tool("reverse", "hello")` test karo.
3. `Computer` class banao jo `CPU` aur `RAM` objects rakhe (composition).

**Answers:**
```python
# 1 & 2
class ReverseTool(Tool):
    def __init__(self):
        super().__init__("reverse", "Reverses a string")
    def run(self, text: str) -> str:
        return text[::-1]
agent.add_tool(ReverseTool())
print(agent.use_tool("reverse", "hello"))    # olleh

# 3
class CPU:
    def __init__(self, cores):
        self.cores = cores
class RAM:
    def __init__(self, size):
        self.size = size
class Computer:
    def __init__(self):
        self.cpu = CPU(8)
        self.ram = RAM(16)
pc = Computer()
print(pc.cpu.cores, pc.ram.size)     # 8 16
```

### 🏁 Week 8 wrap-up*"Yeh week aapne classes ko PROFESSIONAL banaya:*
- *`__str__`/`__repr__` — sundar, debuggable objects (Class 46)*
- *`__eq__`/`__len__` + class attributes (Class 47)*
- *classmethod/staticmethod — from_dict, utilities (Class 48)*
- *property — computed + validated attributes (Class 49)*
- *Composition + Agent-with-Tools project (Class 50)*

*Aapne ab POORA OOP (Week 7-8) cover kar liya, aur ek asli Agent ka skeleton bana diya! Yeh bahut bada milestone hai.*

> 🟢 **Buffer/revision suggestion:** *Aage badhne se pehle, Week 1–8 ke saare projects (converter, calculator, guessing game, contact book, tools.py, agent skeleton) ko memory se dobara banane ki koshish karo. Yeh foundation ko pakka karega.*

*Next week — ERRORS aur RESILIENCE: code jo fail hone par bhi sambhal jaaye (agents constantly fail hote hain!). Shabaash, agli class mein milte hain!"*

### 📝 Weekend revision task
Agent-with-Tools project ko blank file se dobara banao. Bonus: ek `WordCountTool` add karo aur agent ke saare tools `list_tools()` se dikhao.

---

## 🎤 Industry Interview Questions — Week 8

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between `__str__` and `__repr__`?**

`__str__` returns a human-friendly, readable string (used by `print()` and `str()`). `__repr__` returns an unambiguous, developer-facing string meant for debugging — ideally one that looks like valid code to recreate the object, e.g. `Message(role='user', content='hi')`. `repr()` and the interactive prompt use `__repr__`, and containers (like lists) show the `__repr__` of their elements. If you only implement one, implement `__repr__`, because Python falls back to it when `__str__` is missing.

**Q2. What is the difference between a class attribute and an instance attribute, and what's the common pitfall?**

A class attribute is defined on the class and shared by all instances; an instance attribute is set per object (usually in `__init__`) and belongs only to that object. The pitfall is a *mutable* class attribute, like `tools = []` at class level — every instance shares the same list, so appending via one instance affects all of them. Mutable per-object state must be created inside `__init__`.

**Q3. When would you use a `@classmethod`, a `@staticmethod`, and a regular instance method?**

An instance method (takes `self`) operates on a specific object's data. A `@classmethod` (takes `cls`) operates on the class itself — the classic use is an *alternative constructor* like `Message.from_dict(data)` that builds and returns an instance. A `@staticmethod` takes neither `self` nor `cls`; it's just a utility function grouped inside the class because it's logically related, but it doesn't use object or class state.

**Q4. What is `@property` and why use it instead of a public attribute or explicit getter/setter methods?**

`@property` lets a method be accessed like an attribute (`obj.area` instead of `obj.area()`), so you can start with a plain attribute and later add computed values or validation *without changing the calling code*. Compared to Java-style `get_x()`/`set_x()` methods, properties keep the clean attribute syntax while still allowing validation in the setter (e.g. rejecting a negative temperature). This is the Pythonic way to control attribute access.

**Q5. Why implement `__eq__`, and what must you remember about `__hash__`?**

By default two objects are "equal" only if they are the *same* object in memory. Implementing `__eq__` lets you define value-based equality (two `Message` objects with the same fields are equal). Important: if you override `__eq__`, Python sets `__hash__` to `None`, making instances unhashable (unusable in sets/dict keys). If you need them hashable, also implement `__hash__` consistently with `__eq__` — equal objects must have equal hashes.
