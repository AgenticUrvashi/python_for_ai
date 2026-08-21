# WEEK 9 — Errors & Resilience (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week hum code ko 'bulletproof' banayenge — jo crash hone ke bajaye galtiyon ko sambhal le. Yeh agentic AI ke liye CRITICAL hai, kyunki agents har waqt fail hote hain: API timeout, galat input, internet gaya. Jo engineer failure handle karta hai, wahi succeed karta hai."*

---

## CLASS 51 — Understanding Exceptions

*"Week 0 mein humne errors se DARNA chhoda. Aaj se hum errors ko CONTROL karna seekhenge. Jab code mein kuch galat hota hai, Python ek 'exception' phenkta hai (raise karta hai). Aaj samajhenge yeh exceptions hote kya hain aur common types kaunse hain."*

### 🎯 Today's goal
Exceptions kya hain samajhna aur common types pehchaanna.

### 👨‍🏫 Concept 1 — exception = code ka 'ruk jao' signal

> **📖 Technical definition — Exception:** An exception is an event that occurs during execution and interrupts the normal flow of a program. When an error condition arises, Python raises an exception object of a specific type; if it is not handled, the program stops.

*"Jab Python kisi line par kaam nahi kar paata, woh program ko ROK deta hai aur ek exception 'raise' karta hai. Agar hum use handle na karein, program crash ho jaata hai."*
```python
print("Start")
result = 10 / 0          # yahan exception raise hua
print("End")             # yeh kabhi nahi chala — program crash
```
Output:
```
Start
ZeroDivisionError: division by zero
```
*"Dekho 'End' print nahi hua. Exception ne program ko beech mein hi rok diya. Hamara goal: aise rukne se bachna, gracefully handle karna."*

### 👨‍🏫 Concept 2 — common exception types (jaan-pehchaan banao)
```python
10 / 0                    # ZeroDivisionError — zero se divide
int("abc")                # ValueError — text ko number nahi bana sakte
print(undefined_var)      # NameError — variable exist nahi karta
[1, 2, 3][10]             # IndexError — list mein itna index nahi
{"a": 1}["b"]             # KeyError — dict mein woh key nahi
"5" + 5                   # TypeError — string aur int jod nahi sakte
open("nofile.txt")        # FileNotFoundError — file maujood nahi
```
*"Har error ka NAAM batata hai KYA galat hua. Inhe pehchanna seekho — yeh fixing ka pehla kadam hai. Yeh exact naam aap roz dekhoge."*

### 👨‍🏫 Concept 3 — traceback padhna (Python 3.15 super helpful)

> **📖 Technical definition — Traceback:** A traceback is the report Python prints when an unhandled exception occurs. It lists the chain of function calls that led to the error, ending with the exception type and message on the last line.

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
```
Traceback:
```
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    result = divide(10, 0)
  File "test.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```
*"Traceback ko NEECHE se UPAR padho: aakhri line error ka type+message (`ZeroDivisionError`). Upar wali lines batati hain error kahan se aaya (line 2, function `divide` mein, jo line 4 se bula gaya). Python 3.15 yeh aur saaf dikhaता hai."*

### 👨‍🏫 Concept 4 — exceptions BURI nahi hain
*"Yaad rakho: exceptions Python ka 'kuch galat hai' batane ka tareeka hai. Yeh helpful hain! Bina inke, galat code chupke se galat result deta. Exception kehta hai 'ruk, yahan dhyaan do'. Aaj se hum inhe handle karna seekhenge, darna nahi."*

### 💻 Demo — alag errors trigger karo
```python
tests = ["10/0", "int(abc)", "list[10]"]
print("Let's trigger errors on purpose:")

# 1
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught: {e}")        # Caught: division by zero

# 2
try:
    n = int("hello")
except ValueError as e:
    print(f"Caught: {e}")        # Caught: invalid literal for int() with base 10: 'hello'
```
*"(`try/except` kal detail mein — abhi bas dekho ki hum error ko 'pakad' (catch) sakte hain aur message print kar sakte hain, crash nahi.)"*

### 🔗 Agentic link
*"Ek agent ka har step fail ho sakta hai: LLM API timeout deta hai (TimeoutError), tool galat input se ValueError, JSON parse fail (KeyError). Inn error types ko pehchanna pehla kadam hai unhe handle karne ka. Aaj aapne 'dushman' ko jaan liya — kal use harana seekhenge."*

### ✍️ Homework
1. Jaan-boojh kar 3 alag errors banao (ZeroDivisionError, ValueError, IndexError) aur traceback padho.
2. Har error ke liye ek line likho: "Yeh error kab aata hai?"
3. `int(input(...))` mein letters daalo aur dekho kaunsa error aata hai.

**Answers:**
```python
# 1 (in alag-alag lines run karke errors dekho)
10 / 0                    # ZeroDivisionError — jab denominator 0 ho
int("abc")                # ValueError — jab string ko number nahi bana sakte
[1, 2][5]                 # IndexError — jab list mein utna index nahi

# 3
# int(input("Number: "))   par "hello" daalo → ValueError
```

### 🔗 Agli class
*"Agli class — `try/except/else/finally`: errors ko gracefully PAKADNA aur sambhalna. Yahin se aapka code professional ban-ta hai."*

---

## CLASS 52 — try / except / else / finally

*"Aaj week ka core: `try/except`. Idea simple hai — 'koshish (try) karo yeh code chalane ki; agar error aaye (except), toh crash ke bajaye yeh karo.' Yeh aapke program ko zinda rakhta hai."*

### 🎯 Today's goal
`try/except/else/finally` ka poora block samajhna.

### 👨‍🏫 Concept 1 — basic try/except

> **📖 Technical definition — `try`/`except`/`else`/`finally`:** This construct handles exceptions. Code that might fail goes in `try`; a matching `except` block runs if a specified exception is raised; the optional `else` block runs only when no exception occurred; and the optional `finally` block always runs, typically for cleanup.

```python
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Program continues...")       # yeh ab chalega! crash nahi hua
```
Output:
```
Cannot divide by zero!
Program continues...
```
*"`try` block mein woh code daalo jo fail ho sakta hai. `except` block mein woh code jo error aane par chale. Ab program crash nahi hua — error pakda gaya aur program aage badh gaya. Yeh GAME-CHANGER hai."*

### 👨‍🏫 Concept 2 — error message capture karna (`as e`)
```python
try:
    age = int("not a number")
except ValueError as e:
    print(f"Error occurred: {e}")
    # Error occurred: invalid literal for int() with base 10: 'not a number'
```
*"`as e` se hum asli error message ko ek variable `e` mein pakad lete hain, taaki use log ya print kar sakein. Debugging mein bahut kaam aata hai."*

### 👨‍🏫 Concept 3 — `else` aur `finally`
*"Poora block 4 hisson ka hota hai:"*
```python
try:
    number = int(input("Enter a number: "))      # fail ho sakta hai
except ValueError:
    print("That's not a valid number!")          # error aane par
else:
    print(f"Great! You entered {number}")        # SIRF jab koi error NA aaye
finally:
    print("Thank you for using the program")     # HAMESHA chalta hai
```
- **`try`** — risky code.
- **`except`** — error aaye toh.
- **`else`** — koi error NA aaye toh (success).
- **`finally`** — HAMESHA (error ho ya na ho) — cleanup ke liye.

*"`finally` super useful hai cleanup ke liye — jaise file band karna ya connection close karna — chahe kuch bhi ho jaaye, yeh chalega."*

### 💻 Demo — safe number input
```python
def get_number():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, using 0 instead")
        return 0

n = get_number()        # letters daalo → "Invalid input, using 0", return 0
print(f"You entered: {n}")
```
*"Ab chahe user kuch bhi type kare, program crash nahi hoga — galat input par 0 use kar lega. Yeh real software jaisa robust hai."*

### ❌ Common mistakes
```python
# 1) sab kuch try mein daalna (bahut bada try block)
try:
    a = 5
    b = 10
    c = a + b           # yeh fail nahi hoga, try mein daalne ki zaroorat nahi
    risky = 10 / 0      # sirf yeh risky hai
except:
    ...
# behtar: sirf risky line try mein rakho

# 2) khaali except (sab kuch nigal jaana) — KHATARNAK
try:
    risky()
except:                 # ❌ har error chup-chaap kha jaata hai (bug chhup jaate hain)
    pass
# behtar: specific error pakdo (kal seekhenge)
```

### 🔗 Agentic link
*"Yeh BAHUT important hai: ek agent mein, HAR external call (LLM API, tool, web request) ko `try/except` mein wrap karte hain. Kyun? Taaki ek tool ka fail hona POORE agent ko crash na kar de. Agent error pakad le, soch le 'yeh fail hua, kuch aur try karoon', aur chalta rahe. Yeh resilience agents ko bharosemand banata hai."*

### ✍️ Homework
1. Safe division: do numbers lo, divide karo, ZeroDivisionError handle karo.
2. Safe int conversion: user input ko int banao, ValueError handle karke "Invalid" bolo.
3. Ek try/except/else/finally ka poora example likho jo chaaron blocks dikhaye.

**Answers:**
```python
# 1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # Cannot divide by zero

# 2
text = input("Enter a number: ")
try:
    num = int(text)
    print(f"Doubled: {num * 2}")
except ValueError:
    print("Invalid number")

# 3
try:
    x = int("10")
except ValueError:
    print("error")
else:
    print(f"Success: {x}")       # Success: 10
finally:
    print("Done")                # Done
```

### 🔗 Agli class
*"Agli class — alag-alag errors ko ALAG tareeke se handle karna. Kyunki timeout aur galat-input ko alag treatment chahiye."*

---

## CLASS 53 — Specific Exceptions

*"Pichli class mein humne errors pakde. Par sab errors ek jaise nahi hote — galat input ka jawaab alag, file-not-found ka alag. Aaj seekhenge alag-alag exceptions ko alag-alag handle karna. Yeh precise aur professional hai."*

### 🎯 Today's goal
Multiple `except` blocks, aur sahi exception type pakadna.

### 👨‍🏫 Concept 1 — alag errors, alag handlers

> **📖 Technical definition — Multiple exception handlers:** A `try` block can be followed by several `except` blocks, each targeting a specific exception type. Python runs the first handler whose type matches the raised exception, so more specific exceptions must be listed before more general ones like `Exception`.

```python
try:
    numbers = [1, 2, 3]
    index = int(input("Enter index: "))
    print(numbers[index])
except ValueError:
    print("Please enter a valid number")       # input number nahi tha
except IndexError:
    print("Index out of range (use 0-2)")      # index list mein nahi
```
*"Python pehla MATCHING except dhoondhta hai. Agar input 'abc' tha → ValueError handler. Agar input '10' tha → IndexError handler. Har error ka apna sahi jawaab."*

### 👨‍🏫 Concept 2 — ek handler, kai errors
```python
try:
    risky_operation()
except (ValueError, TypeError) as e:           # dono ek saath
    print(f"Input problem: {e}")
```
*"Agar do errors ko same treatment dena ho, unhe ek tuple mein daal do `(ValueError, TypeError)`. Ek handler, dono cover."*

### 👨‍🏫 Concept 3 — order matter karta hai (specific pehle)
```python
try:
    risky()
except Exception:               # ❌ yeh SAB pakad lega, specific kabhi nahi chalega
    print("Some error")
except ValueError:              # yeh kabhi nahi chalega (upar wala pehle pakad leta hai)
    print("Value error")
```
*"`Exception` saare errors ka 'baap' hai — yeh sab pakad leta hai. Isliye HAMESHA specific exceptions PEHLE rakho, general `Exception` SABSE AAKHIR mein (agar zaroori ho)."*

### 👨‍🏫 Concept 4 — general fallback (samajhdaari se)
```python
try:
    risky()
except ValueError:
    print("Bad value")
except FileNotFoundError:
    print("File missing")
except Exception as e:          # baaki sab ke liye safety net (aakhir mein)
    print(f"Unexpected error: {e}")
```
*"Specific errors pehle, phir ek general `Exception` aakhir mein — taaki koi anjaan error bhi crash na kare. Par khaali `except:` se yeh behtar hai kyunki yahan hum error ko LOG karte hain, chupate nahi."*

### 💻 Demo — file reader with specific handling
```python
def read_file(filename):
    try:
        with open(filename) as f:           # file kholna (Week 10 detail)
            return f.read()
    except FileNotFoundError:
        return f"File '{filename}' not found"
    except PermissionError:
        return f"No permission to read '{filename}'"

print(read_file("nonexistent.txt"))     # File 'nonexistent.txt' not found
```

### ❌ Common mistakes
```python
# general pehle (specific kabhi nahi chalega)
try:
    int("abc")
except Exception:           # ❌ yeh ValueError ko bhi pakad lega
    print("general")
except ValueError:          # kabhi nahi chalega — dead code
    print("value")

# galat exception pakadna
try:
    10 / 0
except ValueError:          # ❌ yeh ZeroDivisionError hai, ValueError nahi
    print("won't catch it")
# program phir bhi crash hoga
```

### 🔗 Agentic link
*"Yeh agents ke liye perfect hai: ek `TimeoutError` ko aap RETRY karoge (shayad network slow tha), par ek `ValueError` (galat input) ko retry karne ka koi fayda nahi — use turant report karo. Alag errors, alag strategy. Aaj aapne precise error handling seekhi jo agents ko smart banati hai."*

### ✍️ Homework
1. Ek program jo list se index access kare, ValueError aur IndexError dono alag handle kare.
2. `int(input)` mein ek try with ValueError aur ek general Exception fallback.
3. Do errors `(ZeroDivisionError, ValueError)` ko ek hi handler se pakdo.

**Answers:**
```python
# 1
nums = [10, 20, 30]
try:
    i = int(input("Index: "))
    print(nums[i])
except ValueError:
    print("Not a number")
except IndexError:
    print("Index out of range")

# 3
try:
    x = int("abc")
    y = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Math/value error: {e}")
```

### 🔗 Agli class
*"Agli class — apne KHUD ke errors banana (`raise`) aur custom exception classes. Taaki aapka code apni galtiyां saaf-saaf bata sake."*

---

## CLASS 54 — raise & Custom Exceptions

*"Ab tak humne Python ke errors PAKDE. Aaj hum apne KHUD ke errors banayenge aur phenkenge (raise). Kyun? Taaki jab aapke code mein kuch galat ho — jaise balance se zyada nikalna — aap ek saaf, specific error de sako, na ki ek confusing crash."*

### 🎯 Today's goal
`raise` se errors phenkna, aur custom exception classes banana.

### 👨‍🏫 Concept 1 — `raise` (khud error phenko)

> **📖 Technical definition — `raise`:** The `raise` statement deliberately triggers an exception. It is used to signal an error condition explicitly (for example, invalid input), stopping normal execution with a clear, specific message instead of allowing incorrect data to propagate.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(set_age(25))      # 25
print(set_age(-5))      # ❌ ValueError: Age cannot be negative
```
*"`raise` se aap jaan-boojh kar ek error phenkte ho jab kuch galat ho. Yeh chupchaap galat value accept karne se behtar hai — aap turant, saaf-saaf bata dete ho 'yeh galat hai'. 'Fail loudly, fail early' — professional rule."*

### 👨‍🏫 Concept 2 — kyun raise karein? (silent bug se bachna)
```python
# bina raise — silent galat result
def withdraw_bad(balance, amount):
    return balance - amount         # negative ho sakta hai, koi warning nahi!

print(withdraw_bad(100, 500))       # -400  😱 (galat, par chup-chaap)

# raise ke saath — turant pakda jaata hai
def withdraw_good(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# withdraw_good(100, 500)    # ❌ ValueError: Insufficient funds (saaf signal)
```

### 👨‍🏫 Concept 3 — custom exception class

> **📖 Technical definition — Custom exception:** A custom exception is a user-defined error type created by subclassing `Exception` (or one of its subclasses). It gives a project its own named, meaningful error types that can be raised and caught specifically.

*"Python ke built-in errors (ValueError, etc.) achhe hain, par apne project ke liye apne SPECIFIC errors banana behtar hai. Bas `Exception` se inherit karo (Week 7 ka inheritance!)."*
```python
class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds the balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ₹{amount}, balance is ₹{balance}")
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    # Transaction failed: Cannot withdraw ₹500, balance is ₹100
```
*"`class InsufficientFundsError(Exception)` ek naya, specific error type banata hai. Ab koi bhi `except InsufficientFundsError` se SIRF yeh wala error pakad sakta hai. Yeh aapke code ko bahut readable aur professional banata hai."*

### 👨‍🏫 Concept 4 — exception hierarchy (apne errors ka family)
```python
class ToolError(Exception):
    """Base error for all tool problems."""
    pass

class ToolNotFoundError(ToolError):
    """Specific: tool ka naam nahi mila."""
    pass

class ToolTimeoutError(ToolError):
    """Specific: tool ne time-out kar diya."""
    pass

# faayda: aap base se sab pakad sakte ho, ya specific se ek
try:
    raise ToolTimeoutError("Tool took too long")
except ToolError as e:          # base pakadta hai dono children ko
    print(f"A tool failed: {e}")
```
*"Ek base `ToolError` banao, phir specific errors usse inherit karein. Ab `except ToolError` saare tool errors pakad leta hai, ya `except ToolTimeoutError` sirf ek. Yeh agents mein bahut clean error-handling deta hai."*

### ❌ Common mistakes
```python
def f(x):
    if x < 0:
        raise "Error!"          # ❌ string raise nahi kar sakte — exception object chahiye
        # sahi: raise ValueError("Error!")

class MyError:                  # ❌ Exception se inherit nahi kiya — yeh error nahi banega
    pass
# sahi: class MyError(Exception): pass
```

### 🔗 Agentic link
*"Real agents apne custom errors banate hain: `ToolError`, `RateLimitError`, `InvalidToolInputError`. Isse agent ka loop precisely react kar sakta hai: 'RateLimitError aaya? thodi der ruk ke retry karo. InvalidToolInputError? user se dobara poocho.' Saaf, named errors = smart agent behaviour. Aaj aapne professional error-design seekha."*

### ✍️ Homework
1. Ek function `set_marks(m)` jo 0-100 ke bahar value par ValueError raise kare.
2. Ek custom exception `NegativeNumberError` banao aur ek function jo negative par use raise kare.
3. Ek `BankAccount` class (Week 7) mein `withdraw` ko custom `InsufficientFundsError` raise karwao.

**Answers:**
```python
# 1
def set_marks(m):
    if m < 0 or m > 100:
        raise ValueError("Marks must be between 0 and 100")
    return m
# set_marks(150)   # ValueError

# 2
class NegativeNumberError(Exception):
    pass
def sqrt_check(n):
    if n < 0:
        raise NegativeNumberError("Cannot square-root a negative number")
    return n ** 0.5
try:
    sqrt_check(-4)
except NegativeNumberError as e:
    print(e)        # Cannot square-root a negative number

# 3
class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError("Not enough balance")
        self._balance -= amount
        return self._balance
acc = BankAccount(100)
try:
    acc.withdraw(500)
except InsufficientFundsError as e:
    print(e)        # Not enough balance
```

### 🔗 Agli class
*"Agli class — week ka finale: RETRY pattern. Ek fail hone wale kaam ko dobara try karna — bilkul jaisा agents API failures par karte hain. Phir hum apne tools module ko resilient banayenge."*

---

## CLASS 55 — Retry Pattern (Project Class)

*"Aaj ek SUPER practical skill: RETRY. Maan lo internet ek second ke liye gaya aur API call fail ho gayi. Crash karna bewakoofi hai — dobara try karo! Yeh exactly woh hai jo har production agent karta hai. Aaj hum ek retry wrapper banayenge."*

### 🎯 Today's goal
Loop ke andar try/except se retry pattern, aur attempts + backoff idea.

### 👨‍🏫 Concept 1 — retry ka basic idea

> **📖 Technical definition — Retry pattern:** The retry pattern re-attempts an operation that failed with a transient error, up to a maximum number of attempts. Exponential backoff increases the wait time between attempts (for example 1s, 2s, 4s) to avoid overwhelming a struggling service.

*"Retry = 'fail hua? thodi der ruk, dobara try kar. N baar tak.' Iske 3 hisse: (1) ek loop attempts ke liye, (2) try/except andar, (3) success par break, ya max attempts par haar maano."*
```python
import time

def flaky_task(attempt):
    """Pehle 2 attempts fail, teesre par success (demo ke liye)."""
    if attempt < 3:
        raise ConnectionError("Network error")
    return "Success!"

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    try:
        result = flaky_task(attempt)
        print(f"Attempt {attempt}: {result}")
        break                                   # success — loop chhodo
    except ConnectionError as e:
        print(f"Attempt {attempt} failed: {e}")
        if attempt < max_attempts:
            time.sleep(1)                       # thodi der ruko, phir retry
        else:
            print("All attempts failed. Giving up.")
```
Output:
```
Attempt 1 failed: Network error
Attempt 2 failed: Network error
Attempt 3: Success!
```
*"Dekho: pehle 2 fail hue, par hum ruke nahi — retry kiya, aur 3rd par success. `time.sleep(1)` har retry ke beech 1 second rukta hai (server ko saans dene). Yeh real resilience hai."*

### 👨‍🏫 Concept 2 — backoff (har baar zyada ruko)
*"Smart retry: har fail ke baad ZYADA der ruko (1s, 2s, 4s...). Ise 'exponential backoff' bolte hain. Yeh server par overload nahi daalta jab woh already struggle kar raha ho."*
```python
import time

for attempt in range(1, 4):
    wait = 2 ** (attempt - 1)       # 1, 2, 4 seconds
    print(f"Attempt {attempt}, would wait {wait}s on failure")
```
*"`2 ** (attempt-1)` deta hai 1, 2, 4, 8... Har retry pehle se double wait. Yeh industry-standard pattern hai API calls ke liye."*

### 🛠️ Mini Project — retry wrapper for tools
*"Ab hum ek reusable retry FUNCTION banayenge jo kisi bhi function ko retry kar sake. Yeh decorator nahi (woh Week 11), par usi soch ka simple version. Yeh aapke tools module ka resilience layer hai."*
```python
import time


def retry(func, max_attempts: int = 3, delay: float = 1.0):
    """Run func, retrying on failure with a wait between attempts.

    Args:
        func: A no-argument function to call.
        max_attempts: How many times to try before giving up.
        delay: Base seconds to wait between attempts.

    Returns:
        Whatever func returns on success.

    Raises:
        The last exception if all attempts fail.
    """
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            return func()                       # koshish
        except Exception as e:                  # koi bhi failure
            last_error = e
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                wait = delay * (2 ** (attempt - 1))    # backoff
                print(f"Retrying in {wait}s...")
                time.sleep(wait)
    # saare attempts fail — aakhri error wapas phenko
    raise last_error


# --- test ---
counter = {"calls": 0}

def unreliable():
    counter["calls"] += 1
    if counter["calls"] < 3:
        raise ConnectionError("Temporary failure")
    return "Data fetched!"

result = retry(unreliable, max_attempts=5, delay=0.5)
print(result)       # Data fetched!  (3rd attempt par)
```
*"Yeh `retry` function kisi bhi failing kaam ko sambhal sakta hai: 5 baar try karo, har baar zyada ruko, success par result do, ya saare fail hone par aakhri error phenko. Yeh EXACTLY woh hai jo agents API calls ke liye use karte hain. Aapka tools module ab resilient hai!"*

### ❌ Common mistakes
```python
# success par break bhool jaana → success ke baad bhi loop chalta rahega
for attempt in range(3):
    try:
        result = task()
        # break bhool gaye → galat
    except Exception:
        ...

# infinite retry (max limit nahi) — agar permanently fail ho toh hamesha chalega
while True:
    try:
        task()
        break
    except Exception:
        continue        # ❌ koi max-attempt limit nahi — khatarnak
```

### 🔗 Agentic link
*"Yeh week ka taj hai: ASLI agents har LLM/tool call ke around retry+backoff lagate hain, kyunki APIs temporarily fail hoti rehti hain (rate limits, timeouts, network blips). Bina retry ke, ek chhota network blip poora agent task fail kar deta. Aapne abhi production-grade resilience banaya — yeh sach mein industry skill hai."*

### ✍️ Homework
1. `retry` function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.
2. Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).
3. `retry` mein ek case add karo jahan saare attempts fail hon — aakhri error dekho.

**Answers:**
```python
# 2
delay = 1
for attempt in range(1, 5):
    print(f"Attempt {attempt}: wait {delay * (2 ** (attempt - 1))}s")
# Attempt 1: wait 1s
# Attempt 2: wait 2s
# Attempt 3: wait 4s
# Attempt 4: wait 8s

# 3
def always_fails():
    raise ValueError("nope")
try:
    retry(always_fails, max_attempts=2, delay=0.1)
except ValueError as e:
    print(f"Gave up: {e}")      # Gave up: nope
```

### 🏁 Week 9 wrap-up*"Yeh week aapne code ko BULLETPROOF banaya:*
- *Exceptions samajhna — error types (Class 51)*
- *try/except/else/finally — gracefully pakadna (Class 52)*
- *Specific exceptions — alag errors, alag handling (Class 53)*
- *raise & custom exceptions — apne saaf errors (Class 54)*
- *Retry pattern + backoff — production resilience (Class 55)*

*Ab aapka code crash nahi karta — woh sambhalta hai aur recover karta hai. Yeh agents ke liye non-negotiable hai. Next week — files aur JSON, jo agent ko 'yaad' (persistence) dega aur LLM APIs ki language (JSON) sikhayega. Shabaash!"*

### 📝 Weekend revision task
Apne `tools.py` module mein har function ke around `retry` use karne ki practice karo. Ek function jaan-boojh kar kabhi-kabhi fail karne wala banao (`random` se) aur retry se use stable karo.

---

## 🎤 Industry Interview Questions — Week 9

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. Explain the roles of `try`, `except`, `else`, and `finally`.**

`try` wraps code that might raise. `except` catches and handles a specific error type. `else` runs only if the `try` block succeeded with no exception (a good place for code that should run on success but shouldn't be "protected" by the try). `finally` always runs — exception or not — and is used for cleanup like closing files or releasing resources. Keeping the "risky" and "on success" code separated with `else` makes intent clearer.

**Q2. Why is catching a bare `except:` (or `except Exception`) considered bad practice?**

A blanket catch swallows *every* error, including ones you didn't anticipate (typos, `KeyboardInterrupt`, programming bugs), which hides real problems and makes debugging painful. You should catch the *specific* exceptions you know how to handle (`ValueError`, `TimeoutError`, etc.) and let unexpected ones propagate. Catching broadly is only acceptable at a top-level boundary where you log and convert to a generic, safe user-facing message.

**Q3. When should you create a custom exception class?**

When your code has a domain-specific failure that callers should be able to catch and handle distinctly — e.g. `RateLimitError` or `InvalidToolArgsError`. A custom exception (subclassing `Exception`) makes error handling precise and self-documenting, lets callers `except YourError` without accidentally catching unrelated errors, and lets you attach extra context. Reuse built-ins when they fit; create custom ones when they add meaning.

**Q4. What is retry with exponential backoff, and why add jitter?**

Retrying means re-attempting a transient failure (network blip, rate limit, timeout). Exponential backoff increases the wait between attempts — 1s, 2s, 4s, 8s — so you don't hammer a struggling service. Jitter (a small random offset added to each delay) prevents the "thundering herd" problem where many clients that failed at the same time all retry in sync and overload the service again. This pattern is essential around LLM and API calls in production agents.

**Q5. What is the difference between the EAFP and LBYL styles in Python?**

**LBYL** ("Look Before You Leap") checks preconditions first: `if key in d: use d[key]`. **EAFP** ("Easier to Ask Forgiveness than Permission") just tries and catches the failure: `try: use d[key] except KeyError: ...`. Python idiomatically favors EAFP because it avoids race conditions (the state could change between the check and the use) and is often cleaner when the "happy path" is the common case.
