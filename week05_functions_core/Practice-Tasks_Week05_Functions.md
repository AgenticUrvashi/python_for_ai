# PRACTICE PROJECTS — Week 5 (Functions) · English + हिंदी

> **Note (EN):** These 20 real-world practice projects use ONLY Week 5 concepts — `def`, `return`, parameters, default values, keyword arguments, `*args`, `**kwargs`, and the mutable-default trap (`None` sentinel). Solve them yourself — that is how real skill is built.
>
> **नोट (हिंदी):** ये 20 प्रैक्टिस प्रोजेक्ट सिर्फ़ Week 5 के concepts पर आधारित हैं — `def`, `return`, parameters, default values, keyword arguments, `*args`, `**kwargs`, और mutable-default trap (`None` sentinel)। इन्हें खुद हल करो — असली स्किल इसी से बनती है।
>
> **Rules / नियम:**
> - Write each task in a fresh `.py` file. / हर task को नई `.py` file में लिखो।
> - Every function must use `return` (not `print`) unless the task clearly asks to print. / हर function `return` करे (print नहीं), जब तक task साफ़ न कहे कि print करना है।
> - Try for at least 15–20 minutes before looking at the **Answer Key** at the bottom. / नीचे दिए **Answer Key** को देखने से पहले कम से कम 15–20 मिनट खुद कोशिश करो।
>
> **Difficulty / कठिनाई:** 🟢 Easy → 🟡 Medium → 🔴 Hard. Do them in order. / क्रम में करो।

---

## 🟢 EASY — `def`, parameters, `return` (Class 31)

### Project 1 — Room Area Calculator
- **EN:** Write a function `room_area(length, width)` that returns the area of a room. Use it to find the area of 3 different rooms and print each result.
- **हिंदी:** एक function `room_area(length, width)` बनाओ जो कमरे का area **return** करे। इसे 3 अलग-अलग कमरों का area निकालने के लिए इस्तेमाल करो और हर result print करो।
- **Concepts:** `def`, two parameters, `return`, function call
- **Hint:** `return length * width`. Print the call: `print(room_area(10, 12))`.

---

### Project 2 — Temperature Converter
- **EN:** Write a function `celsius_to_f(c)` that converts Celsius to Fahrenheit and **returns** the value. Test it with 0, 37, and 100 degrees.
- **हिंदी:** एक function `celsius_to_f(c)` बनाओ जो Celsius को Fahrenheit में बदल कर value **return** करे। इसे 0, 37 और 100 डिग्री पर test करो।
- **Concepts:** `def`, arithmetic, `return`
- **Hint:** Formula: `(c * 9 / 5) + 32`.

---

### Project 3 — Simple Interest Calculator
- **EN:** Write a function `simple_interest(principal, rate, years)` that returns the simple interest `(P × R × T) / 100`. Print interest for ₹10000 at 5% for 3 years.
- **हिंदी:** एक function `simple_interest(principal, rate, years)` बनाओ जो simple interest `(P × R × T) / 100` **return** करे। ₹10000 पर 5% की दर से 3 साल का interest print करो।
- **Concepts:** three parameters, `return`
- **Hint:** `return (principal * rate * years) / 100`.

---

### Project 4 — Greeting Card Maker
- **EN:** Write a function `make_greeting(name, occasion)` that **returns** a message like `"Happy Diwali, Asha!"`. Do NOT print inside the function — return the string and print it outside.
- **हिंदी:** एक function `make_greeting(name, occasion)` बनाओ जो `"Happy Diwali, Asha!"` जैसा message **return** करे। Function के अंदर print मत करो — string return करो और बाहर print करो।
- **Concepts:** f-string, `return` vs `print`
- **Hint:** `return f"Happy {occasion}, {name}!"`.

---

### Project 5 — Tip Calculator
- **EN:** Write a function `tip_amount(bill, percent)` that returns how much tip to pay. Then print the total bill (bill + tip) for a ₹800 bill at 10%.
- **हिंदी:** एक function `tip_amount(bill, percent)` बनाओ जो tip की रकम **return** करे। फिर ₹800 के bill पर 10% tip के साथ कुल bill (bill + tip) print करो।
- **Concepts:** `return`, using the returned value in more maths
- **Hint:** `return bill * percent / 100`, then `total = bill + tip_amount(800, 10)`.

---

### Project 6 — Even or Odd Checker
- **EN:** Write a function `is_even(n)` that **returns** `True` if the number is even, else `False`. Use it in a loop to print which numbers in `[3, 8, 15, 22, 41]` are even.
- **हिंदी:** एक function `is_even(n)` बनाओ जो number even होने पर `True`, वरना `False` **return** करे। इसे loop में इस्तेमाल करके बताओ `[3, 8, 15, 22, 41]` में कौन-से numbers even हैं।
- **Concepts:** returning a boolean, `%`, using a function in a loop
- **Hint:** `return n % 2 == 0`.

---

### Project 7 — Discount Price Calculator
- **EN:** Write a function `final_price(price, discount_percent)` that returns the price after discount. Print the final price of a ₹1500 item with 20% off.
- **हिंदी:** एक function `final_price(price, discount_percent)` बनाओ जो discount के बाद की कीमत **return** करे। ₹1500 के item पर 20% छूट के बाद final price print करो।
- **Concepts:** `return`, percentage maths
- **Hint:** `return price - (price * discount_percent / 100)`.

---

## 🟡 MEDIUM — defaults, keyword arguments, `*args`, `**kwargs` (Class 32–33)

### Project 8 — Smart Greeting (default value)
- **EN:** Write `greet(name, greeting="Hello")` where `greeting` has a default. Call it once with only a name, and once with a custom greeting like `"Namaste"`.
- **हिंदी:** `greet(name, greeting="Hello")` बनाओ जिसमें `greeting` का default हो। इसे एक बार सिर्फ़ name के साथ, और एक बार custom greeting जैसे `"Namaste"` के साथ call करो।
- **Concepts:** default parameter value
- **Hint:** `return f"{greeting}, {name}!"`. Calling `greet("Asha")` uses the default.

---

### Project 9 — Pizza Order System (defaults + keyword args)
- **EN:** Write `order_pizza(item, qty=1, size="medium")`. Show 3 orders: only item; item + qty; item + `size="large"` using a keyword argument.
- **हिंदी:** `order_pizza(item, qty=1, size="medium")` बनाओ। 3 orders दिखाओ: सिर्फ़ item; item + qty; और item + `size="large"` keyword argument से।
- **Concepts:** multiple defaults, positional vs keyword arguments
- **Hint:** `return f"{qty} {size} {item}"`. Try `order_pizza("pizza", size="large")`.

---

### Project 10 — Power Function (default exponent)
- **EN:** Write `power(base, exp=2)` that returns `base ** exp`. By default it squares; but `power(2, 3)` should give 8.
- **हिंदी:** `power(base, exp=2)` बनाओ जो `base ** exp` **return** करे। Default में यह square करे; पर `power(2, 3)` का जवाब 8 आए।
- **Concepts:** default value, `**` operator
- **Hint:** `return base ** exp`. `power(5)` → 25.

---

### Project 11 — Shopping Cart Total (`*args`)
- **EN:** Write `cart_total(*prices)` that returns the sum of any number of item prices. Test it with 3 prices and with 6 prices.
- **हिंदी:** `cart_total(*prices)` बनाओ जो कितने भी item prices का जोड़ **return** करे। इसे 3 prices और 6 prices के साथ test करो।
- **Concepts:** `*args`, `sum()`
- **Hint:** `return sum(prices)`. Inside, `prices` is a tuple.

---

### Project 12 — Class Average (`*args` with a guard)
- **EN:** Write `average(*marks)` that returns the average of any number of marks. If called with no marks, return 0 (avoid divide-by-zero).
- **हिंदी:** `average(*marks)` बनाओ जो कितने भी marks का average **return** करे। अगर बिना marks के call हो तो 0 return करो (divide-by-zero से बचो)।
- **Concepts:** `*args`, `len()`, guard condition
- **Hint:** `if len(marks) == 0: return 0` first, then `return sum(marks) / len(marks)`.

---

### Project 13 — User Profile Builder (`**kwargs`)
- **EN:** Write `show_profile(**details)` that prints each detail as `key: value`. Call it with `name`, `age`, and `city`.
- **हिंदी:** `show_profile(**details)` बनाओ जो हर detail को `key: value` की तरह print करे। इसे `name`, `age`, और `city` के साथ call करो।
- **Concepts:** `**kwargs`, dict `.items()`, loop
- **Hint:** `for key, value in details.items(): print(f"{key}: {value}")`.

---

### Project 14 — LLM Message Maker (default + real AI shape)
- **EN:** Write `make_message(text, role="user")` that **returns** a dict `{"role": role, "content": text}`. Make a normal user message and a `role="system"` message. (This is exactly how AI chat messages look!)
- **हिंदी:** `make_message(text, role="user")` बनाओ जो dict `{"role": role, "content": text}` **return** करे। एक normal user message और एक `role="system"` message बनाओ। (AI chat messages बिल्कुल ऐसे ही दिखते हैं!)
- **Concepts:** default value, returning a dict, agentic link
- **Hint:** `return {"role": role, "content": text}`.

---

## 🔴 HARD — mutable-default trap, refactoring, combining (Class 34–35)

### Project 15 — Safe Shopping Cart (mutable-default trap)
- **EN:** Write `add_item(item, cart=None)` correctly so that each fresh call (without a cart) starts with an EMPTY cart. Call it 3 separate times and show each returns only its own item. (Do NOT use `cart=[]` — explain in a comment why.)
- **हिंदी:** `add_item(item, cart=None)` सही तरीके से बनाओ ताकि हर नई call (बिना cart के) खाली cart से शुरू हो। इसे 3 अलग बार call करके दिखाओ कि हर बार सिर्फ़ अपना item आता है। (`cart=[]` मत इस्तेमाल करो — comment में कारण लिखो।)
- **Concepts:** mutable default trap, `None` sentinel, `is None`
- **Hint:** `if cart is None: cart = []` — this makes a fresh list every call.

---

### Project 16 — Chat History Appender (no data leak)
- **EN:** Write `add_message(text, history=None)` that appends `{"role": "user", "content": text}` to the history and returns it. Start two SEPARATE conversations and prove their histories do not mix.
- **हिंदी:** `add_message(text, history=None)` बनाओ जो `{"role": "user", "content": text}` को history में जोड़ कर उसे return करे। दो अलग बातचीत शुरू करके साबित करो कि उनकी history आपस में नहीं मिलती।
- **Concepts:** `None` default, list of dicts, `.append()`
- **Hint:** `if history is None: history = []` — otherwise both chats share one list (a privacy bug!).

---

### Project 17 — Calculator Refactor (many small functions)
- **EN:** Refactor a calculator into functions: `add`, `subtract`, `multiply`, `divide` (handle divide-by-zero by returning a message). Then write `calculate(a, b, op)` that calls the right one based on `op` (`"+"`, `"-"`, `"*"`, `"/"`).
- **हिंदी:** Calculator को functions में बाँटो: `add`, `subtract`, `multiply`, `divide` (divide-by-zero पर message return करो)। फिर `calculate(a, b, op)` बनाओ जो `op` (`"+"`, `"-"`, `"*"`, `"/"`) के हिसाब से सही function call करे।
- **Concepts:** many functions, dispatch with `if/elif` or `match`, `return`
- **Hint:** In `divide`, `if b == 0: return "Cannot divide by zero"`.

---

### Project 18 — Grade Report (one function, many students)
- **EN:** Write `get_grade(marks)` returning `"A"/"B"/"C"/"D"`. Then loop over a dict of students `{"Asha": 92, "Rahul": 70, "Priya": 81}` and print each student's grade using the function.
- **हिंदी:** `get_grade(marks)` बनाओ जो `"A"/"B"/"C"/"D"` **return** करे। फिर students के dict `{"Asha": 92, "Rahul": 70, "Priya": 81}` पर loop चलाकर हर student का grade function से print करो।
- **Concepts:** `return`, `if/elif/else`, reusing a function in a loop, dict `.items()`
- **Hint:** `>= 90 → A`, `>= 75 → B`, `>= 60 → C`, else `D`.

---

### Project 19 — Restaurant Bill (combine everything)
- **EN:** Write `restaurant_bill(*prices, tax=5, tip=0)` that returns the final total: sum of all item prices, plus `tax`%, plus `tip`%. Call it with `tax` defaulted and `tip=10` passed as a keyword argument.
- **हिंदी:** `restaurant_bill(*prices, tax=5, tip=0)` बनाओ जो final total **return** करे: सभी item prices का जोड़, फिर `tax`%, फिर `tip`%। इसे एक बार `tax` को default रखते हुए और `tip=10` keyword argument देकर call करो।
- **Concepts:** `*args` + keyword-only-style defaults together, percentage maths
- **Hint:** `subtotal = sum(prices)`, then add `subtotal * tax / 100` and `subtotal * tip / 100`.

---

### Project 20 — Build Your First Tools Library (capstone)
- **EN:** Create a file `my_tools.py` with 4 reusable functions, each returning a value: `celsius_to_f(c)`, `bmi(weight, height)`, `is_prime(n)`, and `word_count(text)`. Test all four and print the results. This is the seed of your own "AI tools" library!
- **हिंदी:** एक file `my_tools.py` बनाओ जिसमें 4 reusable functions हों, हर एक value **return** करे: `celsius_to_f(c)`, `bmi(weight, height)`, `is_prime(n)`, और `word_count(text)`। चारों को test करके results print करो। यह आपकी अपनी "AI tools" library की शुरुआत है!
- **Concepts:** multiple functions, `return`, loops/flags inside functions, `.split()`
- **Hint:** For `is_prime`, use a flag: assume prime, loop `2..n-1`, if any divides evenly set flag `False`. For `word_count`, `return len(text.split())`.

---

## 🚀 CONFIDENCE BUILDERS — bigger projects (20+ lines each)

> **EN:** These 10 projects need **more than 20 lines** of code and combine several functions into one working program. This is where real confidence comes from — building complete mini-apps! Use only functions + earlier-week tools (loops, dicts, lists, `while`, `input`).
> **हिंदी:** इन 10 projects में **20 से ज़्यादा lines** का code चाहिए और कई functions मिलकर एक चलने वाला program बनाते हैं। असली confidence यहीं से आता है — पूरे mini-app बनाने से! सिर्फ़ functions + पिछले हफ़्तों के tools (loops, dicts, lists, `while`, `input`) इस्तेमाल करो।

---

### Project 21 — ATM Machine Simulator
- **EN:** Build an ATM with functions `check_balance(balance)`, `deposit(balance, amount)`, and `withdraw(balance, amount)` (block overdraft with a message). Run a `while` menu: 1) Balance 2) Deposit 3) Withdraw 4) Exit. Keep updating the balance from the returned values.
- **हिंदी:** एक ATM बनाओ जिसमें functions हों `check_balance(balance)`, `deposit(balance, amount)`, और `withdraw(balance, amount)` (पैसे कम हों तो message देकर रोको)। एक `while` menu चलाओ: 1) Balance 2) Deposit 3) Withdraw 4) Exit. हर बार return की गई value से balance update करते रहो।
- **Concepts:** multiple functions, `return`, `while` menu, `if/elif/else`
- **Hint:** In `withdraw`, `if amount > balance: return balance` (unchanged) with a warning; else `return balance - amount`.

---

### Project 22 — Student Report Card System
- **EN:** Write `total(marks)`, `average(marks)`, and `grade(avg)` functions. Loop over a list of students (each a dict with `name` and a list of 3 subject marks) and print a full report line for each. At the end print the class topper.
- **हिंदी:** `total(marks)`, `average(marks)`, और `grade(avg)` functions बनाओ। students की list (हर एक dict जिसमें `name` और 3 subjects के marks की list हो) पर loop चलाकर हर student की पूरी report line print करो। आख़िर में class topper print करो।
- **Concepts:** functions on lists, loop over list of dicts, running max
- **Hint:** `total` = `sum(marks)`, `average` = `total / len`. Track topper with a max-average variable.

---

### Project 23 — Quiz Game with Scoring
- **EN:** Make a quiz. Store questions as a list of dicts (`question`, `answer`). Write `ask(question, answer)` that takes the user's input and returns `1` if correct else `0`. Loop all questions, add up the score with a `score` accumulator, then print a final result with a pass/fail message.
- **हिंदी:** एक quiz बनाओ। questions को dicts की list में रखो (`question`, `answer`)। `ask(question, answer)` बनाओ जो user का input लेकर सही होने पर `1` वरना `0` return करे। सभी questions पर loop चलाओ, `score` accumulator से जोड़ो, फिर pass/fail message के साथ final result print करो।
- **Concepts:** list of dicts, function returning a number, accumulator, `input()`
- **Hint:** `return 1 if user.strip().lower() == answer.lower() else 0`.

---

### Project 24 — Simple Banking (multiple accounts)
- **EN:** Use a dict `accounts = {"Asha": 5000, "Rahul": 3000}`. Write `deposit(accounts, name, amount)` and `withdraw(accounts, name, amount)` that update and return the dict (check the account exists and enough balance). Run a menu to operate on any account and always show the updated balances.
- **हिंदी:** एक dict `accounts = {"Asha": 5000, "Rahul": 3000}` इस्तेमाल करो। `deposit(accounts, name, amount)` और `withdraw(accounts, name, amount)` बनाओ जो dict को update करके return करें (account मौजूद है और balance काफ़ी है — check करो)। किसी भी account पर काम करने के लिए menu चलाओ और हमेशा updated balances दिखाओ।
- **Concepts:** dict as shared state, functions modifying and returning a dict, validation
- **Hint:** `if name not in accounts: return accounts` with a message; guard `amount > accounts[name]` in withdraw.

---

### Project 25 — Restaurant Ordering System
- **EN:** Store a menu as a dict `{"pizza": 200, "burger": 120, "coke": 50}`. Write `add_to_order(order, item)` (returns updated order list) and `bill(order, menu, tax=5)` (returns total with tax). Run a menu loop to add items, then print an itemised bill.
- **हिंदी:** menu को dict `{"pizza": 200, "burger": 120, "coke": 50}` में रखो। `add_to_order(order, item)` बनाओ (updated order list return करे) और `bill(order, menu, tax=5)` (tax के साथ total return करे)। items जोड़ने के लिए menu loop चलाओ, फिर itemised bill print करो।
- **Concepts:** dict lookup, `*`/default args, list building, loop, `return`
- **Hint:** `bill` = `sum(menu[item] for item in order)`, then add `subtotal * tax / 100`.

---

### Project 26 — Number Guessing Game (refactored)
- **EN:** Refactor the guessing game into functions: `check_guess(guess, secret)` returns `"low"/"high"/"correct"`, and `play(secret, max_attempts)` runs the whole game loop using it, returning `True` if the player won. Print win/lose with attempts used.
- **हिंदी:** guessing game को functions में बाँटो: `check_guess(guess, secret)` जो `"low"/"high"/"correct"` return करे, और `play(secret, max_attempts)` जो पूरा game loop चलाए और जीतने पर `True` return करे। कितने attempts लगे उसके साथ win/lose print करो।
- **Concepts:** helper functions, `while`, counter, `return` a boolean
- **Hint:** Loop `while attempts < max_attempts`; on `"correct"` return `True`; after loop return `False`.

---

### Project 27 — Password Strength Checker
- **EN:** Write `check_strength(password)` that returns `"Weak"`, `"Medium"`, or `"Strong"` based on how many rules it passes: length ≥ 8, has a digit, has an uppercase, has a lowercase, has a special character. Test it on 3 different passwords and print each verdict.
- **हिंदी:** `check_strength(password)` बनाओ जो कितने नियम पास हुए उसके आधार पर `"Weak"`, `"Medium"`, या `"Strong"` return करे: length ≥ 8, एक digit हो, एक uppercase हो, एक lowercase हो, एक special character हो। इसे 3 अलग passwords पर test करके हर verdict print करो।
- **Concepts:** helper functions or `any()`, counting conditions, string checks, `return`
- **Hint:** Count how many of the 5 checks are `True`. 4–5 → Strong, 2–3 → Medium, else Weak.

---

### Project 28 — Temperature Conversion Tool (multi-mode)
- **EN:** Write three functions: `c_to_f(c)`, `f_to_c(f)`, `c_to_k(c)`. Run a `while` menu asking which conversion the user wants, take the value, call the right function, and print the result. Loop until the user chooses Exit.
- **हिंदी:** तीन functions बनाओ: `c_to_f(c)`, `f_to_c(f)`, `c_to_k(c)`। एक `while` menu चलाओ जो पूछे कौन-सा conversion चाहिए, value लो, सही function call करो, और result print करो। Exit चुनने तक loop चलाओ।
- **Concepts:** several functions, menu dispatch, `float(input())`, loop
- **Hint:** `f_to_c` = `(f - 32) * 5 / 9`; `c_to_k` = `c + 273.15`.

---

### Project 29 — Contact Book Manager
- **EN:** Build a contact book (dict of name → phone). Write functions `add_contact`, `search_contact`, `delete_contact`, and `show_all`, each taking and returning/using the contacts dict safely. Run a full `while` menu with options 1–5 (5 = Exit).
- **हिंदी:** एक contact book बनाओ (dict: name → phone)। functions बनाओ `add_contact`, `search_contact`, `delete_contact`, और `show_all`, हर एक contacts dict को safely ले और return/use करे। पूरा `while` menu चलाओ options 1–5 के साथ (5 = Exit)।
- **Concepts:** dict CRUD, multiple functions, `.get()`, `in` check, menu loop
- **Hint:** In `search_contact`, use `contacts.get(name)` and handle `None` (not found).

---

### Project 30 — Shopping Cart & Invoice Generator (capstone)
- **EN:** Build a shopping system. Functions: `add_item(cart, name, price, qty)` (returns updated cart list of dicts), `cart_subtotal(cart)`, `apply_discount(subtotal, percent=0)`, and `print_invoice(cart, discount_percent=0)`. Add at least 3 items, apply a discount, and print a neat itemised invoice with subtotal, discount, and grand total.
- **हिंदी:** एक shopping system बनाओ। Functions: `add_item(cart, name, price, qty)` (dicts की updated cart list return करे), `cart_subtotal(cart)`, `apply_discount(subtotal, percent=0)`, और `print_invoice(cart, discount_percent=0)`। कम से कम 3 items जोड़ो, discount लगाओ, और subtotal, discount, और grand total के साथ साफ़-सुथरा itemised invoice print करो।
- **Concepts:** list of dicts, multiple cooperating functions, defaults, `return`, formatting
- **Hint:** Each cart item is a dict `{"name":..., "price":..., "qty":...}`. Subtotal = `sum(i["price"] * i["qty"] for i in cart)`.

---

## ✅ Self-Check Rubric / खुद जाँचो

- **EN:** After each project ask: (1) Does it run without errors? (2) Does the function `return` (not just `print`)? (3) Can I reuse this function elsewhere? (4) Are my parameter names meaningful?
- **हिंदी:** हर project के बाद पूछो: (1) क्या बिना error चलता है? (2) क्या function `return` करता है (सिर्फ़ `print` नहीं)? (3) क्या मैं इसे कहीं और दोबारा इस्तेमाल कर सकता हूँ? (4) क्या parameter के नाम meaningful हैं?

---
---
---

# 🔒 SOLUTIONS / ANSWER KEY

> ## ⚠️ STOP! / रुको!
> **EN:** Only look here after you've tried a project for at least 15–20 minutes. Many correct solutions exist — yours does not need to match exactly, it just needs to work.
> **हिंदी:** यहाँ सिर्फ़ तब देखो जब आप किसी project पर कम से कम 15–20 मिनट खुद कोशिश कर चुके हो। कई सही हल हो सकते हैं — आपका code बिल्कुल same होना ज़रूरी नहीं, बस सही काम करे।

---

### ✅ Solution 1 — Room Area Calculator
```python
def room_area(length, width):
    return length * width

print(room_area(10, 12))    # 120
print(room_area(8, 8))      # 64
print(room_area(15, 10))    # 150
```

---

### ✅ Solution 2 — Temperature Converter
```python
def celsius_to_f(c):
    return (c * 9 / 5) + 32

print(celsius_to_f(0))      # 32.0
print(celsius_to_f(37))     # 98.6
print(celsius_to_f(100))    # 212.0
```

---

### ✅ Solution 3 — Simple Interest Calculator
```python
def simple_interest(principal, rate, years):
    return (principal * rate * years) / 100

print(simple_interest(10000, 5, 3))    # 1500.0
```

---

### ✅ Solution 4 — Greeting Card Maker
```python
def make_greeting(name, occasion):
    return f"Happy {occasion}, {name}!"

message = make_greeting("Asha", "Diwali")
print(message)              # Happy Diwali, Asha!
```

---

### ✅ Solution 5 — Tip Calculator
```python
def tip_amount(bill, percent):
    return bill * percent / 100

tip = tip_amount(800, 10)
total = 800 + tip
print(f"Tip: {tip}")        # Tip: 80.0
print(f"Total: {total}")    # Total: 880.0
```

---

### ✅ Solution 6 — Even or Odd Checker
```python
def is_even(n):
    return n % 2 == 0

for num in [3, 8, 15, 22, 41]:
    if is_even(num):
        print(f"{num} is even")
```
**Expected output:**
```
8 is even
22 is even
```

---

### ✅ Solution 7 — Discount Price Calculator
```python
def final_price(price, discount_percent):
    return price - (price * discount_percent / 100)

print(final_price(1500, 20))    # 1200.0
```

---

### ✅ Solution 8 — Smart Greeting (default value)
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Asha"))            # Hello, Asha!
print(greet("Rahul", "Namaste"))   # Namaste, Rahul!
```

---

### ✅ Solution 9 — Pizza Order System
```python
def order_pizza(item, qty=1, size="medium"):
    return f"{qty} {size} {item}"

print(order_pizza("pizza"))               # 1 medium pizza
print(order_pizza("pizza", 2))            # 2 medium pizza
print(order_pizza("pizza", size="large")) # 1 large pizza
```

---

### ✅ Solution 10 — Power Function
```python
def power(base, exp=2):
    return base ** exp

print(power(5))         # 25
print(power(2, 3))      # 8
```

---

### ✅ Solution 11 — Shopping Cart Total
```python
def cart_total(*prices):
    return sum(prices)

print(cart_total(100, 250, 90))            # 440
print(cart_total(10, 20, 30, 40, 50, 60))  # 210
```

---

### ✅ Solution 12 — Class Average
```python
def average(*marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

print(average(80, 90, 100))    # 90.0
print(average())               # 0
```

---

### ✅ Solution 13 — User Profile Builder
```python
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Asha", age=17, city="Mumbai")
```
**Expected output:**
```
name: Asha
age: 17
city: Mumbai
```

---

### ✅ Solution 14 — LLM Message Maker
```python
def make_message(text, role="user"):
    return {"role": role, "content": text}

print(make_message("Hello"))
# {'role': 'user', 'content': 'Hello'}
print(make_message("You are helpful", role="system"))
# {'role': 'system', 'content': 'You are helpful'}
```

---

### ✅ Solution 15 — Safe Shopping Cart
```python
def add_item(item, cart=None):
    # cart=[] would be created ONCE and shared across calls (a bug).
    # None + fresh list gives each call its own cart.
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("milk"))     # ['milk']
print(add_item("bread"))    # ['bread']
print(add_item("eggs"))     # ['eggs']
```

---

### ✅ Solution 16 — Chat History Appender
```python
def add_message(text, history=None):
    if history is None:
        history = []
    history.append({"role": "user", "content": text})
    return history

chat1 = add_message("Hi")
chat2 = add_message("Hello")
print(chat1)    # [{'role': 'user', 'content': 'Hi'}]
print(chat2)    # [{'role': 'user', 'content': 'Hello'}]
```

---

### ✅ Solution 17 — Calculator Refactor
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
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Unknown operation"

print(calculate(10, 5, "+"))    # 15
print(calculate(10, 0, "/"))    # Cannot divide by zero
print(calculate(6, 7, "*"))     # 42
```

---

### ✅ Solution 18 — Grade Report
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

students = {"Asha": 92, "Rahul": 70, "Priya": 81}
for name, marks in students.items():
    print(f"{name}: Grade {get_grade(marks)}")
```
**Expected output:**
```
Asha: Grade A
Rahul: Grade C
Priya: Grade B
```

---

### ✅ Solution 19 — Restaurant Bill
```python
def restaurant_bill(*prices, tax=5, tip=0):
    subtotal = sum(prices)
    total = subtotal + (subtotal * tax / 100) + (subtotal * tip / 100)
    return total

print(restaurant_bill(200, 300, 100))          # 630.0  (tax 5%, no tip)
print(restaurant_bill(200, 300, 100, tip=10))  # 690.0  (tax 5% + tip 10%)
```

---

### ✅ Solution 20 — Build Your First Tools Library
```python
# my_tools.py

def celsius_to_f(c):
    return (c * 9 / 5) + 32

def bmi(weight, height):
    return weight / height ** 2

def is_prime(n):
    if n < 2:
        return False
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime

def word_count(text):
    return len(text.split())

print(celsius_to_f(37))               # 98.6
print(round(bmi(60, 1.7), 1))         # 20.8
print(is_prime(7))                    # True
print(is_prime(8))                    # False
print(word_count("I love Python"))    # 3
```

---

### ✅ Solution 21 — ATM Machine Simulator
```python
def check_balance(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
        return balance
    return balance - amount

balance = 1000
while True:
    print("\n1) Balance  2) Deposit  3) Withdraw  4) Exit")
    choice = input("Choice: ")

    if choice == "1":
        print(f"Balance: {check_balance(balance)}")
    elif choice == "2":
        amount = float(input("Deposit amount: "))
        balance = deposit(balance, amount)
        print(f"New balance: {balance}")
    elif choice == "3":
        amount = float(input("Withdraw amount: "))
        balance = withdraw(balance, amount)
        print(f"New balance: {balance}")
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
```

---

### ✅ Solution 22 — Student Report Card System
```python
def total(marks):
    return sum(marks)

def average(marks):
    return total(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

students = [
    {"name": "Asha", "marks": [85, 90, 95]},
    {"name": "Rahul", "marks": [70, 65, 72]},
    {"name": "Priya", "marks": [88, 91, 84]},
]

topper_name = ""
topper_avg = 0

for s in students:
    avg = average(s["marks"])
    print(f"{s['name']:<6} | Total: {total(s['marks'])} | Avg: {avg:.2f} | Grade: {grade(avg)}")
    if avg > topper_avg:
        topper_avg = avg
        topper_name = s["name"]

print(f"\nClass Topper: {topper_name} ({topper_avg:.2f})")
```

---

### ✅ Solution 23 — Quiz Game with Scoring
```python
def ask(question, answer):
    user = input(question + " ")
    if user.strip().lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print(f"Wrong! Answer: {answer}")
        return 0

quiz = [
    {"question": "Capital of India?", "answer": "Delhi"},
    {"question": "2 + 2 * 2 = ?", "answer": "6"},
    {"question": "Python keyword to make a function?", "answer": "def"},
]

score = 0
for q in quiz:
    score = score + ask(q["question"], q["answer"])

print(f"\nYour score: {score}/{len(quiz)}")
if score >= len(quiz) / 2:
    print("You passed!")
else:
    print("Try again!")
```

---

### ✅ Solution 24 — Simple Banking (multiple accounts)
```python
def deposit(accounts, name, amount):
    if name not in accounts:
        print("Account not found")
        return accounts
    accounts[name] = accounts[name] + amount
    return accounts

def withdraw(accounts, name, amount):
    if name not in accounts:
        print("Account not found")
        return accounts
    if amount > accounts[name]:
        print("Insufficient funds")
        return accounts
    accounts[name] = accounts[name] - amount
    return accounts

accounts = {"Asha": 5000, "Rahul": 3000}

while True:
    print("\n1) Deposit  2) Withdraw  3) Show  4) Exit")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Account name: ")
        amount = float(input("Amount: "))
        accounts = deposit(accounts, name, amount)
    elif choice == "2":
        name = input("Account name: ")
        amount = float(input("Amount: "))
        accounts = withdraw(accounts, name, amount)
    elif choice == "3":
        print(accounts)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
```

---

### ✅ Solution 25 — Restaurant Ordering System
```python
def add_to_order(order, item):
    order.append(item)
    return order

def bill(order, menu, tax=5):
    subtotal = sum(menu[item] for item in order)
    return subtotal + (subtotal * tax / 100)

menu = {"pizza": 200, "burger": 120, "coke": 50}
order = []

while True:
    print("\nMenu:", menu)
    choice = input("Add item (or 'done'): ").lower()
    if choice == "done":
        break
    if choice in menu:
        order = add_to_order(order, choice)
        print(f"Added {choice}")
    else:
        print("Item not on menu")

print("\n----- BILL -----")
for item in order:
    print(f"{item:<8} {menu[item]}")
print(f"Total (with tax): {bill(order, menu):.2f}")
```

---

### ✅ Solution 26 — Number Guessing Game (refactored)
```python
def check_guess(guess, secret):
    if guess < secret:
        return "low"
    elif guess > secret:
        return "high"
    else:
        return "correct"

def play(secret, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Guess (1-100): "))
        attempts = attempts + 1
        result = check_guess(guess, secret)
        if result == "correct":
            print(f"Correct in {attempts} attempts!")
            return True
        elif result == "low":
            print("Too low")
        else:
            print("Too high")
    print(f"Out of attempts! The number was {secret}")
    return False

won = play(42, 5)
print("Won!" if won else "Better luck next time!")
```

---

### ✅ Solution 27 — Password Strength Checker
```python
def check_strength(password):
    score = 0
    if len(password) >= 8:
        score = score + 1
    if any(ch.isdigit() for ch in password):
        score = score + 1
    if any(ch.isupper() for ch in password):
        score = score + 1
    if any(ch.islower() for ch in password):
        score = score + 1
    if any(not ch.isalnum() for ch in password):
        score = score + 1

    if score >= 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

for pwd in ["abc", "abcd1234", "Abcd@1234"]:
    print(f"{pwd:<12} -> {check_strength(pwd)}")
```
**Expected output:**
```
abc          -> Weak
abcd1234     -> Medium
Abcd@1234    -> Strong
```

---

### ✅ Solution 28 — Temperature Conversion Tool (multi-mode)
```python
def c_to_f(c):
    return (c * 9 / 5) + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_k(c):
    return c + 273.15

while True:
    print("\n1) C to F  2) F to C  3) C to K  4) Exit")
    choice = input("Choice: ")
    if choice == "1":
        value = float(input("Celsius: "))
        print(f"= {c_to_f(value):.2f} F")
    elif choice == "2":
        value = float(input("Fahrenheit: "))
        print(f"= {f_to_c(value):.2f} C")
    elif choice == "3":
        value = float(input("Celsius: "))
        print(f"= {c_to_k(value):.2f} K")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
```

---

### ✅ Solution 29 — Contact Book Manager
```python
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return contacts

def search_contact(contacts, name):
    phone = contacts.get(name)
    if phone:
        print(f"{name}: {phone}")
    else:
        print("Contact not found")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name}")
    else:
        print("Contact not found")
    return contacts

def show_all(contacts):
    if not contacts:
        print("No contacts yet")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

contacts = {}
while True:
    print("\n1) Add  2) Search  3) Delete  4) Show all  5) Exit")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts = add_contact(contacts, name, phone)
    elif choice == "2":
        search_contact(contacts, input("Name to search: "))
    elif choice == "3":
        contacts = delete_contact(contacts, input("Name to delete: "))
    elif choice == "4":
        show_all(contacts)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
```

---

### ✅ Solution 30 — Shopping Cart & Invoice Generator (capstone)
```python
def add_item(cart, name, price, qty):
    cart.append({"name": name, "price": price, "qty": qty})
    return cart

def cart_subtotal(cart):
    return sum(item["price"] * item["qty"] for item in cart)

def apply_discount(subtotal, percent=0):
    return subtotal - (subtotal * percent / 100)

def print_invoice(cart, discount_percent=0):
    print("\n------- INVOICE -------")
    for item in cart:
        line = item["price"] * item["qty"]
        print(f"{item['name']:<10} {item['qty']} x {item['price']} = {line}")
    subtotal = cart_subtotal(cart)
    grand_total = apply_discount(subtotal, discount_percent)
    print(f"Subtotal      : {subtotal}")
    print(f"Discount      : {discount_percent}%")
    print(f"Grand Total   : {grand_total:.2f}")

cart = []
cart = add_item(cart, "Notebook", 40, 3)
cart = add_item(cart, "Pen", 10, 5)
cart = add_item(cart, "Bag", 500, 1)
print_invoice(cart, discount_percent=10)
```
**Expected output:**
```
------- INVOICE -------
Notebook   3 x 40 = 120
Pen        5 x 10 = 50
Bag        1 x 500 = 500
Subtotal      : 670
Discount      : 10%
Grand Total   : 603.00
```

---

*Solutions complete. / Solutions खत्म. If your answer looks different but gives the right output, it is also correct! / अगर आपका answer अलग दिखता है पर सही output देता है, तो वह भी सही है!* 🎉
