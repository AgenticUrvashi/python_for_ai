# WEEK 12 — Professional Workflow (Live Class — Hinglish)

> **Note:** Yahan samjhane wali baatein Hinglish mein hain, aur saare Python **topics, terms aur code English mein**. Code blocks woh hain jo aap khud type karoge; terminal commands `bash`/`powershell` blocks mein hain.
>
> **Week promise:** *"Is week hum CODE likhna chhod kar ek REAL ENGINEER ki tarah kaam karna seekhenge: project ko isolate karna (venv), code ko version karna (Git), secrets ko safe rakhna (.env). Week ke end tak aapka pehla portfolio repo GitHub par hoga."*

---

## CLASS 66 — Virtual Environments & pip

*"Ek problem: Project A ko `requests` ka version 2.0 chahiye, Project B ko version 3.0. Agar sab ek jagah install ho, toh takraav (conflict)! Solution: har project ka apna alag 'virtual environment' — ek separate dabba jisme us project ke packages rehte hain. Aaj yahi seekhenge."*

### 🎯 Today's goal
`pip` check/upgrade, `venv` banana/activate karna, `pip install`, aur `requirements.txt`.

### 👨‍🏫 Concept 1 — virtual environment aur `pip` kya hain aur kyun

> **📖 Technical definition — Virtual environment and `requirements.txt`:** A virtual environment is an isolated directory containing its own Python interpreter and installed packages for a single project. A `requirements.txt` file lists the project's package dependencies (and versions), so an identical environment can be recreated elsewhere with `pip install -r requirements.txt`.

> **📖 Technical definition — `pip` (Package Installer for Python):** `pip` is the standard package manager for Python, used to install, update, and manage third-party packages from PyPI (Python Package Index). It comes pre-installed with standard Python distributions.

*"Virtual environment ('venv') ek project ke liye alag, isolated Python setup hai. Iske packages sirf us project mein rehte hain, baaki system se alag. Isse projects ek doosre ko nahi bigaadte."*

#### 🛠️ `pip` Check & Upgrade (Environment setup se pehle)
*"Python install karte hi `pip` pehle se milta hai. Par venv banane se pehle check aur upgrade kar lena achhi habit hai:"*
```bash
# Check karo pip working hai aur version kya hai:
pip --version
# ya:
python -m pip --version

# pip ko latest version par upgrade karo (recommended):
python -m pip install --upgrade pip

# Agar pip missing ho (system Python mein):
python -m ensurepip --default-pip
```

### 👨‍🏫 Concept 2 — venv banao aur activate karo
```bash
# venv banao (ek baar)
python -m venv .venv

# activate karo (har baar jab project par kaam karo)
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Mac/Linux:
source .venv/bin/activate
```
*"`python -m venv .venv` ek `.venv` folder banata hai (project ka dabba). `activate` use 'on' karta hai — ab terminal mein `(.venv)` dikhega, matlab aap us isolated environment ke andar ho. Deactivate karne ke liye bas `deactivate` likho."*

> **Note (Windows):** Agar `Activate.ps1` permission error de, toh ek baar `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` chalao (PowerShell ko scripts chalane ki permission). Yeh common hai aur safe hai.

### 👨‍🏫 Concept 3 — packages install karo (`pip`)
```bash
# venv active hone ke baad:
pip install requests
pip install pydantic
pip list                    # kya-kya installed hai dekho
```
*"Ab jo bhi install hoga, woh SIRF is venv mein jaayega — system Python saaf rahega. `pip list` saare installed packages dikhata hai."*

### 👨‍🏫 Concept 4 — `requirements.txt` (project ki shopping list)
```bash
# saare installed packages + versions ek file mein save karo
pip freeze > requirements.txt
```
File aisi dikhegi:
```
pydantic==2.9.0
requests==2.32.0
```
*"`requirements.txt` aapke project ki 'dependency list' hai. Koi aur (ya aap, naye computer par) bas yeh chala kar wahi setup pa sakta hai:"*
```bash
pip install -r requirements.txt
```
*"`-r` ka matlab 'is file ki saari cheezein install karo'. Yeh 'works on my machine' problem (Week 0 yaad hai?) ka asli solution hai — sabke paas same versions."*

### 💻 Demo — naya project setup
```bash
mkdir my_agent_project
cd my_agent_project
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows
pip install requests
pip freeze > requirements.txt
```
*"Yeh exact 4 steps har naye Python project ki shururat hain. Yeh muscle memory ban-na chahiye."*

### ❌ Common mistakes
```bash
# venv activate karna bhool jaana
pip install requests        # ❌ agar venv active nahi, system mein chala gaya

# .venv ko Git mein daalna (agla class — yeh BADI file hai, ignore karo)
```

### 🔗 Agentic link
*"AI projects mein BAHUT heavy dependencies hoti hain (openai, langchain, numpy, torch...). Inhe alag-alag projects mein isolate karna ZAROORI hai, warna versions takraate hain aur ghante barbaad hote hain. Har professional AI engineer venv use karta hai — koi exception nahi. Yeh pehla 'real engineer' skill hai."*

### ✍️ Homework
1. Ek naya folder banao, usme venv banao aur activate karo.
2. Koi ek package install karo (`requests`) aur `pip list` se dekho.
3. `requirements.txt` banao `pip freeze` se aur use kholkar dekho.

**Answer (commands):**
```bash
mkdir practice_project
cd practice_project
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install requests
pip list
pip freeze > requirements.txt
```

### 🔗 Agli class
*"Agli class — modern packaging (`pyproject.toml`) aur tezi se chalne wale tools jaise `uv`."*

---

## CLASS 67 — Modern Packaging & Lazy Imports

*"`requirements.txt` purana tareeka hai. Modern Python projects `pyproject.toml` use karte hain — ek file jo project ki saari info rakhti hai. Aur naye, super-fast tools (`uv`) ise sambhalte hain. Aaj inse parichay."*

### 🎯 Today's goal
`pyproject.toml` samajhna, `uv` install/usage aur `poetry` ka intro, aur lazy imports (3.15).

### 👨‍🏫 Concept 1 — `pyproject.toml` (project ka ID card)

> **📖 Technical definition — `pyproject.toml`:** `pyproject.toml` is the modern standard configuration file for a Python project. It declares metadata (name, version, required Python version), dependencies, and tool settings in one place, replacing older setup files.

*"`pyproject.toml` ek file hai jo aapke project ki saari jaankari rakhti hai: naam, version, dependencies, settings. Yeh aaj ka standard hai."*
```toml
[project]
name = "my-agent"
version = "0.1.0"
description = "My first AI agent project"
requires-python = ">=3.15"
dependencies = [
    "requests>=2.32",
    "pydantic>=2.9",
]
```
*"Dekho — yeh ek hi file mein project ka naam, version, Python version, aur dependencies sab rakhti hai. Yeh `requirements.txt` + project info, sab ek jagah. Iss repo ka apna `pyproject.toml` bhi aap kholkar dekh sakte ho!"*

### 👨‍🏫 Concept 2 — `uv` (super-fast modern tool)
*"`uv` ek naya, bahut TEZ tool hai (Rust mein bana) jo venv banata hai aur packages install karta hai — `pip` se kai guna fast. Industry tezi se ise apna rahi hai."*

#### 📥 `uv` Install kaise karein (System-wide ek baar)
*"Environment banane ya package management se pehle `uv` ko apne system mein ek baar install karna hota hai:"*
```bash
# Method 1 — pip ke zariye (sabse aasan, cross-platform):
pip install uv

# Method 2 — Standalone official installer:
# Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Check karo install hua ya nahi:
uv --version
```

#### 🚀 `uv` Workflows — Do tareeke (Don't get confused!)
*"`uv` do tarike ke workflows support karta hai. Dono mein se koi bhi galat nahi hai, par modern industry 'Project Workflow' ko official standard maanti hai:"*

> **📖 Technical definition — `uv` Workflows:** `uv` supports two operation modes:
> 1. **Project Management Mode (`uv init`, `uv add`, `uv sync`):** The modern, declarative standard. Uses `pyproject.toml` and `uv.lock` for reproducible dependency locking and automatic environment syncing.
> 2. **Pip-compatible Mode (`uv venv`, `uv pip install`):** A fast drop-in replacement for traditional `python -m venv` and `pip install`, ideal for quick scripts or legacy `requirements.txt` workflows.

---

##### 📊 Summary Table — Which workflow to use?

| Feature | 1. Official Project Workflow (`uv init` / `uv sync`) | 2. Pip-compatible Workflow (`uv venv` / `uv pip`) |
| :--- | :--- | :--- |
| **Best For** | Naye projects & Company/Production repos | Legacy projects & Quick single-script experiments |
| **Config File** | `pyproject.toml` + `uv.lock` | `requirements.txt` (or none) |
| **Venv Creation** | Automatic (`uv sync` / `uv run` handles `.venv`) | Manual (`uv venv`) |
| **Add Packages** | `uv add requests` | `uv pip install requests` |
| **Run Code** | `uv run python main.py` (No activation needed) | Activate `.venv` first, then `python main.py` |

---

#### 💡 Real-World Scenarios (Kaise use karein?)

##### 🌟 Scenario A: Naya Project Banana (New Project Setup)
Agar aap scratch se ek naya Python/AI project shuru kar rahe ho:
```bash
# 1. Project initialize karo (folder + pyproject.toml + gitignore banega):
uv init my_agent_app
cd my_agent_app

# 2. Packages add karo (pyproject.toml update hoga + uv.lock banega + .venv sync hoga):
uv add requests pydantic

# 3. Code run karo (bina venv activate kiye!):
uv run python main.py
```

##### 🏢 Scenario B: Existing Company Project mein Setup Karna (Company Project Workflow)
Agar aap kisi company mein ho ya GitHub se koi purana project clone kiya hai:

* **Case 1: Project mein `requirements.txt` hai (Traditional Repo):**
  ```bash
  cd existing_company_project

  # Fast .venv banao aur requirements.txt install karo:
  uv venv
  # Windows: .venv\Scripts\Activate.ps1  |  Mac/Linux: source .venv/bin/activate
  uv pip install -r requirements.txt
  ```

* **Case 2: Company Project ko Modern `uv` (`pyproject.toml`) mein Migrate karna ho:**
  ```bash
  cd existing_company_project

  # 1. Existing folder mein pyproject.toml add karo:
  uv init --bare

  # 2. Existing requirements.txt ke packages pyproject.toml mein import karo:
  uv add -r requirements.txt

  # 3. Exact lockfile aur environment create karo:
  uv sync
  ```

*"Concept samajhna kaafi hai abhi: `uv` wahi kaam karta hai jo `pip`+`venv`, par bahut tez aur `pyproject.toml` ke saath smooth. (Poetry ek aur popular tool hai — same idea.) Aap aage inme se koi use karoge."*

### 👨‍🏫 Concept 3 — semantic versioning (`>=`, `==`, `~=`)

> **📖 Technical definition — Semantic versioning:** Semantic versioning labels releases as `MAJOR.MINOR.PATCH`, where MAJOR marks incompatible changes, MINOR adds backward-compatible features, and PATCH fixes bugs. Version specifiers like `>=`, `==`, and `~=` constrain which versions a dependency may use.

* **🔢 Version Format:** `MAJOR.MINOR.PATCH` (e.g., `2.32.0`)
  * **MAJOR (2):** Breaking changes (old code might break).
  * **MINOR (32):** New features added safely (backward-compatible).
  * **PATCH (0):** Small bug fixes.

```toml
"requests>=2.32"     # 2.32 ya usse naya
"requests==2.32.0"   # bilkul yahi version (exact)
"requests~=2.32"     # 2.32 se compatible (2.x, par 3.0 nahi)
```
*"Version numbers `MAJOR.MINOR.PATCH` hote hain (jaise 2.32.0). `>=` 'isse naya bhi chalega', `==` 'bilkul yahi'. AI projects mein versions pin karna (`==`) reproducibility ke liye accha hai."*

### 👨‍🏫 Concept 4 — lazy imports (Python 3.15)

> **📖 Technical definition — Lazy import:** A lazy import defers loading a module until the moment it is actually needed (for example, inside the function that uses it), rather than at program startup. This speeds up start time when a heavy module may not always be used.

*"Normally `import` poora module turant load karta hai — agar bhaari ho toh program start slow. Idea: module ko TAB load karo jab pehli baar zaroorat ho ('lazy'). Python 3.15 ise behtar support karta hai, aur fast CLI tools banane mein madad karta hai."*
```python
# concept: bhaari import ko function ke andar daal do (zaroorat par hi load)
def use_heavy():
    import numpy as np          # sirf jab yeh function chale, tab load
    return np.array([1, 2, 3])
# program start fast — numpy tabhi load hua jab use_heavy() bula
```
*"Simple version: bhaari module ko function ke andar import karo — woh tabhi load hoga jab function chale. Yeh CLI agents ko fast start karta hai (har baar saari heavy AI libraries load nahi hoti). Python 3.15 isko aur smooth banata hai."*

### ❌ Common mistakes
```toml
[project]
name = my-agent         # ❌ value quotes mein honi chahiye: name = "my-agent"

dependencies = "requests"   # ❌ list honi chahiye: ["requests"]
```

### 🔗 Agentic link
*"Modern AI projects `pyproject.toml` + `uv`/`poetry` use karte hain — clean dependency management. Aur lazy imports CLI agents (jaise ek terminal-based AI assistant) ko fast start dete hain, kyunki saari bhaari ML libraries ek saath load nahi hoti. Yeh professional packaging skills hain."*

### ✍️ Homework
1. Is repo ka `pyproject.toml` kholkar padho — naam aur dependencies dhoondho.
2. Ek apna `pyproject.toml` likho with naam, version, description.
3. Ek function banao jisme heavy import (`import json`) andar ho (lazy style).

**Answers:**
```toml
# 2 — pyproject.toml
[project]
name = "my-first-agent"
version = "0.1.0"
description = "Learning project for agentic AI"
requires-python = ">=3.15"
dependencies = []
```
```python
# 3
def parse(text):
    import json            # lazy import
    return json.loads(text)
print(parse('{"a": 1}'))   # {'a': 1}
```

### 🔗 Agli class
*"Agli class — project structure: code ko folders mein professional tareeke se organize karna."*

---

## CLASS 68 — Project Structure

*"Ab tak hamari files ek folder mein bikhri hain. Real projects mein ek SAAF structure hota hai — har cheez ki apni jagah. Achha structure project ko samajhne aur grow karne mein aasan banata hai. Aaj ek professional layout seekhenge."*

### 🎯 Today's goal
Ek clean project structure banana: `src/`, modules, `README.md`, `.gitignore`.

### 👨‍🏫 Concept 1 — ek achha project kaisा dikhta hai
```
my_agent_project/
├── .venv/                  # virtual environment (Git mein NAHI)
├── src/                    # saara source code yahan
│   ├── __init__.py         # batata hai 'yeh ek package hai'
│   ├── tools.py            # tool functions
│   ├── agent.py            # agent class
│   └── main.py             # entry point (program yahan se chalta hai)
├── tests/                  # test files (Week 13)
│   └── test_tools.py
├── .env                    # secrets (Git mein NAHI)
├── .gitignore             # Git ko batata hai kya ignore kare
├── requirements.txt        # ya pyproject.toml
└── README.md               # project ka description
```
*"Dekho har cheez ki apni jagah: code `src/` mein, tests `tests/` mein, secrets `.env` mein, info `README.md` mein. Yeh structure har professional project mein milta hai."*

### 👨‍🏫 Concept 2 — `__init__.py` (folder ko package banao)

> **📖 Technical definition — Package and `__init__.py`:** A package is a directory containing related Python modules. Placing an `__init__.py` file inside a directory marks it as a package. Beyond marking package boundaries, `__init__.py` runs automatically when the package is imported, allowing package-level exports (shortcuts), package initialization code, and defining public APIs via `__all__`.

*"Agar ek folder mein `__init__.py` ho, toh Python use ek 'package' maanta hai. `__init__.py` 2 main kaam karta hai:*
*1. **Folder ko Package banana** (marking the directory).*
*2. **Clean Import Shortcuts (Re-exports)**: lambe imports ko chhota aur clean banana.*

#### 💡 Practical Example — Clean Package Surface

##### 📁 Folder Structure:
```text
my_project/
├── src/
│   ├── __init__.py        # Package header & shortcuts
│   ├── tools.py           # Tool functions (add, subtract)
│   └── agent.py           # Agent class
└── main.py                # Entry point
```

##### 📄 `src/tools.py`:
```python
def add(a: int, b: int) -> int:
    return a + b
```

##### 📄 `src/agent.py`:
```python
class Agent:
    def __init__(self, name: str):
        self.name = name
```

---

#### 🔄 Two Ways to use `__init__.py`:

##### 1. Basic Way (Empty `__init__.py`):
*"Agar `src/__init__.py` bilkul khaali (empty file) ho, toh aapko exact sub-module file path se import karna padega:"*
```python
# main.py mein:
from src.tools import add
from src.agent import Agent
```

##### 2. Professional Way (Re-exporting Shortcuts inside `src/__init__.py`):
*"Agar hum `src/__init__.py` ke andar shortcuts expose kar dein:"*
```python
# src/__init__.py
from .tools import add
from .agent import Agent

__version__ = "1.0.0"
__all__ = ["add", "Agent"]
```

*"Ab `main.py` mein import kitna clean ho gaya! Direct package se sab mil jayega:"*
```python
# main.py mein (Clean & Elegant import):
from src import Agent, add

agent = Agent("Assistant")
print(add(5, 10))
```

*"`__init__.py` aapke internal folder structure ki complexity chhupa kar ek clean interface (public API) deta hai. Large projects mein yeh sabse badi strength hai."*

### 👨‍🏫 Concept 3 — `README.md` (project ka chehra)
*"`README.md` Markdown mein likha project ka introduction hai. Jab koi GitHub par aapka project khole, yeh pehli cheez dikhti hai. Isme hota hai:"*
```markdown
# My Agent Project

A simple AI agent built in pure Python.

## Setup
1. Create venv: `python -m venv .venv`
2. Activate it
3. Install: `pip install -r requirements.txt`

## Usage
Run: `python src/main.py`

## Features
- Calculator tool
- Time tool
```
*"Achha README = log aapka project samajh paate hain aur use kar paate hain. Yeh aapke portfolio ka chehra hai — recruiters yeh padhte hain!"*

### 👨‍🏫 Concept 4 — `.gitignore` (kya Git mein NA jaaye)

> **📖 Technical definition — `.gitignore`:** `.gitignore` is a text file listing file and folder patterns that Git should not track. It keeps generated files, virtual environments, and secret files (like `.env`) out of the repository.

*"Kuch cheezein Git mein kabhi nahi jaani chahiye: venv (badi, dobara ban sakti hai), secrets (.env), cache files. `.gitignore` Git ko batata hai inhe ignore karo."*
```gitignore
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```
*"Yeh BAHUT important hai — especially `.env` (secrets). Agla class Git, aur uske baad secrets. `.gitignore` aapko galti se secrets push karne se bachata hai."*

### ❌ Common mistakes
```
# sab kuch ek file mein (1000 lines ki main.py) — ❌ todo modules mein
# .env ko Git mein daalna — ❌ secrets leak! .gitignore use karo
# README na likhna — ❌ koi nahi samajhega project kaise chale
```

### 🔗 Agentic link
*"Real agent projects bade hote hain: tools, agent logic, prompts, config, tests — sab alag. Achhi structure se aap (aur aapki team) ise manage kar paate ho. Aur ek saaf README + structure aapke portfolio ko professional dikhata hai jab aap AI jobs ke liye apply karoge. Yeh seedhe career skill hai."*

### ✍️ Homework
1. Apne purane kisi project ko is structure mein reorganize karo (`src/`, README).
2. Ek `README.md` likho with setup aur usage sections.
3. Ek `.gitignore` banao jisme `.venv/`, `.env`, `__pycache__/` ho.

**Answer (structure):**
```
practice_project/
├── src/
│   ├── __init__.py
│   ├── tools.py
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

### 🔗 Agli class
*"Agli class — Git aur GitHub: apne code ko 'save points' dena aur duniya ke saath share karna. Har engineer ka roz ka tool."*

---

## CLASS 69 — Git & GitHub

*"Git ek 'time machine' hai aapke code ke liye — har 'save point' (commit) par aap wapas jaa sakte ho. GitHub woh jagah hai jahan aap apna code online rakhte ho (backup + sharing + portfolio). Yeh har engineer ka roz ka tool hai, aur jobs mein zaroori."*

### 🎯 Today's goal
Git basics (`init/add/commit/status/log`), branches, aur GitHub par push.

### 👨‍🏫 Concept 1 — Git kya karta hai
*"Git aapke project ke 'snapshots' (commits) save karta hai. Galti ho gayi? Purane commit par wapas. Naya feature try karna? Ek branch banao. Yeh aapko bina dar ke experiment karne deta hai."*

### 👨‍🏫 Concept 2 — basic Git workflow (4 commands)

> **📖 Technical definition — Commit and branch:** A commit is a saved snapshot of the project's tracked files at a point in time, with a descriptive message. A branch is an independent line of commits that lets you develop changes separately from the main code and merge them back later.

```bash
git init                    # is folder ko Git project banao (ek baar)
git status                  # kya badla hai dekho
git add .                   # saari changes 'stage' karo (commit ke liye taiyar)
git commit -m "First commit"    # ek snapshot save karo with message
```
*"Flow yaad rakho: change karo → `git add` (taiyar karo) → `git commit` (save karo). Har commit ek save-point hai. `git status` har kadam par dekhne ke liye — yeh aapka best friend hai."*

### 👨‍🏫 Concept 3 — commit messages (achhe likho)
```bash
git commit -m "Add calculator tool"        # ✅ saaf, batata hai kya hua
git commit -m "stuff"                       # ❌ bekaar — 6 mahine baad samajh nahi aayega
```
*"Achha commit message batata hai aapne KYA kiya. 'Add X', 'Fix Y', 'Update Z' style use karo. Future-aap aapko dhanyavaad denge."*

### 👨‍🏫 Concept 4 — history dekho aur branches
```bash
git log --oneline           # saare commits ki list (chhoti)

git branch feature-x        # nayi branch banao (alag line of work)
git checkout feature-x      # us branch par jao
# ya ek saath:
git checkout -b feature-x
```
*"Branch ek alag 'line of work' hai — main code ko bina chhede naya feature try karo. Kaam ho gaya toh merge kar do. Teams isse parallel kaam karti hain."*

### 👨‍🏫 Concept 5 — GitHub par push
```bash
# GitHub par ek naya (khaali) repo banao, phir:
git remote add origin https://github.com/yourname/my-project.git
git branch -M main
git push -u origin main         # code online chala gaya!
```
*"`git push` aapka local code GitHub par bhej deta hai — backup + sharing + portfolio. Ab duniya (aur recruiters) aapka kaam dekh sakte hain. Pehli baar `-u origin main` set karta hai; uske baad bas `git push`."*

### 👨‍🏫 ⚠️ Concept 6 — pehle `.gitignore` (secrets push mat karo!)
*"Push karne se PEHLE confirm karo `.gitignore` mein `.env` hai. Warna aapke API keys GitHub par public ho jaayenge — ek bahut common aur khatarnak galti. Hamesha `git status` se check karo ki `.env` 'untracked/ignored' hai, commit hone wali files mein nahi."*

### ❌ Common mistakes
```bash
git commit -m "msg"         # ❌ agar 'git add' nahi kiya, kuch commit nahi hoga
# pehle git add karo

# .env commit kar dena → ❌ secrets leak (gitignore use karo)
# git add karne se pehle git status se check karo kya-kya add hoga
```

### 🔗 Agentic link
*"SAARA professional AI development Git par chalta hai: collaboration, code review, deployment, version history — sab. Aapke agent projects GitHub par aapka portfolio banenge, jo AI jobs/internships ke liye zaroori hai. 'Show me your GitHub' har AI interview mein poocha jaata hai. Aaj aapne woh foundation rakhi."*

### ✍️ Homework
1. Apne kisi project mein `git init`, `git add .`, `git commit -m "..."` karo.
2. `git log --oneline` se apni commit history dekho.
3. (Bonus) GitHub account banao aur ek repo push karne ki koshish karo.

**Answer (commands):**
```bash
cd my_project
git init
git add .
git commit -m "Initial commit: tools module"
git log --oneline
# GitHub repo banane ke baad:
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

### 🔗 Agli class
*"Agli class — week ka finale: secrets ko safe rakhna (.env), aur code ki speed measure karna (profiling). Phir aapka pehla portfolio repo!"*

---

## CLASS 70 — Secrets & Profiling (Project Class)

*"Aaj do cheezein: (1) API keys ko CODE se BAHAR rakhna (.env files) — yeh AI mein critical security hai. (2) Apne code ke slow hisse dhoondhna (profiling). Phir hum sab jod kar aapka pehla portfolio repo banayenge!"*

### 🎯 Today's goal
`.env` + `python-dotenv` se secrets, aur basic profiling.

### 👨‍🏫 ⚠️ Concept 1 — secrets KABHI code mein nahi
```python
# ❌ KABHI aisा mat karo:
api_key = "sk-1234567890abcdef"     # ❌ code mein hard-coded secret!
# agar yeh GitHub par gaya, koi bhi aapki key use kar lega (aur aapka paisa!)
```
*"Yeh sabse badi security galti hai jo beginners karte hain. API keys, passwords — yeh KABHI code mein nahi likhne. Kyun? Code Git mein jaata hai, Git GitHub par, aur secret public ho jaata hai. Hackers bots se aise keys turant pakad lete hain."*

### 👨‍🏫 Concept 2 — `.env` file (secrets ka safe ghar)

> **📖 Technical definition — Environment variables and `.env`:** Environment variables are configuration values stored outside the source code, in the process environment. A `.env` file holds such values (like API keys) locally and is loaded at runtime, keeping secrets out of the code and out of version control.

*"Secrets ek alag `.env` file mein rakho jo Git mein KABHI nahi jaati (gitignore!)."*
```
# .env file (yeh Git mein nahi jaati)
OPENAI_API_KEY=sk-your-real-key-here
DATABASE_URL=postgres://localhost/mydb
```
```python
# code mein .env se load karo:
import os
from dotenv import load_dotenv      # pip install python-dotenv

load_dotenv()                       # .env file padho

api_key = os.getenv("OPENAI_API_KEY")   # environment se lo, code se nahi
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in .env")
```
*"`load_dotenv()` `.env` file padhta hai, aur `os.getenv("KEY")` se hum value lete hain — code mein secret kahin likha nahi. `.env` gitignore mein hai, toh woh kabhi push nahi hoti. Yeh standard, safe tareeka hai."*

### 👨‍🏫 Concept 3 — `.env.example` (template, bina secrets)
```
# .env.example (yeh Git mein JAA sakti hai — sirf keys, values khaali)
OPENAI_API_KEY=
DATABASE_URL=
```
*"Ek `.env.example` rakho jisme sirf key-NAAM ho, values khaali. Yeh batata hai 'is project ko yeh secrets chahiye' bina asli values leak kiye. Naya developer ise copy karke apni values bhar leta hai. Best practice."*

### 👨‍🏫 Concept 4 — profiling (slow hisse dhoondho)

> **📖 Technical definition — Profiling:** Profiling is measuring where a program spends its time (or memory) during execution, so optimisation efforts target the actual bottlenecks. Tools range from simple timers to `cProfile`, which reports the time taken by each function.

*"Jab code slow ho, ANDAAZ mat lagao kahan slow hai — MEASURE karo. Simple timing:"*
```python
import time

start = time.perf_counter()
total = sum(range(10_000_000))      # kuch bhaari kaam
elapsed = time.perf_counter() - start
print(f"Took {elapsed:.3f} seconds")
```
*"`time.perf_counter()` precise timing deta hai. Bade code ke liye Python ka `cProfile` module har function ka time dikhata hai (Python 3.15 ne profiling tools improve kiye hain). Rule: 'measure, don't guess' — slow part dhoondh kar usi ko fix karo."*
```bash
# poore script ka profile (kaunsa function kitna time leta hai):
python -m cProfile myscript.py
```

### 🛠️ Mini Project — Portfolio Repo #1
*"Ab sab jodte hain. Aapka pehla professional, portfolio-ready repo:"*

**Structure:**
```
my-tools-project/
├── .venv/              # (gitignored)
├── src/
│   ├── __init__.py
│   ├── tools.py        # aapke typed, documented tools (Week 6+11)
│   └── main.py
├── .env                # (gitignored) — agar koi key ho
├── .env.example        # template
├── .gitignore
├── requirements.txt
└── README.md
```

**`src/main.py`:**
```python
import os
from dotenv import load_dotenv
from src.tools import add, word_count, get_current_time

load_dotenv()

def main():
    print("=== My Tools Demo ===")
    print(f"Time: {get_current_time()}")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Word count: {word_count('hello world python')}")

if __name__ == "__main__":
    main()
```

**Steps:**
```bash
git init
# .gitignore mein .venv/, .env, __pycache__/ daalo
git add .
git status                  # CONFIRM: .env list mein NAHI hai
git commit -m "Add tools module with clean structure"
# GitHub repo banao, phir:
git remote add origin <url>
git branch -M main
git push -u origin main
```
*"Mubarak ho! Yeh aapka pehla professional repo hai — clean structure, README, gitignored secrets, version-controlled, GitHub par live. Yeh aapke AI portfolio ka pehla piece hai. Recruiters yeh dekhenge!"*

### ❌ Common mistakes
```python
api_key = "sk-real-key"     # ❌ hard-coded — use .env

# .env ko gitignore mein daalna bhool jaana → secret push ho gaya
# fix: turant key revoke/regenerate karo, .gitignore add karo
```

### 🔗 Agentic link
*"Yeh agents ke liye CRITICAL hai: har agent ko LLM API keys chahiye, aur woh HAMESHA `.env` se aati hain, kabhi code se nahi. Ek leaked OpenAI key se hazaron rupaye ka nuksaan ho sakta hai. Aur profiling se hum agents ke slow steps (jaise zyada API calls) dhoondh kar optimize karte hain. Aapne ab tak ka poora 'pure Python' professionally complete kar liya!"*

### ✍️ Homework
1. Ek `.env` file banao with ek dummy key, aur use `python-dotenv` se load karke print karo (asli secret nahi — dummy).
2. `.env.example` banao (key naam, khaali value).
3. Apne tools project ko Week 12 ki sab cheezon (venv, structure, gitignore, README, git) ke saath complete karo.

**Answers:**
```python
# .env file:
# MY_KEY=hello123

# 1
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("MY_KEY"))      # hello123

# 2  — .env.example:
# MY_KEY=
```

### 🏁 Week 12 wrap-up*"Yeh week aapne ENGINEER ki tarah kaam karna seekha:*
- *venv & pip — isolated projects (Class 66)*
- *pyproject.toml, uv, lazy imports (Class 67)*
- *Project structure — clean layout (Class 68)*
- *Git & GitHub — version control + portfolio (Class 69)*
- *Secrets (.env) & profiling + portfolio repo (Class 70)*

*Ab aap professional workflow jaante ho aur aapka pehla repo GitHub par hai! Ab tak aapne POORA core Python + professional skills cover kar liya. Next week — TESTING: code ke saath proof ki woh kaam karta hai. Shabaash!"*

### 📝 Weekend revision task
Apne portfolio repo ka README.md improve karo: features list, setup steps, ek example output. Yeh aapke career ka pehla showcase hai — ise sundar banao!

---

## 🎤 Industry Interview Questions — Week 12

> Real interview-style questions covering this week's topics, with model answers (in English). Try to answer them yourself first, then read the solution.

**Q1. What is the difference between `requirements.txt` and `pyproject.toml`, and why pin versions?**

`requirements.txt` is a simple flat list of packages (optionally with versions) for `pip install -r`. `pyproject.toml` is the modern, richer standard that declares project metadata, dependencies, and tool config in one place, and is what tools like `uv` and build systems use. You pin versions (and use a lock file) so every developer and every CI/production machine installs the *exact same* dependency versions — otherwise "works on my machine" bugs appear when a dependency silently updates.

**Q2. Describe the basic Git workflow and what a good commit message looks like.**

The core loop is: `git add` (stage changes) → `git commit -m "..."` (save a snapshot to local history) → `git push` (upload to the remote, e.g. GitHub). A good commit message has a short imperative summary line ("Add retry logic to LLM client") explaining the *why*, not just restating the diff, so history is readable. Small, focused commits are easier to review and revert than giant ones.

**Q3. How do you keep secrets out of your code and out of Git?**

Store secrets (API keys, DB passwords) in environment variables, typically loaded from a `.env` file, and read them in code with something like `os.environ`. Add `.env` to `.gitignore` so it's never committed, and commit a `.env.example` with blank placeholder values to document what's needed. Never hard-code secrets in source. Always run `git status` before pushing, and if a secret is ever committed, rotate it immediately — removing it from history is not enough.

**Q4. What is profiling, and when should you optimize?**

Profiling measures where a program actually spends its time (using tools like `cProfile` or `timeit`), so you optimize based on evidence, not guesses. The rule is: make it correct first, then measure, then optimize only the proven bottleneck. Premature optimization wastes effort and adds complexity; often the slow part is something surprising (an N+1 loop, an un-cached API call) that only a profiler reveals.

**Q5. What does a clean project structure look like and why does `__init__.py` matter?**

A clean layout separates source code (often a `src/` package), tests, and docs, with a `README.md`, dependency files, and `.gitignore` at the root. `__init__.py` marks a directory as a Python *package* so its modules can be imported with dotted paths (`from myproject.tools import add`) and controls what the package exposes. Good structure makes a project easy to navigate, test, package, and hand off — a signal of professional work to reviewers and recruiters.
