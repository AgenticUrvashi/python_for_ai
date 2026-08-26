# WEEK 10 — Files, JSON & Text (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap apni screen par khud type karoge.
>
> **Week promise:** *"Is week hum data ko SAVE karna seekhenge (taaki program band hone par bhi yaad rahe) aur JSON sikhenge — woh language jisme HAR LLM API baat karti hai. Yeh agent ko 'memory' deta hai aur APIs se judne ke liye taiyar karta hai."*

---

## CLASS 56 — Reading & Writing Files

*"Ab tak hamare programs band karte hi sab bhool jaate the. Variables RAM mein the — bijli gayi, sab gaya. Aaj hum data ko FILE mein save karenge — hard disk par, permanently. Ab program 'yaad' rakh sakta hai."*

### 🎯 Today's goal
`with open()` se files likhna aur padhna, aur modes `r/w/a`.

### 👨‍🏫 Concept 1 — file mein likhna (`with open`)

> **📖 Technical definition — File handling with `open()`:** `open()` returns a file object connected to a file on disk, opened in a given mode. Using it with a `with` statement (a context manager) guarantees the file is automatically closed when the block ends, flushing any written data safely.

```python
with open("notes.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("Python is fun.\n")

print("File saved!")
```
*"`open("notes.txt", "w")` ek file kholta hai 'write' mode mein. `with` ka matlab: kaam khatam hote hi file APNE AAP band ho jaayegi (bahut important — warna data save nahi hota). `f.write()` text likhta hai. `\n` ek nayi line ka matlab hai."*

### 👨‍🏫 ⚠️ Concept 2 — modes (`w` vs `a` vs `r`)

> **📖 Technical definition — File mode:** A file mode is the string passed to `open()` that sets how the file is used: `"r"` reads an existing file, `"w"` writes and overwrites all existing content, and `"a"` appends new content to the end while keeping the old content.

| Mode | Matlab | Dhyaan |
|---|---|---|
| `"r"` | Read (padho) | Default. File na ho toh error. |
| `"w"` | Write (likho) | **Purana sab MITA deta hai!** |
| `"a"` | Append (jodo) | End mein add karta hai, purana safe |
*"⚠️ SABSE BADA trap: `"w"` mode file ka SAARA purana content MITA deta hai aur naya likhta hai. Agar purana data bachana hai aur naya jodna hai, `"a"` (append) use karo. Yeh galti sabko ek baar lagti hai."*

### 👨‍🏫 Concept 3 — file padhna
```python
# poori file ek string mein
with open("notes.txt", "r") as f:
    content = f.read()
print(content)

# line-by-line (badi files ke liye behtar)
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())        # strip() extra newline hataata hai
```
*"`f.read()` poori file ek baar mein deta hai. Loop `for line in f` ek-ek line deta hai — badi files ke liye memory-friendly. `.strip()` se line ke end ka `\n` saaf karte hain."*

### 👨‍🏫 Concept 4 — append mode (data jodo)
```python
with open("log.txt", "a") as f:
    f.write("New entry\n")          # purane ke END mein jodta hai
```
*"Har baar program chale, append mode purana mita-ye bina naya add karta hai. Logs aur diaries ke liye perfect."*

### 👨‍🏫 Concept 5 — UTF-8 (Python 3.15)
```python
with open("hindi.txt", "w", encoding="utf-8") as f:
    f.write("नमस्ते 🙏 Hello World")
```
*"Python 3.15 mein UTF-8 by default hai, toh Hindi aur emojis smoothly save hote hain. Phir bhi, files ke saath `encoding="utf-8"` explicitly likhna ek achhi, safe habit hai — har machine par same behaviour."*

### 💻 Demo — simple diary
```python
def add_entry(text):
    with open("diary.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_diary():
    with open("diary.txt", "r", encoding="utf-8") as f:
        return f.read()

add_entry("Today I learned file handling")
add_entry("It was easy!")
print(read_diary())
```

### ❌ Common mistakes
```python
# 'w' se galti se data udaana
with open("important.txt", "w") as f:    # ❌ purana sab gaya!
    f.write("new")                        # append chahiye tha toh "a"

# with ke bina (file band karna bhool jaana)
f = open("a.txt", "w")
f.write("hi")
# f.close() bhool gaye → data shayad save na ho. 'with' use karo hamesha.
```

### 🔗 Agentic link
*"Agents files ka bahut use karte hain: prompt templates ko file se LOAD karna, conversation logs ko SAVE karna, results ko file mein likhna. `with open()` aap har agent project mein dekhoge. Append mode logs ke liye, read mode config ke liye."*

### ✍️ Homework
1. Ek file `mygoals.txt` mein 3 goals likho (write mode).
2. Use padho aur print karo.
3. Append mode se ek 4th goal add karo, phir dobara poori file padho.

**Answers:**
```python
# 1
with open("mygoals.txt", "w", encoding="utf-8") as f:
    f.write("Learn Python\n")
    f.write("Build an AI agent\n")
    f.write("Get a job\n")

# 2
with open("mygoals.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 3
with open("mygoals.txt", "a", encoding="utf-8") as f:
    f.write("Stay consistent\n")
with open("mygoals.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### 🔗 Agli class
*"Agli class — `pathlib` se file paths ko sahi aur SAFE tareeke se handle karna. Security ke liye bhi important."*

---

## CLASS 57 — pathlib & Safe Paths

*"File paths ('C:/Users/...' ya '/home/...') har OS mein alag hote hain. Aur agar aap user se path lo, toh ek khatra hai — woh aapke system ki private files tak pahunch sakta hai. Aaj `pathlib` se paths ko saaf aur SAFE handle karna seekhenge."*

### 🎯 Today's goal
`pathlib.Path` use karna, aur paths ko ek allowed folder ke andar rakhna (security).

### 👨‍🏫 Concept 1 — `pathlib.Path` (modern path handling)

> **📖 Technical definition — `pathlib.Path`:** `pathlib.Path` is an object-oriented representation of a filesystem path. It joins paths with the `/` operator in an OS-independent way and provides methods to inspect, read, write, and resolve files and directories.

```python
from pathlib import Path

p = Path("data") / "notes.txt"      # OS-safe joining (/ operator!)
print(p)                            # data\notes.txt (Windows) ya data/notes.txt (Mac)

print(p.name)        # notes.txt    — file ka naam
print(p.suffix)      # .txt         — extension
print(p.parent)      # data         — folder
print(p.exists())    # True/False   — file maujood hai?
```
*"`Path("data") / "notes.txt"` — yeh `/` operator paths ko OS-safe jodta hai (Windows backslash, Mac slash — Python khud sambhaal leta hai). Manually string jodne se behtar."*

### 👨‍🏫 Concept 2 — files/folders banana aur padhna
```python
from pathlib import Path

folder = Path("myfolder")
folder.mkdir(exist_ok=True)         # folder banao (already ho toh error nahi)

file = folder / "hello.txt"
file.write_text("Hello!", encoding="utf-8")     # ek line mein likho
print(file.read_text(encoding="utf-8"))         # ek line mein padho — Hello!
```
*"`pathlib` shortcuts deta hai: `write_text` aur `read_text` — chhoti files ke liye `with open` se bhi simple. `mkdir(exist_ok=True)` folder banata hai bina error ke agar pehle se ho."*

### 👨‍🏫 Concept 3 — folder ki files list karo
```python
from pathlib import Path

folder = Path(".")                  # "." = current folder
for txt_file in folder.glob("*.txt"):       # saari .txt files
    print(txt_file.name)
```
*"`.glob("*.txt")` ek folder ki saari `.txt` files deta hai. `*` ka matlab 'kuch bhi'. Yeh ek folder ke documents process karne ke liye perfect hai."*

### 👨‍🏫 ⚠️ Concept 4 — SECURITY: path traversal se bachna

> **📖 Technical definition — Path traversal:** Path traversal is a security vulnerability where untrusted input containing sequences like `../` is used to escape an intended directory and access files elsewhere on the system. It is prevented by resolving the final absolute path and confirming it stays inside an allowed base folder.

*"Yeh BAHUT important hai. Agar aap user se filename lo aur seedhe use karo, woh `../../secret.txt` jaisा daal kar aapke system ki private files chura sakta hai. Ise 'path traversal attack' bolte hain. Hamesha check karo ki final path aapke ALLOWED folder ke ANDAR hi rahe."*
```python
from pathlib import Path

def safe_read(user_filename: str) -> str:
    """Read a file ONLY if it stays inside the 'uploads' folder.

    SECURITY (path traversal prevention): user input ko seedhe path mein
    use karna khatarnak hai — woh '../' se bahar nikal sakta hai. Isliye
    hum resolve karke check karte hain ki final path allowed folder ke andar hai.
    """
    base = Path("uploads").resolve()            # allowed folder (absolute)
    target = (base / user_filename).resolve()   # final path (absolute)

    # check: target base ke ANDAR hai?
    if not target.is_relative_to(base):
        raise ValueError("Access denied: path outside allowed folder")

    return target.read_text(encoding="utf-8")

# safe_read("notes.txt")        # ✅ allowed
# safe_read("../../secret.txt") # ❌ ValueError: Access denied
```
*"`.resolve()` poora absolute path banata hai (saare `../` solve karke). Phir `is_relative_to(base)` check karta hai ki woh hamare allowed folder ke andar hai ya nahi. Bahar jaane ki koshish? → reject. Yeh ek ZAROORI security check hai jab user filenames de."*

> **Teacher accuracy/security note:** Yeh rule yaad rakho — **kabhi bhi user input ko bina validate kiye file path mein use mat karo.** Hamesha allowed base folder ke andar resolve karke confirm karo. Yeh OWASP ka classic 'path traversal' attack rokta hai.

### ❌ Common mistakes
```python
# user input seedhe path mein — KHATARNAK
filename = input("File: ")
open(filename)               # ❌ user '../../etc/passwd' daal sakta hai

# string concatenation se path (OS-unsafe)
path = "data" + "/" + "file.txt"     # ❌ Path("data") / "file.txt" use karo
```

### 🔗 Agentic link
*"Agents ke paas aksar 'file tools' hote hain (file padho/likho). Yeh tools KHATARNAK ho sakte hain agar LLM ya user koi galat path de. Isliye har file-tool mein yeh safe-path check ZAROORI hai — taaki agent galti se ya hamle mein system files na chhede. Security agentic AI ka ek bada hissa hai."*

### ✍️ Homework
1. `pathlib` se ek folder banao aur usme ek file likho (`write_text`).
2. Current folder ki saari `.txt` files list karo (`glob`).
3. `safe_read` jaisा function banao jo ek allowed folder ke bahar ke path ko reject kare.

**Answers:**
```python
# 1
from pathlib import Path
folder = Path("test_folder")
folder.mkdir(exist_ok=True)
(folder / "data.txt").write_text("hello", encoding="utf-8")

# 2
for f in Path(".").glob("*.txt"):
    print(f.name)

# 3
def is_safe(base_name, user_name):
    base = Path(base_name).resolve()
    target = (base / user_name).resolve()
    return target.is_relative_to(base)
print(is_safe("uploads", "ok.txt"))         # True
print(is_safe("uploads", "../secret.txt"))  # False
```

### 🔗 Agli class
*"Agli class — JSON: woh data format jisme HAR LLM API baat karti hai. Yeh week ka, balki poore course ka, sabse zaroori data-format hai."*

---

## CLASS 58 — JSON

*"Aaj ka topic agentic AI ke liye SABSE zaroori hai: JSON. Yeh ek text format hai data ko store/bhejne ke liye. Aur dhyaan se suno — HAR LLM API, HAR tool call, HAR web API JSON mein baat karti hai. Yeh AI ki 'common language' hai."*

### 🎯 Today's goal
Python aur JSON ke beech convert karna: `json.dump/load/dumps/loads`.

### 👨‍🏫 Concept 1 — JSON dikhta kaise hai?

> **📖 Technical definition — JSON:** JSON (JavaScript Object Notation) is a lightweight, text-based data format for storing and exchanging structured data as key–value objects and arrays. It is language-independent and is the standard format used by web and LLM APIs.

*"JSON Python dictionary se BAHUT milta-julta dikhta hai (yeh achhi khabar hai!). Yeh keys aur values rakhta hai:"*
```json
{
  "name": "Asha",
  "age": 17,
  "subjects": ["Math", "Science"],
  "is_student": true
}
```
*"Dekho — yeh almost ek Python dict hai! Chhote farak: JSON mein `true`/`false`/`null` (Python: `True`/`False`/`None`), aur keys hamesha double-quotes mein. Python inhe automatically convert kar deta hai."*

### 👨‍🏫 Concept 2 — Python → JSON string (`dumps`)

> **📖 Technical definition — Serialization / deserialization:** Serialization converts an in-memory Python object into a JSON text form (`json.dumps` to a string, `json.dump` to a file). Deserialization is the reverse, parsing JSON text back into Python objects (`json.loads` from a string, `json.load` from a file).

```python
import json

data = {"name": "Asha", "age": 17, "passed": True}

json_string = json.dumps(data)
print(json_string)          # {"name": "Asha", "age": 17, "passed": true}
print(type(json_string))    # <class 'str'>   — ab yeh ek string hai

# sundar (readable) banao
pretty = json.dumps(data, indent=2)
print(pretty)
```
*"`json.dumps()` (dump-string) ek Python dict ko JSON STRING banata hai. `indent=2` se woh sundar, padhne layak ban jaata hai. Note: Python ka `True` JSON ka `true` ban gaya — automatic."*

### 👨‍🏫 Concept 3 — JSON string → Python (`loads`)
```python
import json

json_string = '{"name": "Rahul", "age": 18, "passed": true}'

data = json.loads(json_string)
print(data)             # {'name': 'Rahul', 'age': 18, 'passed': True}
print(data["name"])     # Rahul    — ab yeh normal dict hai!
print(type(data))       # <class 'dict'>
```
*"`json.loads()` (load-string) ek JSON string ko wapas Python dict banata hai. Yaad rakhne ka tareeka: `dumps`/`loads` ke 's' = STRING. Yeh do ulte kaam hain."*

### 👨‍🏫 Concept 4 — file ke saath JSON (`dump`/`load`)
```python
import json

data = {"name": "Asha", "scores": [85, 90, 78]}

# JSON file mein save (dump — bina 's')
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# JSON file se load
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["scores"])     # [85, 90, 78]
```
*"`dump`/`load` (bina 's') seedhe FILE ke saath kaam karte hain. `dumps`/`loads` (with 's') STRINGS ke saath. Yeh farak yaad rakho — yeh confuse karta hai."*

| Function | Kaam |
|---|---|
| `json.dumps(data)` | dict → JSON **string** |
| `json.loads(text)` | JSON string → dict |
| `json.dump(data, file)` | dict → JSON **file** |
| `json.load(file)` | JSON file → dict |

### 💻 Demo — save aur reload chat history
```python
import json

# yeh LLM messages ki shakal hai (Week 4 yaad hai?)
history = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi! How can I help?"},
]

# save
with open("chat.json", "w", encoding="utf-8") as f:
    json.dump(history, f, indent=2)

# reload (jaise program dobara chala)
with open("chat.json", "r", encoding="utf-8") as f:
    restored = json.load(f)

print(restored[0]["content"])       # Hello
print(f"Restored {len(restored)} messages")     # Restored 2 messages
```
*"Dekho — humne ek poori chat history save ki aur wapas load ki! Yeh literally agent ki memory persist karna hai."*

### ❌ Common mistakes
```python
import json
# dumps vs dump confuse karna
json.dump(data)          # ❌ dump ko file chahiye: json.dump(data, f)
json.dumps(data, f)      # ❌ dumps ko file nahi chahiye: json.dumps(data)

# invalid JSON load karna
json.loads("{'name': 'Asha'}")   # ❌ JSON ko DOUBLE quotes chahiye, single nahi
```

### 🔗 Agentic link
*"Yeh poore course ki sabse important class ho sakti hai. **Har LLM API JSON leti aur deti hai.** Aap messages ko JSON mein bhejte ho, model JSON mein reply deta hai, tools JSON mein call hote hain. Agent ki memory JSON file mein save hoti hai. JSON master karna = AI APIs ke saath fluently baat karna. Ise pakka karo!"*

### ✍️ Homework
1. Ek dict banao aur use `json.dumps(indent=2)` se sundar print karo.
2. Ek JSON string `'{"city": "Mumbai", "pin": 400001}'` ko dict mein load karke `city` print karo.
3. Apni Week 4 ki contact book (list of dicts) ko JSON file mein save aur reload karo.

**Answers:**
```python
import json
# 1
data = {"name": "Priya", "hobbies": ["reading", "coding"]}
print(json.dumps(data, indent=2))

# 2
s = '{"city": "Mumbai", "pin": 400001}'
d = json.loads(s)
print(d["city"])        # Mumbai

# 3
contacts = [{"name": "Asha", "phone": "98765"}, {"name": "Rahul", "phone": "91234"}]
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, indent=2)
with open("contacts.json", "r", encoding="utf-8") as f:
    print(json.load(f))
```

### 🔗 Agli class
*"Agli class — CSV (spreadsheet data) aur REGEX (text mein patterns dhoondhna). Regex se hum messy LLM output se cheezein nikaalenge."*

---

## CLASS 59 — CSV & Regex

*"Aaj do tools: CSV (Excel-jaisा table data padhna/likhna) aur REGEX (text mein patterns dhoondhne ka super-power — emails, numbers, code blocks nikaalna). Dono real data ke saath roz kaam aate hain."*

### 🎯 Today's goal
`csv` module se table data, aur `re` module se patterns (`search/findall/sub`).

### 👨‍🏫 Concept 1 — CSV (comma-separated values)

> **📖 Technical definition — CSV:** CSV (Comma-Separated Values) is a plain-text tabular format where each line is a row and columns are separated by commas. Python's `csv` module reads and writes it, with `DictReader` mapping each row to a dictionary keyed by the header.

*"CSV ek simple table format hai — har line ek row, columns comma se alag. Excel files aksar CSV mein export hoti hain."*
```python
import csv

# CSV likhna
rows = [
    ["Name", "Marks"],          # header
    ["Asha", 85],
    ["Rahul", 90],
]
with open("marks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# CSV padhna
with open("marks.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)              # ['Name', 'Marks'], ['Asha', '85'], ...
```
*"`csv.writer` rows likhta hai, `csv.reader` rows padhta hai. Dhyaan: padhne par sab STRINGS hote hain ('85', 85 nahi) — zaroorat ho toh `int()` karo. `newline=""` Windows par extra blank lines rokta hai."*

### 👨‍🏫 Concept 2 — CSV as dictionaries (zyada readable)
```python
import csv

with open("marks.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)       # har row ek dict (header keys)
    for row in reader:
        print(row["Name"], row["Marks"])     # Asha 85 ...
```
*"`DictReader` har row ko ek dict banata hai header ko keys use karke. `row["Name"]` se column access — index gin-ne se behtar."*

### 👨‍🏫 Concept 3 — Regex (patterns dhoondhna)

> **📖 Technical definition — Regular expression (regex):** A regular expression is a compact pattern language for matching, searching, and replacing text. Python's `re` module uses these patterns via functions such as `search` (first match), `findall` (all matches), and `sub` (replace matches).

*"Regex ('regular expressions') text mein patterns dhoondhne ki ek mini-language hai. Pehli baar ajeeb dikhta hai, par bahut powerful. Hum `re` module use karte hain."*
```python
import re

text = "Contact: asha@gmail.com or call 9876543210"

# saare numbers dhoondho
numbers = re.findall(r"\d+", text)
print(numbers)          # ['9876543210']

# email dhoondho
email = re.search(r"\w+@\w+\.\w+", text)
print(email.group())    # asha@gmail.com
```
*"`\d` = ek digit, `\d+` = ek ya zyada digits. `\w` = ek letter/digit. `re.findall` saare matches deta hai (list), `re.search` pehla match deta hai. `r"..."` ek 'raw string' hai — regex ke liye zaroori (backslashes safe rehte hain)."*

### 👨‍🏫 Concept 4 — common regex patterns
```python
import re

text = "I have 3 cats and 12 dogs. #pets #animals"

print(re.findall(r"\d+", text))       # ['3', '12']        — numbers
print(re.findall(r"#\w+", text))      # ['#pets', '#animals'] — hashtags
print(re.sub(r"\d+", "N", text))      # I have N cats and N dogs...  — replace
```
| Pattern | Meaning / Matlab | Example / Match |
|---|---|---|
| **Character Classes** | | |
| `\d` | Single digit (0-9) | `"5"` in `"Room 5"` |
| `\D` | Non-digit character | `"R"`, `"o"`, `" "` |
| `\w` | Word character (letter, digit, `_`) | `"user_1"` |
| `\W` | Non-word character (symbol, space) | `"@"`, `"#"`, `"!"`, `" "` |
| `\s` | Whitespace (space, tab, newline) | `" "`, `"\t"`, `"\n"` |
| `\S` | Non-whitespace character | Any non-space character |
| `.` | Any single character (except `\n`) | `"a"`, `"9"`, `"%"` |
| `[abc]` | Any character in set (`a`, `b`, or `c`) | `"a"` in `"apple"` |
| `[^abc]` | Any character NOT in set | `"p"`, `"l"`, `"e"` in `"apple"` |
| `[a-z]` / `[A-Z]` | Lowercase / Uppercase range | `"a"`-`"z"` or `"A"`-`"Z"` |
| **Quantifiers & Anchors** | | |
| `+` | 1 or more times (greedy) | `\d+` -> `"123"` |
| `*` | 0 or more times | `\d*` -> `""` or `"123"` |
| `?` | 0 or 1 time (optional) | `colou?r` -> `"color"`, `"colour"` |
| `{n}` | Exactly `n` times | `\d{4}` -> `"2026"` |
| `{n,m}` | Between `n` and `m` times | `\d{2,4}` -> `"23"`, `"2026"` |
| `^` | Start of string / line | `^Hello` -> `"Hello world"` |
| `$` | End of string / line | `end$` -> `"the end"` |
| `\b` | Word boundary | `\bcat\b` -> matches `"cat"`, not `"cater"` |
| **Groups & Operators** | | |
| `(...)` | Capturing group | `(\d{3})-(\d{4})` |
| `(?:...)` | Non-capturing group | `(?:https\|http)` |
| `a\|b` | Either `a` or `b` (OR logic) | `"cat\|dog"` |
| **Common Real-World Regex Patterns** | | |
| `r"\d+"` | Extract all numbers | `"100"`, `"45"` |
| `r"#\w+"` | Hashtags | `"#pets"`, `"#ai"` |
| `r"[\w.-]+@[\w.-]+\.\w+"` | Email address | `"user@example.com"` |
| `r"https?://\S+"` | Web URLs | `"https://google.com"` |
| `r"\b\d{10}\b"` | 10-digit mobile number | `"9876543210"` |
| `r"\d{4}-\d{2}-\d{2}"` | Date (YYYY-MM-DD) | `"2026-08-25"` |
| `r"\{.*?\}"` | Extract JSON object string | `{"key": "value"}` |

*"`re.sub(pattern, replacement, text)` matches ko replace karta hai. Yeh text cleaning ke liye lifesaver hai."*

### 💻 Demo — LLM output se cheezein nikaalna
```python
import re

llm_output = "Here is the answer: the total cost is 1500 rupees and the code is ABC123."

numbers = re.findall(r"\d+", llm_output)
print(f"Found numbers: {numbers}")      # Found numbers: ['1500', '123']

code = re.search(r"[A-Z]+\d+", llm_output)
print(f"Found code: {code.group()}")    # Found code: ABC123
```
*"Dekho — AI ka jawaab text hota hai, aur hum regex se usme se zaroori cheezein (numbers, codes) nikaal lete hain. Yeh agents mein bahut kaam aata hai."*

### ❌ Common mistakes
```python
import re
# raw string bhool jaana
re.findall("\d+", text)      # ⚠️ kaam kar sakta hai par r"\d+" likho — safe habit

# search None de toh .group() crash
m = re.search(r"\d+", "no digits here")
print(m.group())             # ❌ AttributeError — pehle check karo: if m:
```

### 🔗 Agentic link
*"LLM output aksar messy hota hai — text ke beech mein JSON, code blocks, numbers chhupe hote hain. Regex se hum unhe nikaalte hain: ` ```python ... ``` ` se code block, ya `\{.*\}` se JSON, ya numbers/emails. CSV se hum eval results aur datasets handle karte hain. Dono real agent-data skills hain."*

### ✍️ Homework
1. Ek CSV file 3 students ke naam+marks ke saath banao aur `DictReader` se padho.
2. Ek sentence se saare numbers `re.findall(r"\d+")` se nikaalo.
3. Ek text se saare hashtags (`#word`) nikaalo.

**Answers:**
```python
import csv, re
# 1
with open("s.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerows([["Name", "Marks"], ["A", 80], ["B", 90], ["C", 70]])
with open("s.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["Name"], row["Marks"])

# 2
print(re.findall(r"\d+", "I am 17, born in 2009"))   # ['17', '2009']

# 3
print(re.findall(r"#\w+", "Loving #python and #ai"))  # ['#python', '#ai']
```

### 🔗 Agli class
*"Agli class — week ka finale: commands chalana (subprocess) aur proper logging, phir ek Notes/Chat-log app banayenge. Security par bhi dhyaan."*

---

## CLASS 60 — subprocess & logging (Project Class)

*"Aaj do professional cheezein: (1) Python se doosre programs/commands chalana (subprocess) — agents ko 'code run karne' ki taakat deta hai. (2) Proper LOGGING — `print` se behtar tareeka apne program ko track karne ka. Dono mein SECURITY zaroori hai."*

### 🎯 Today's goal
`subprocess` se safe command-running, aur `logging` (print ke bajaye).

### 👨‍🏫 Concept 1 — subprocess (commands chalana)

> **📖 Technical definition — `subprocess`:** The `subprocess` module runs external programs from Python as separate processes and can capture their output and exit code. Passing the command as a list of arguments (rather than a shell string) avoids shell interpretation and command-injection risks.

```python
import subprocess

# ek command chalao aur output capture karo
result = subprocess.run(
    ["python", "--version"],        # command ek LIST mein (safe!)
    capture_output=True,
    text=True,
)
print(result.stdout)        # Python 3.15.x
print(result.returncode)    # 0 (0 = success)

import subprocess
result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(result.stdout)

import subprocess
# Run command to check git version
result = subprocess.run(["git", "--version"], capture_output=True, text=True)
print("Output:", result.stdout.strip())
print("Return Code:", result.returncode)  # 0 means success


```

*"`subprocess.run()` ek command chalata hai. Dhyaan do — command ek LIST hai `["python", "--version"]`, ek string nahi. Yeh bahut important hai (agla concept dekho)."*

### 👨‍🏫 ⚠️ Concept 2 — SECURITY: `shell=True` se bachо
*"Yeh ek BADA security rule hai. Kabhi bhi user input ko `shell=True` ke saath command mein mat daalo — woh apne commands chhup ke chala sakta hai (command injection)."*
```python
import subprocess

# ❌ KHATARNAK — user input + shell=True
user_input = "test.txt; rm -rf /"        # user kuch bhi daal sakta hai
# subprocess.run(f"cat {user_input}", shell=True)   # ❌ DISASTER

#rm -rf /: A notoriously destructive command:
#rm: Remove (delete) files/folders.
#-r (recursive): Delete folders and everything inside them.
#-f (force): Force delete without prompting for confirmation.
#/: The root directory (entire hard drive/system).

# ✅ SAFE — command list ke roop mein, shell=True ke BINA
filename = "test.txt"
subprocess.run(["cat", filename])     # cat use for linux system   # user input ek alag argument, command nahi ban sakta

import subprocess
path = r"complete file path"
# Run command and capture output cleanly
result = subprocess.run(["cmd", "/c", "type", path], capture_output=True, text=True)
print(result.stdout)

```
*"Rule yaad rakho: **command hamesha LIST ke roop mein do, aur `shell=True` se bacho** (especially user/LLM input ke saath). List form mein user ka text ek ARGUMENT rehta hai, command nahi ban sakta. Yeh command injection rokta hai."*

> **Note:** Agents jo 'code execute' karte hain, unka yeh sabse bada khatra hai. Hamesha: (1) command list-form mein, (2) `shell=True` avoid, (3) jahan ho sake input validate/sandbox karo.

### 👨‍🏫 Concept 3 — logging (print se behtar)

> **📖 Technical definition — Logging:** Logging is the practice of recording structured, timestamped messages about a program's execution at severity levels (such as INFO, WARNING, ERROR). Unlike `print`, it can be filtered by level and routed to files, and sensitive data must never be logged.

*"`print` debugging ke liye theek hai, par real apps `logging` use karte hain. Kyun? Logging mein levels (info/warning/error), timestamps, aur aap inhe file mein bhej sakte ho — bina code badle on/off kar sakte ho."*
```python
import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Program started")
logging.warning("Low memory")
logging.error("Something failed")
```
Output:
```
2026-06-28 23:00:00 - INFO - Program started
2026-06-28 23:00:00 - WARNING - Low memory
2026-06-28 23:00:00 - ERROR - Something failed
```
*"Har message ka level aur time aata hai. Production mein aap `level=logging.WARNING` set karke chhoti info chhupा sakte ho — code badle bina. Yeh professional habit hai."*

### 👨‍🏫 ⚠️ Concept 4 — SECURITY: secrets kabhi log mat karo
```python
import logging

api_key = "sk-secret-12345"

logging.info(f"Using API key: {api_key}")    # ❌ NEVER — secret log mein leak ho gaya!

# ✅ safe — secret kabhi mat log karo
logging.info("API key loaded successfully")   # ✅ koi secret nahi
```
*"BAHUT zaroori rule: passwords, API keys, tokens, personal data (phone, email) KABHI log mat karo. Logs aksar dikhte hain (files, dashboards) — secret leak ho sakta hai. Sirf safe info log karo: 'key loaded', 'request done' — value nahi."*

> **Note (logging rule):** Logs mein PII/secrets daalna ek classic security mistake hai. Hamesha 'kaam hua' jaisा outcome log karo, sensitive VALUE nahi.

### 🛠️ Mini Project — Notes/Chat-log App
*"Ek app jo notes save kare (JSON mein, list of dicts — agent message-history ki shakal!), regex se search kare, aur properly log kare. Yeh is poore week ko jodta hai."*
```python
import json
import logging
import re
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

NOTES_FILE = Path("notes.json")


def load_notes() -> list:
    """Load notes from the JSON file (empty list if none)."""
    if not NOTES_FILE.exists():
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_note(text: str) -> None:
    """Add a note with a timestamp and save to JSON."""
    notes = load_notes()
    notes.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
    })
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)
    logging.info("Note saved")          # ✅ no sensitive content logged


def search_notes(keyword: str) -> list:
    """Return notes whose text contains the keyword (case-insensitive)."""
    notes = load_notes()
    return [n for n in notes if re.search(keyword, n["text"], re.IGNORECASE)]


# --- demo ---
save_note("Learned file handling today")
save_note("JSON is the language of AI APIs")
save_note("Practice regex daily")

results = search_notes("json")
print(f"Found {len(results)} note(s):")
for note in results:
    print(f"  [{note['time']}] {note['text']}")
```
*"Yeh app sab use karta hai: JSON (save/load), pathlib (safe file), regex (search), logging (track), aur list-of-dicts (agent memory shape!). Yeh ek mini agent-memory system hai. `ensure_ascii=False` se Hindi/emojis JSON mein theek dikhte hain."*

### ❌ Common mistakes
```python
# shell=True with user input (command injection)
subprocess.run(user_text, shell=True)        # ❌ never

# secret logging
logging.info(f"password={password}")          # ❌ never log secrets

# print ki jagah logging na use karna bade apps mein
print("error happened")                       # bade apps mein logging.error() use karo
```

### 🔗 Agentic link
*"Agents mein: subprocess se 'code execution' tools bante hain (par SAFELY — shell=True nahi, sandboxed). Logging se hum agent ka har step trace karte hain — 'kaunsa tool chala, kya result aaya' — taaki debug kar sakein, par SECRETS (API keys) kabhi log nahi karte. Yeh production agents ki real practices hain."*

### ✍️ Homework
1. `subprocess.run` se `python --version` chalao (list form) aur output print karo.
2. Logging se 3 messages (info, warning, error) print karo timestamps ke saath.
3. Notes app mein ek note add karo aur ek keyword se search karo.

**Answers:**
```python
# 1
import subprocess
r = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(r.stdout.strip())

# 2
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("Started")
logging.warning("Careful")
logging.error("Failed")

# 3 — upar wala notes app use karo:
save_note("Buy groceries")
print(search_notes("groceries"))
```

### 🏁 Week 10 wrap-up*"Yeh week aapne data ko PERSIST karna aur AI ki language seekhi:*
- *Files read/write — permanent memory (Class 56)*
- *pathlib + safe paths — security (Class 57)*
- *JSON — LLM APIs ki language (Class 58)*
- *CSV + regex — table data aur pattern extraction (Class 59)*
- *subprocess + logging + Notes app — safe pro practices (Class 60)*

*Ab aapke programs cheezein YAAD rakh sakte hain aur JSON bol sakte hain — agent memory aur API communication ki neev tayyar. Next week — advanced Python (generators, decorators) jo har agent codebase mein milta hai. Shabaash!"*

### 📝 Weekend revision task
Notes app ko upgrade karo: ek `delete_note(keyword)` function add karo (matching notes hatao, save karo), aur har action ko safely log karo (content log mat karna).

---

## 🎤 Industry Interview Questions — Week 10

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. Why should you open files with a `with` statement instead of `open()` and `close()` manually?**

`with open(...) as f:` is a context manager that guarantees the file is closed automatically when the block ends — even if an exception is raised inside it. Manual `open()`/`close()` leaks file handles if an error occurs before `close()`, which on long-running services can exhaust the OS's file-descriptor limit. The `with` form is shorter, safer, and the standard idiom.

**Q2. What is the difference between JSON and a Python dict, and between `json.dumps`/`loads` and `json.dump`/`load`?**

A Python dict is an in-memory object; JSON is a text format for exchanging data between systems (it's what LLM APIs speak). `json.dumps(obj)` serializes a Python object to a JSON *string*; `json.loads(s)` parses a JSON string back into Python objects. The no-`s` versions work with file objects directly: `json.dump(obj, f)` writes to a file and `json.load(f)` reads from one. Note JSON keys are always strings and it supports only a limited set of types.

**Q3. Why does file encoding (e.g. `encoding="utf-8"`) matter?**

Encoding defines how characters are turned into bytes on disk. If you write with one encoding and read with another, non-ASCII text (Hindi, emojis, accented characters) becomes garbled or raises a `UnicodeDecodeError`. Explicitly specifying `encoding="utf-8"` makes behavior consistent across operating systems (Windows historically defaults to a different codec), which is critical because AI prompts and responses are full of multilingual text.

**Q4. How do you safely build a file path from user-controlled input to avoid path traversal?**

Never concatenate raw user input into a path — inputs like `../../etc/passwd` can escape your intended directory. Validate the filename against a strict allowlist (e.g. only alphanumerics, `.`, `_`, `-`), then resolve the final path and confirm it stays inside the base directory: with `pathlib`, compute `(base_dir / name).resolve()` and check that it `.is_relative_to(base_dir.resolve())`. Reject anything that resolves outside the base. (This is a required security control — user input alone must never determine the target path.)

**Q5. In production, why use the `logging` module instead of `print`, and what must you never log?**

`logging` gives you severity levels (debug/info/warning/error), timestamps, structured output, and configurable destinations, and it can be turned up or down per environment without editing code — `print` gives none of that. Critically, you must never log secrets or sensitive data: API keys, tokens, passwords, or full request/response bodies that may contain them. Log safe fields like operation names, request IDs, and outcomes. Also, when running external commands with `subprocess`, avoid `shell=True` with untrusted input to prevent command injection.
