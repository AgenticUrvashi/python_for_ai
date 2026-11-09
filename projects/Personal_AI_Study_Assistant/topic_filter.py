"""
Topic Filter for Personal AI Study Assistant (StudySync Pro)
Enforces strict study-only rule:
- Returns True ONLY if the question is academic, study, homework, or educational.
- Returns False if the question is chit-chat, entertainment, sports, politics, gossip, or non-educational.
"""

import re
from typing import Optional

# Comprehensive academic/study keywords (English + Hinglish academic terms)
STUDY_KEYWORDS = {
    # Computer Science & Programming
    "python", "programming", "code", "coding", "algorithm", "data structure", "array",
    "linked list", "stack", "queue", "tree", "graph", "binary search", "sorting",
    "recursion", "oop", "class", "function", "variable", "loop", "syntax", "debug",
    "compiler", "interpreter", "database", "sql", "html", "css", "javascript",
    "c++", "java", "react", "machine learning", "deep learning", "neural network",
    "artificial intelligence", "nlp", "computer", "software", "hardware", "operating system",
    "git", "github", "api", "json", "rest", "frontend", "backend", "fullstack",
    "big-o", "time complexity", "space complexity", "pointer", "memory", "async",
    
    # Mathematics & Calculations
    "math", "mathematics", "algebra", "calculus", "geometry", "trigonometry", "matrix",
    "matrices", "vector", "derivative", "integration", "integral", "probability",
    "statistics", "equation", "formula", "theorem", "fraction", "percentage",
    "arithmetic", "logarithm", "quadratic", "polynomial", "differentiation",
    "pythagoras", "mean", "median", "mode", "variance", "standard deviation",
    
    # Sciences
    "science", "physics", "chemistry", "biology", "atom", "molecule", "cell",
    "photosynthesis", "gravity", "force", "velocity", "acceleration", "thermodynamics",
    "optics", "quantum", "dna", "rna", "genetics", "organism", "chemical reaction",
    "periodic table", "element", "compound", "energy", "electricity", "magnetism",
    "respiration", "mitosis", "meiosis", "evolution", "ecology", "ecosystem",
    "newton", "einstein", "bohr", "electron", "proton", "neutron", "acid", "base",
    
    # General Academic & School / College
    "study", "learn", "explain", "explanation", "definition", "define", "solve",
    "solution", "homework", "exam", "quiz", "test", "assignment", "syllabus",
    "notes", "summary", "tutorial", "revision", "concept", "theory", "derive",
    "derivation", "difference between", "compare", "contrast", "history", "geography",
    "economics", "civics", "literature", "english", "grammar", "vocabulary",
    "essay", "paragraph", "comprehension", "sample paper", "ncert", "cbse",
    "flashcard", "mnemonic", "question", "answer", " viva", "practical",

    # Hinglish Academic phrasing
    "padhai", "samjhao", "batao", "kaise kare", "kya hota hai", "kya hai",
    "kaise kaam karta", "antar", "udaharan", "sawaal", "prashna", "formula kya",
    "definition kya", "kaise solve kare", "kaise likhein"
}

# Explicit non-study topics (blacklist)
NON_STUDY_PATTERNS = [
    # Entertainment & Bollywood/Hollywood
    r"\b(movie|film|cinema|song|songs|music|lyrics|actor|actress|bollywood|hollywood)\b",
    r"\b(salman khan|shahrukh khan|srk|deepika|ranbir|alia bhatt|katrina|akshay kumar)\b",
    r"\b(box office|trailer|teaser|netflix|web series|episode|ott)\b",
    
    # Sports & Games
    r"\b(ipl|cricket score|football match|fifa|world cup match|who won the match)\b",
    r"\b(virat kohli|rohit sharma|dhoni|messi|ronaldo|ipl score)\b",
    r"\b(pubg|free fire|gta|bgmi|video game cheat|gaming)\b",
    
    # Romance, Flirting & Dating
    r"\b(girlfriend|boyfriend|gf|bf|love|date me|marry me|kiss|crush|flirt|romance)\b",
    r"\b(tum mujhse pyar|are you single|do you love me)\b",
    
    # Gossip, Personal & Casual Chitchat
    r"\b(gossip|rumor|weather today|aaj ka mausam|horoscope|rashifal|astrology)\b",
    r"\b(recipe|khana banana|biryani kaise|cooking|makeup tips|fashion tips)\b",
    
    # Politics & Non-educational debates
    r"\b(modi vs|rahul gandhi|election result|bjp vs congress|political gossip)\b"
]

def is_math_expression(text: str) -> bool:
    """Detect if the text is primarily a math calculation or equation."""
    has_digit = any(char.isdigit() for char in text)
    has_operator = any(symbol in text for symbol in ["+", "-", "*", "/", "^", "%", "="])
    
    # Simple arithmetic string like "25 * 4 + 10" or "solve 3x + 5 = 20"
    if has_digit and has_operator:
        return True
    return False

def is_study_related(question: str) -> bool:
    """
    Evaluates if question is strictly study-related.
    Returns: True if study-related, False otherwise.
    """
    if not question or not question.strip():
        return False
        
    cleaned = question.strip().lower()
    
    # 1. First check explicit non-study patterns (blacklist)
    for pattern in NON_STUDY_PATTERNS:
        if re.search(pattern, cleaned, re.IGNORECASE):
            return False
            
    # 2. Check if it's a math expression or calculation
    if is_math_expression(cleaned):
        return True
        
    # 3. Check for presence of study keywords
    words = re.findall(r"\b[a-z0-9+#.-]+\b", cleaned)
    for word in words:
        if word in STUDY_KEYWORDS:
            return True
            
    # 4. Check for multi-word study phrases
    for keyword in STUDY_KEYWORDS:
        if " " in keyword and keyword in cleaned:
            return True
            
    # 5. Check academic question starters
    academic_starters = [
        "what is", "how to solve", "how does", "why does", "explain the", "explain",
        "calculate", "differentiate between", "write a code", "write a program",
        "give an example of", "find the value of", "step by step solution",
        "what are the types of", "definition of", "formula for", "summary of",
        "summarize", "help me understand", "teach me", "prepare for", "notes on",
        "how to implement", "generate a quiz", "flashcards for"
    ]
    for starter in academic_starters:
        if cleaned.startswith(starter):
            return True

    return False


# =====================================================================
# Polite Student Conversational Handling (Greetings, Farewells, Gratitude)
# =====================================================================

FAREWELL_REGEX = re.compile(
    r"^(?:ok\s+|okay\s+|thanks\s+|thank you\s+|chalo\s+|chal\s+)?"
    r"(?:bye(?:\s+bye)?|byee+|goodbye|good\s+bye|alvida|see\s+(?:you|ya|u)(?:\s+soon|\s+later)?|cya|tata|good\s*night|gn|take\s+care|have\s+a\s+(?:good|nice|great)\s+day|bye\s+for\s+now|chalta\s+hu|chalti\s+hu)"
    r"[!.\s]*$",
    re.IGNORECASE
)

GRATITUDE_REGEX = re.compile(
    r"^(?:ok\s+|okay\s+|many\s+|bahut\s+|bohot\s+)?"
    r"(?:thanks(?:\s+a\s+lot|\s+so\s+much|\s+buddy|\s+bro|\s+sir|\s+ma\'?am)?|thank\s+(?:you|u)(?:\s+so\s+much|\s+very\s+much|\s+a\s+lot)?|dhanyawa?d(?:\s+ji)?|shukriya(?:\s+ji)?|tysm|thx)"
    r"[!.\s]*$",
    re.IGNORECASE
)

GREETING_REGEX = re.compile(
    r"^(?:hi+|hello+|hey+|namaste|namaskar|pranam|good\s+(?:morning|afternoon|evening)|how\s+are\s+you|how\s+r\s+u|kaise\s+ho(?:\s+aap)?|kese\s+ho|kya\s+haal\s+hai|what\'?s\s+up|wassup|sup)"
    r"[!.\s]*$",
    re.IGNORECASE
)

ACKNOWLEDGMENT_REGEX = re.compile(
    r"^(?:ok+|okay|theek\s+hai|thik\s+hai|theek\s+h|thik\s+h|achha|achha\s+theek\s+hai|(?:i\s+)?got\s+it|understood|samajh\s+(?:gaya|gayi|aa\s*gaya)|sure(?:\s+thing)?|all?\s*right|perfect|cool|nice|great|awesome|done)"
    r"[!.\s]*$",
    re.IGNORECASE
)

IDENTITY_REGEX = re.compile(
    r"^(?:who\s+are\s+you|who\s+r\s+u|tum\s+kaun\s+ho|aap\s+kaun\s+ho|who\s+made\s+you|what\s+is\s+your\s+name|tumhara\s+naam\s+kya\s+hai|what\s+can\s+you\s+do)"
    r"[!.\s\?]*$",
    re.IGNORECASE
)

def detect_conversational_intent(text: str) -> Optional[str]:
    """
    Detects polite student conversational intents (greeting, farewell, gratitude, acknowledgment, identity).
    Returns intent name ('farewell', 'gratitude', 'greeting', 'acknowledgment', 'identity') or None.
    """
    if not text or not text.strip():
        return None
    cleaned = text.strip()

    # If the text is an arithmetic/math expression, don't treat it as chit-chat
    if is_math_expression(cleaned):
        return None

    if FAREWELL_REGEX.match(cleaned):
        return "farewell"
    if GRATITUDE_REGEX.match(cleaned):
        return "gratitude"
    if IDENTITY_REGEX.match(cleaned):
        return "identity"
    if GREETING_REGEX.match(cleaned):
        return "greeting"
    if ACKNOWLEDGMENT_REGEX.match(cleaned):
        return "acknowledgment"
    return None

def get_conversational_response(intent: str) -> str:
    """Returns friendly, educational persona responses for student conversational intents."""
    if intent == "farewell":
        return (
            "### 👋 Goodbye & Happy Learning! 🎓\n\n"
            "Alvida! All the best with your studies. 📚✨\n\n"
            "- **Revise Regularly:** Don't forget to review the concepts we discussed today.\n"
            "- **Practice Problems:** Try solving a few practice questions or take a quick quiz when you return.\n"
            "- **Always Here:** Jab bhi koi study doubt ho ya revision karna ho, feel free to ask anytime.\n\n"
            "Take care and keep shining in your academics! 🌟"
        )
    elif intent == "gratitude":
        return (
            "### 🌟 You're Very Welcome! 🎓\n\n"
            "Mujhe khushi hui ki main aapki padhai me help kar saka! 💡\n\n"
            "- Feel free to ask if you need more examples, code snippets, or deeper explanations.\n"
            "- Aap chahein toh hum is topic ka ek quick **Practice Quiz** bhi solve kar sakte hain.\n\n"
            "Keep studying and keep asking questions! 📚✨"
        )
    elif intent == "greeting":
        return (
            "### 👋 Hello! Welcome to StudySync Pro 🎓\n\n"
            "Main aapka **Personal AI Study Assistant** hoon. Aaj hum kaunsa subject ya concept padhenge? 📚\n\n"
            "Aap mujhse poochh sakte hain:\n"
            "- 💻 **Computer Science & Coding:** Python, Data Structures, OOPs, Web Dev, Algorithms\n"
            "- 🧮 **Mathematics & Logic:** Algebra, Calculus, Trigonometry, Step-by-step solutions\n"
            "- 🔬 **Science:** Physics laws, Chemistry reactions, Biology mechanisms\n"
            "- 📝 **Exam Prep:** Revision notes, Flashcards, ya 5-25 questions ka Practice Quiz\n\n"
            "Bataiye, kis topic se shuru karein? 🚀"
        )
    elif intent == "acknowledgment":
        return (
            "### 👍 Bahut Badhiya! 🚀\n\n"
            "Glad that made sense!\n\n"
            "- Agla topic ya step explore karein?\n"
            "- Ya is concept pe practice questions / quiz solve karna chahenge?\n\n"
            "Bataiye next kya padhna hai! 📚✨"
        )
    elif intent == "identity":
        return (
            "### 🎓 StudySync Pro - Personal AI Study Assistant\n\n"
            "Main hoon aapka dedicated **AI Study Assistant**! 🌟\n\n"
            "Mera maksad hai aapki padhai ko aasan, fast aur interactive banana:\n"
            "- 💡 **Concept Explanations:** Deep dives in Computer Science, Math, Science & Engineering.\n"
            "- 🧮 **Instant Math Solver:** Step-by-step equation and calculation solving.\n"
            "- 📝 **Dynamic Quizzes:** 5 to 25 interactive questions with instant scoring & feedback.\n"
            "- 🗂️ **Smart Flashcards & Notes:** Summarize PDFs/notes and generate quick revision cards.\n"
            "- 🎯 **Multi-Turn Context:** Follow-up questions, code walkthroughs, and error debugging.\n\n"
            "Aap mujhse apni padhai se juda koi bhi sawaal poochh sakte hain! 📚✨"
        )
    return "How can I help you with your studies today? 📚"
