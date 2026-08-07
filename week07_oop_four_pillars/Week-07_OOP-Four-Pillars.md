# WEEK 7 — OOP: The Four Pillars (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> 🟡 **Pacing note:** *"Yeh week thoda naya aur abstract hai — pehli baar 'objects' ki soch aati hai. Hum SLOW chalenge. Agar pehli baar mein 100% clear na ho, normal hai. Concepts ko examples se baar-baar dohrayenge."*
>
> **Week promise:** *"Is week hum real-world cheezon ko CODE ke 'objects' mein badalna seekhenge. Yeh super important hai kyunki ek Agent, ek Tool, ek Message — sab 'objects' bante hain. OOP ke 4 pillars seekhenge: classes, encapsulation, inheritance, polymorphism, abstraction."*

---

## CLASS 41 — Classes & Objects

*"Ab tak humne data (variables) aur kaam (functions) ko ALAG rakha. Par real cheezein dono ko jodti hain — ek 'dog' ke paas data (naam, age) AUR kaam (bhaunkna) dono hote hain. OOP humein data + functions ko ek 'object' mein jodne deta hai. Aaj se soch badlegi."*

### 🎯 Today's goal
`class` define karna, `__init__`, `self`, aur objects banana.

### 👨‍🏫 Concept 1 — class = blueprint, object = asli cheez

> **📖 Technical definition — Class and object:** A class is a blueprint that defines the attributes (data) and methods (behaviour) shared by a kind of thing. An object is a concrete instance created from that class, holding its own attribute values. Object-oriented programming (OOP) bundles data and the functions that operate on it together.

*"Soch lo ek class ek BLUEPRINT (naksha) hai — jaise ghar ka naksha. Object us naksha se bana asli GHAR hai. Ek blueprint se hum kai ghar (objects) bana sakte hain."*
```python
class Dog:
    def __init__(self, name, age):
        self.name = name        # har dog ka apna naam
        self.age = age          # har dog ki apni age

    def bark(self):
        print(f"{self.name} says Woof!")

# objects (asli dogs) banao
dog1 = Dog("Tommy", 3)
dog2 = Dog("Bruno", 5)

dog1.bark()             # Tommy says Woof!
dog2.bark()             # Bruno says Woof!
print(dog1.name)        # Tommy
print(dog2.age)         # 5
```
*"`Dog` blueprint hai. `dog1` aur `dog2` us blueprint se bane do alag objects hain — alag naam, alag age, par dono `bark()` kar sakte hain."*

### 👨‍🏫 Concept 2 — `__init__` (object bante hi chalne wala setup)

> **📖 Technical definition — `__init__` (constructor):** `__init__` is a special method that Python calls automatically right after a new object is created. It initialises the object's starting attribute values from the arguments passed when the object is constructed.

*"`__init__` ek special method hai jo AUTOMATICALLY chalti hai jab aap naya object banate ho. Ise 'constructor' bolte hain. Yahan hum object ki shuruआti values set karte hain."*
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Asha", 85)     # __init__ yahan apne aap chalti hai
print(s.name)               # Asha
```
*"Jab aap `Student("Asha", 85)` likhte ho, Python turant `__init__` ko call karta hai with name="Asha", marks=85. Aapko khud `__init__()` likhne ki zaroorat nahi — yeh automatic hai."*

### 👨‍🏫 Concept 3 — `self` kya hai? (sabse confusing par simple)

> **📖 Technical definition — `self`:** `self` is the conventional name for the first parameter of every instance method. It refers to the specific object the method was called on, giving the method access to that object's own attributes and other methods. Python passes it automatically.

*"`self` ka matlab hai 'YE WALA object'. Jab `dog1.bark()` chalta hai, `self` = dog1. Jab `dog2.bark()` chalta hai, `self` = dog2. `self` se har object apne hi data tak pahunchta hai."*
```python
class Counter:
    def __init__(self):
        self.count = 0          # self.count = is object ka count

    def increase(self):
        self.count = self.count + 1     # is object ka count badhao

c = Counter()
c.increase()
c.increase()
print(c.count)          # 2
```
*"Rule yaad rakho: har method ka pehla parameter HAMESHA `self` hota hai. Aap use khud nahi bhejte — Python automatically bhejta hai. Aur object ke data ko hamesha `self.something` se access karo."*

### 👨‍🏫 Concept 4 — attributes vs methods

> **📖 Technical definition — Attribute vs method:** An attribute is a piece of data stored on an object (its state). A method is a function defined inside a class that operates on the object (its behaviour). Together they make up what an object "has" and what it "does."

- **Attribute** = object ka DATA (`self.name`, `self.age`). Noun.
- **Method** = object ka KAAM (`bark()`, `increase()`). Verb. (Method = function jo class ke andar hai.)

### 💻 Demo — BankAccount
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def show(self):
        print(f"{self.owner}'s balance: ₹{self.balance}")

acc = BankAccount("Asha", 1000)
acc.show()              # Asha's balance: ₹1000
acc.deposit(500)        # Deposited ₹500. New balance: ₹1500
acc.show()              # Asha's balance: ₹1500
```

### ❌ Common mistakes
```python
class Dog:
    def __init__(name, age):     # ❌ 'self' bhool gaye — pehla param self hona chahiye
        ...

class Dog:
    def __init__(self, name):
        name = name              # ❌ 'self.' bhool gaye — yeh object par save nahi hoga
        # sahi: self.name = name
```

### 🔗 Agentic link
*"Yeh week ka core idea: **ek Agent ek object hai.** Uske paas data (model, tools, memory) AUR kaam (`.run()`, `.add_tool()`) dono hote hain — ek `Agent` class mein bandhe. Aaj aapne us soch ki neev rakhi: cheezon ko data+behaviour wale objects ki tarah dekhna."*

### ✍️ Homework
1. Ek `Car` class banao with `brand`, `speed`, aur ek method `drive()` jo "BRAND is driving at SPEED" print kare.
2. Ek `Student` class with `name`, `marks`, aur method `report()` jo report print kare. 2 objects banao.
3. Ek `Circle` class with `radius` aur method `area()` jo area return kare.

**Answers:**
```python
# 1
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")
Car("Maruti", 80).drive()

# 2
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def report(self):
        print(f"{self.name} scored {self.marks}")
Student("Asha", 85).report()
Student("Rahul", 90).report()

# 3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
print(Circle(7).area())      # 153.93791
```

### 🔗 Agli class
*"Agli class — encapsulation: object ke andar ki cheezein 'chhupana' taaki koi galti se na bigaade. Pehla OOP pillar."*

---

## CLASS 42 — Encapsulation

*"Soch lo ek ATM machine. Aap paise nikaal sakte ho (button daba kar), par machine ke andar ka cash seedhe haath se nahi chhu sakte. Andar ki cheezein 'chhupi' hain, sirf safe buttons bahar hain. Yahi ENCAPSULATION hai — pehla pillar."*

### 🎯 Today's goal
Internal data chhupana (`_private` convention) aur safe methods se access dena.

### 👨‍🏫 Concept 1 — problem: seedha access khatarnak hai

> **📖 Technical definition — Encapsulation:** Encapsulation is the OOP principle of bundling data with the methods that operate on it and restricting direct outside access to that data. Internal state is marked private (by convention with a leading underscore) and changed only through controlled, validated methods.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

acc = BankAccount(1000)
acc.balance = -5000        # 😱 koi bhi balance ko kuch bhi bana sakta hai!
print(acc.balance)         # -5000  (galat, par koi rok nahi)
```
*"Dekho problem? `balance` seedha exposed hai, koi bhi use galat bana sakta hai. Humein ise PROTECT karna hai."*

### 👨‍🏫 Concept 2 — `_` (underscore) convention — "yeh private hai"
*"Python mein hum variable ke aage ek underscore `_` lagakar batate hain 'yeh internal hai, bahar se mat chhuо'. Yeh ek SHARAFAT ka rule hai (Python rok nahi lagata, par har developer ise samajhta hai)."*
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance       # _ = "private, mat chhuо"

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount

    def get_balance(self):
        return self._balance
```
*"`_balance` ka underscore bolta hai: 'isse seedhe mat chhedo, methods use karo.' `deposit()` aur `get_balance()` 'public interface' hain — safe darwaze jinse bahar wale baat karte hain."*

### 👨‍🏫 Concept 3 — validation (methods galat data rokte hain)
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive!")
            return
        self._balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
            return
        self._balance -= amount
        print(f"Withdrew ₹{amount}. Balance: ₹{self._balance}")

acc = BankAccount(1000)
acc.withdraw(500)       # Withdrew ₹500. Balance: ₹500
acc.withdraw(900)       # Insufficient funds!
acc.deposit(-100)       # Deposit must be positive!
```
*"Ab balance ko sirf SAHI tareeke se badla jaa sakta hai. Method ke andar rules (validation) lagaye, taaki kabhi galat state na bane. Yahi encapsulation ka asli faayda hai — data SAFE rehta hai."*

### 👨‍🏫 Concept 4 — `__` (double underscore) — aur strict
```python
class Secret:
    def __init__(self):
        self.__key = "hidden"        # double underscore — aur zyada protected

s = Secret()
# print(s.__key)      # ❌ AttributeError — seedhe access mushkil ho jaata hai
```
*"Double underscore Python ko bolta hai naam ko thoda 'chhupa' do (name mangling). Beginners ke liye single `_` kaafi hai — bas convention samajh lo. Double `__` advanced cases ke liye."*

### ❌ Common mistakes
```python
# encapsulation ka matlab _ lagana NAHI — methods se access dena hai
class A:
    def __init__(self):
        self._x = 5
a = A()
a._x = 999          # ❌ technically chalega, par yeh 'rule todna' hai — mat karo
# sahi: a.set_x(999) jaisा method banao validation ke saath
```

### 🔗 Agentic link
*"Ek agent ki internal state (memory, API keys, intermediate results) ko encapsulate karna zaroori hai — bahar wala code seedhe agent ka memory na bigaade. Hum ek saaf 'public interface' dete hain (`agent.run()`, `agent.add_tool()`) aur andar ki cheezein `_private` rakhte hain. Yeh agents ko safe aur predictable banata hai."*

### ✍️ Homework
1. `BankAccount` mein validation add karo taaki balance kabhi negative na ho.
2. Ek `Temperature` class banao with `_celsius`; ek method `set_celsius` jo -273 se kam value reject kare.
3. Ek `Password` class with `_password` aur ek `check(guess)` method jo True/False de.

**Answers:**
```python
# 2
class Temperature:
    def __init__(self):
        self._celsius = 0
    def set_celsius(self, value):
        if value < -273:
            print("Below absolute zero — invalid!")
            return
        self._celsius = value
    def get_celsius(self):
        return self._celsius
t = Temperature()
t.set_celsius(-300)     # Below absolute zero — invalid!
t.set_celsius(25)
print(t.get_celsius())  # 25

# 3
class Password:
    def __init__(self, password):
        self._password = password
    def check(self, guess):
        return guess == self._password
p = Password("secret123")
print(p.check("wrong"))      # False
print(p.check("secret123"))  # True
```

### 🔗 Agli class
*"Agli class — inheritance: ek class doosri se 'wirasat' (properties) le. Doosra pillar, aur frameworks ki neev."*

---

## CLASS 43 — Inheritance

*"Soch lo: Dog, Cat, Cow — sab ALAG hain, par sabme kuch COMMON hai (sab khaate hain, sab sote hain). Har class mein woh common code dobara likhna? Bewakoofi! INHERITANCE se ek 'parent' class banao with common cheezein, aur baaki usse 'wirasat' lein. Doosra pillar."*

### 🎯 Today's goal
Parent class se inherit karna, aur `super()` use karna.

### 👨‍🏫 Concept 1 — basic inheritance

> **📖 Technical definition — Inheritance:** Inheritance lets a child (derived) class reuse the attributes and methods of a parent (base) class. The child automatically gains the parent's behaviour and can add new members or modify inherited ones, avoiding duplicated code.

```python
class Animal:                      # parent class
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):                 # Dog, Animal se inherit karta hai
    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Tommy")
d.eat()         # Tommy is eating    — Animal se mila!
d.sleep()       # Tommy is sleeping  — Animal se mila!
d.bark()        # Tommy says Woof!   — Dog ka apna
```
*"`class Dog(Animal):` ka matlab 'Dog, Animal ka bachcha hai'. Dog ko Animal ke saare methods (eat, sleep) MUFT mein mil gaye, aur Dog ne apna `bark` bhi add kiya. Code dobara likhne se bach gaye!"*

### 👨‍🏫 Concept 2 — parent-child rishta (vocab)
- **Parent / Base / Super class** = upar wali (`Animal`).
- **Child / Derived / Sub class** = neeche wali (`Dog`).
- *"Child ko parent ka SAB kuch milta hai, aur woh apna EXTRA bhi add kar sakta hai."*

### 👨‍🏫 Concept 3 — `super()` (parent ka setup use karo)

> **📖 Technical definition — `super()`:** `super()` returns a proxy to the parent class, letting a child call the parent's methods (most commonly `super().__init__(...)`). This reuses the parent's setup instead of duplicating it in the child.

*"Agar child ko apna `__init__` chahiye PAR parent ka setup bhi, toh `super()` se parent ka `__init__` bula lo."*
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # parent ka __init__ chalao (name set karega)
        self.breed = breed         # phir apna extra

d = Dog("Tommy", "Labrador")
print(d.name)       # Tommy   — parent ne set kiya
print(d.breed)      # Labrador — child ne set kiya
```
*"`super().__init__(name)` ka matlab: 'parent (Animal), tu `name` sambhal le.' Phir child apna `breed` add karta hai. Isse hum parent ka code dohrate nahi — bas use karte hain."*

### 💻 Demo — Vehicle family
```python
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    def info(self):
        print(f"{self.brand} with {self.wheels} wheels")

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 4)     # car ke hamesha 4 wheels

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, 2)     # bike ke hamesha 2 wheels

Car("Maruti").info()      # Maruti with 4 wheels
Bike("Hero").info()       # Hero with 2 wheels
```

### ❌ Common mistakes
```python
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed        # ❌ super().__init__ bhool gaye → self.name set nahi hua
        # ab d.name use karoge toh AttributeError

class Dog(Animal)                 # ❌ colon bhool gaye
```

### 🔗 Agentic link
*"Yeh BAHUT important hai: agentic AI frameworks (LangChain, etc.) aapse expect karte hain ki aap unke `BaseTool` ya `BaseAgent` class se INHERIT karo. Aap likhte ho `class MyTool(BaseTool):` aur aapko saari base functionality muft mil jaati hai, aap sirf apna khaas part add karte ho. Aaj aapne us pattern ki neev rakhi."*

### ✍️ Homework
1. `Animal` parent banao; `Cat` aur `Cow` children banao, har ek apni awaaz wala method.
2. `Shape` parent (with `name`); `Square` aur `Rectangle` children with `super()`.
3. `Employee` parent (name, salary); `Manager` child jo `super()` use kare aur ek `team_size` add kare.

**Answers:**
```python
# 1
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} eats")
class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow")
class Cow(Animal):
    def sound(self):
        print(f"{self.name} says Moo")
Cat("Kitty").sound()      # Kitty says Meow
Cow("Lakshmi").sound()    # Lakshmi says Moo

# 3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
m = Manager("Asha", 90000, 5)
print(m.name, m.salary, m.team_size)    # Asha 90000 5
```

### 🔗 Agli class
*"Agli class — polymorphism: ek hi naam ka method, alag-alag objects mein alag kaam. Teesra pillar — aur agents ke liye genius."*

---

## CLASS 44 — Polymorphism

*"Bada shabd, simple idea. 'Poly' = many, 'morph' = shapes. Polymorphism = ek hi method ka naam, par alag objects mein alag behaviour. Jaise har animal ka `speak()` hota hai, par dog 'Woof' bolta hai aur cat 'Meow'. Same naam, alag kaam. Teesra pillar."*

### 🎯 Today's goal
Method overriding aur polymorphism ka practical use.

### 👨‍🏫 Concept 1 — method overriding (child parent ko badle)

> **📖 Technical definition — Polymorphism and method overriding:** Polymorphism lets objects of different classes respond to the same method call in their own way. Method overriding is a child class redefining a method it inherited, so calling that method on the child runs the child's version.

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):                # parent wala speak OVERRIDE kiya
        print("Woof!")

class Cat(Animal):
    def speak(self):                # apna alag speak
        print("Meow!")

Dog().speak()       # Woof!
Cat().speak()       # Meow!
Animal().speak()    # Some generic sound
```
*"Dono Dog aur Cat ne parent ka `speak` apne hisaab se badal diya (override). Same naam `speak`, par alag behaviour. Yahi polymorphism ka dil hai."*

### 👨‍🏫 Concept 2 — asli power: same code, alag objects
```python
animals = [Dog(), Cat(), Dog(), Cat()]

for animal in animals:
    animal.speak()      # har object apna sahi speak chalata hai!
```
Output:
```
Woof!
Meow!
Woof!
Meow!
```
*"Yeh KAMAAL hai: hum sabko ek loop mein `.speak()` bolte hain, aur har object KHUD jaanta hai uska sahi version kya hai. Humein `if dog → woof, if cat → meow` likhne ki ZAROORAT NAHI. Code saaf aur flexible ho jaata hai."*

### 👨‍🏫 Concept 3 — shapes example (classic)
```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6), Circle(2)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```
Output:
```
Area: 78.54
Area: 24.00
Area: 12.57
```
*"Alag-alag shapes, par sab `.area()` ka jawaab dete hain — har ek apne formula se. Ek loop sabko handle karta hai."*

### ❌ Common mistakes
```python
class Dog(Animal):
    def Speak(self):        # ❌ capital S — alag method ban gaya, override nahi hua
        print("Woof")
# parent ka exact naam (speak) match karna zaroori override ke liye
```

### 🔗 Agentic link
*"Yeh agents ke liye genius hai: aapke paas kai tools hote hain (CalculatorTool, SearchTool, WeatherTool), aur SAB mein ek hi method `.run()` hota hai — par har ek alag kaam karta hai. Agent bas `tool.run(input)` bolta hai, aur sahi tool apna kaam karta hai. Koi lamba `if/elif` nahi. Ek interface, kai behaviours — yahi polymorphism agents ko clean banata hai."*

### ✍️ Homework
1. `Shape` parent; `Triangle` aur `Square` children, dono ka apna `area()`.
2. Ek list mein alag shapes daalo aur loop se sabka area print karo.
3. `Employee` parent with `work()`; `Developer` aur `Designer` children jo alag-alag work print karein.

**Answers:**
```python
# 1 & 2
class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
for s in [Square(4), Triangle(6, 8)]:
    print(s.area())     # 16  then  24.0

# 3
class Employee:
    def work(self):
        print("Working")
class Developer(Employee):
    def work(self):
        print("Writing code")
class Designer(Employee):
    def work(self):
        print("Designing UI")
for e in [Developer(), Designer()]:
    e.work()
```

### 🔗 Agli class
*"Agli class — abstraction: ek 'rule' banana ki har tool ko `run()` likhna ZAROORI hai. Chautha aur aakhri pillar, phir practice."*

---

## CLASS 45 — Abstraction (Practice Class)

*"Aakhri pillar: ABSTRACTION. Idea: ek 'contract' banao jo kahe 'har tool ko ek `run()` method ZAROOR hona chahiye'. Agar koi bhool jaaye, Python turant error de — runtime par crash hone se pehle. Yeh bade projects ko organized rakhta hai."*

### 🎯 Today's goal
Abstract base class (`ABC`, `@abstractmethod`) se ek required interface banana.

### 👨‍🏫 Concept 1 — problem: bina rule ke galti
*"Polymorphism mein hum maante hain har shape ka `area()` hoga. Par agar koi developer bhool jaaye? Tab galat result ya crash. Hum chahte hain Python BHOOL ko PEHLE HI pakad le."*

### 👨‍🏫 Concept 2 — Abstract Base Class (ABC)

> **📖 Technical definition — Abstraction and abstract base class:** Abstraction means defining *what* an object must be able to do while leaving *how* to the concrete classes. An abstract base class (via `ABC`) declares required methods with `@abstractmethod`; it cannot be instantiated directly, and any subclass that fails to implement those methods cannot be instantiated either.

*"`ABC` se hum ek aisा blueprint banate hain jo KHUD object nahi ban sakta — sirf inherit karne ke liye. `@abstractmethod` se hum kehte hain 'yeh method har child mein ZAROORI hai'."*
```python
from abc import ABC, abstractmethod

class Tool(ABC):                    # abstract base class
    @abstractmethod
    def run(self, a, b):
        ...                         # koi body nahi — sirf 'rule' hai

class Adder(Tool):
    def run(self, a, b):
        return a + b                # apna run implement kiya

calc = Adder()
print(calc.run(2, 3))               # 5
```
*"`Tool(ABC)` ek 'contract' hai: 'jo bhi mujhse inherit kare, use `run()` likhna ZAROORI hai.' `Adder` ne `run` likha, toh chal gaya."*

### 👨‍🏫 Concept 3 — rule todoge toh turant error
```python
from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def run(self, input):
        ...

class BrokenTool(Tool):
    pass                            # run() likhna BHOOL gaye!

bt = BrokenTool()                   # ❌ TypeError: Can't instantiate abstract class
                                    #    BrokenTool with abstract method run
```
*"Dekha? Python ne object banane se HI MANA kar diya, kyunki `run()` missing hai. Yeh ek safety net hai — galti runtime par nahi, turant pakdi gayi. Bade teams mein yeh bahut bachata hai."*

### 👨‍🏫 Concept 4 — abstraction ka asli matlab
*"Abstraction ka matlab: 'KYA hona chahiye' define karo, 'KAISE' ko children par chhod do. `Tool` kehta hai 'har tool run hoga' (kya), par har specific tool decide karta hai 'kaise run hoga'. Yeh ek saaf, predictable system banata hai."*

### 💻 Demo — Shape contract
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

for shape in [Circle(5), Square(4)]:
    print(f"{shape.area():.2f}")    # 78.54  then  16.00

# Shape()    # ❌ TypeError — abstract class ka object nahi ban sakta
```

### ❌ Common mistakes
```python
from abc import ABC, abstractmethod
class Tool(ABC):
    @abstractmethod
    def run(self): ...

t = Tool()              # ❌ abstract class ka object nahi banta — pehle inherit karo

class MyTool(Tool):
    def execute(self):  # ❌ galat naam (run nahi) → abstract method abhi bhi missing
        ...
```

### 🔗 Agentic link
*"Yeh agent frameworks ka asli dil hai: woh ek abstract `BaseTool` dete hain with `@abstractmethod run()`. Aap usse inherit karte ho, aur agar `run()` likhna bhool jao, framework turant error deta hai — aapka tola galat agent banne se pehle ruk jaata hai. 'Har tool ko run() lagana hi padega' — yeh rule abstraction se enforce hota hai. Aapne ab OOP ke chaaron pillars jaan liye!"*

### ✍️ Homework
1. Ek abstract `Animal` banao with abstract `sound()`. `Dog` aur `Cat` se implement karo.
2. Jaan-boojh kar ek child banao jo `sound()` na likhe — error padho.
3. Ek abstract `PaymentMethod` with abstract `pay(amount)`; `Cash` aur `Card` se implement karo.

**Answers:**
```python
# 1 & 2
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self): ...
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow"
print(Dog().sound())     # Woof
print(Cat().sound())     # Meow
# class Bird(Animal): pass
# Bird()   # TypeError: abstract method sound missing

# 3
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount): ...
class Cash(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} in cash"
class Card(PaymentMethod):
    def pay(self, amount):
        return f"Paid ₹{amount} by card"
print(Cash().pay(500))   # Paid ₹500 in cash
print(Card().pay(999))   # Paid ₹999 by card
```

### 🏁 Week 7 wrap-up*"Aapne OOP ke CHAARON pillars seekh liye — yeh ek bada achievement hai:*
- *Classes & objects — blueprint + asli cheez (Class 41)*
- *Encapsulation — data chhupana aur protect karna (Class 42)*
- *Inheritance — parent se wirasat (Class 43)*
- *Polymorphism — ek naam, alag behaviour (Class 44)*
- *Abstraction — required interface ka contract (Class 45)*

*Yeh thoda mushkil week tha — agar sab 100% clear na ho, weekend pe dobara dekho, koi jaldi nahi. Next week in classes ko aur Pythonic (saaf aur professional) banayenge. Bahut shaandar kaam!"*

### 📝 Weekend revision task
Ek chhota system banao: abstract `Tool` (with `run()`), aur 2 concrete tools `Calculator` aur `Greeter`. Ek list mein dono daalo aur loop se `run()` call karo. Yeh next weeks mein asli agent banega!

---

## 🎤 Industry Interview Questions — Week 7

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between a class and an object, and what are `__init__` and `self`?**

A class is a blueprint that defines attributes and behavior; an object (instance) is a concrete thing built from that blueprint. `__init__` is the initializer that runs when you create an instance and sets up its starting attributes. `self` is the reference to the specific instance, passed automatically as the first parameter of every instance method, so the method can read and modify that object's own data.

**Q2. Name the four pillars of OOP and explain each in one line.**

**Encapsulation** — bundling data with the methods that operate on it and hiding internal details. **Inheritance** — a child class reusing and extending a parent class. **Polymorphism** — the same method name behaving correctly on different types (one interface, many implementations). **Abstraction** — exposing a simple, essential interface while hiding complex implementation, often via abstract base classes.

**Q3. How does Python implement encapsulation, given it has no truly "private" members?**

By convention and name mangling rather than hard access control. A single underscore (`_value`) signals "internal, please don't touch" but is not enforced. A double underscore (`__value`) triggers *name mangling* — Python renames it to `_ClassName__value`, which discourages accidental access and avoids clashes in subclasses. Real validation/encapsulation is achieved with properties (getters/setters) rather than blocking access outright.

**Q4. Inheritance vs composition — which should you prefer and why?**

Prefer composition ("has-a": an object holds other objects) over inheritance ("is-a": a subclass extends a parent) in most cases. Deep inheritance hierarchies are rigid and create tight coupling, whereas composition is flexible and easier to change and test. Use inheritance only when there is a genuine "is-a" relationship and you want to share/override behavior. This is the classic guideline: "favor composition over inheritance."

**Q5. What is an abstract base class (ABC) and why use one?**

An ABC (from the `abc` module, with `@abstractmethod`) defines a contract: it cannot be instantiated directly, and any concrete subclass *must* implement the abstract methods or Python raises a `TypeError`. This guarantees a consistent interface across implementations — for example an abstract `Tool` with a `run()` method ensures every tool your agent uses is callable the same way, so you can treat them polymorphically in a loop.
