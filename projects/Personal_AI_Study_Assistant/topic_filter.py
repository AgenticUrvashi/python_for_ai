"""
Topic Filter for Personal AI Study Assistant (StudySync Pro)
Enforces strict study-only rule:
- Returns True ONLY if the question is academic, study, homework, or educational.
- Returns False if the question is chit-chat, entertainment, sports, politics, gossip, or non-educational.
"""

import re

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