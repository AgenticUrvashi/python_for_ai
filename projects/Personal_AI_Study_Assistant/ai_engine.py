"""
AI Engine for StudySync Pro - Personal AI Study Assistant.
Powered by Groq High-Performance Inference (Qwen 3.8 27B / Llama 3.3 70B / Llama 3.1 8B).

Features:
1. Strict study-only enforcement with polite Hinglish refusal for non-study queries.
2. High-speed Groq API integration (OpenAI-compatible REST endpoint via urllib).
3. Multi-persona study modes: Concept Explainer, Code & Debug Tutor, Exam Notes, Math Solver.
4. Multi-turn conversation context history support.
5. Dynamic AI Quiz Generator on ANY topic or difficulty.
6. Deep AI Document & Study Notes Analysis with Flashcard extraction.
7. Safe arithmetic & algebraic evaluator.
8. Comprehensive offline academic fallback knowledge engine.
"""

import ast
import json
import math
import operator
import re
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

import config
from topic_filter import is_math_expression, is_study_related

# Safe arithmetic operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

SORRY_MESSAGE = (
    "Sorry! Main sirf study-related aur educational questions ke jawab de sakta hoon. "
    "Kripya apne subject, notes ya concept se juda koi sawaal poochhein. 📚\n\n"
    "*(Aap poochh sakte hain: Python programming, Math formulas & derivations, Science concepts, "
    "Data Structures, Homework solutions, ya Practice Quizzes)*"
)

# Built-in knowledge base for high quality study responses when offline or without API key
KNOWLEDGE_BASE = {
    "binary search": (
        "### 🔍 Binary Search Algorithm\n\n"
        "**Definition:** Binary Search is an efficient divide-and-conquer algorithm for finding a target element in a **sorted** array.\n\n"
        "**Time Complexity:**\n"
        "- **Best Case:** `O(1)` (Found at midpoint on first check)\n"
        "- **Average / Worst Case:** `O(log n)` (Search space halved each step)\n"
        "- **Space Complexity:** `O(1)` (Iterative implementation)\n\n"
        "**Python Implementation:**\n"
        "```python\n"
        "def binary_search(arr, target):\n"
        "    low = 0\n"
        "    high = len(arr) - 1\n"
        "    while low <= high:\n"
        "        mid = (low + high) // 2\n"
        "        if arr[mid] == target:\n"
        "            return mid  # Found at index mid\n"
        "        elif arr[mid] < target:\n"
        "            low = mid + 1  # Target is in the right half\n"
        "        else:\n"
        "            high = mid - 1 # Target is in the left half\n"
        "    return -1  # Target not found\n"
        "```\n\n"
        "**Key Rule:** The list must be strictly sorted before applying binary search!"
    ),
    "data structure": (
        "### 📚 Data Structures Overview\n\n"
        "A **Data Structure** is a specialized format for organizing, processing, retrieving, and storing data efficiently.\n\n"
        "1. **Linear Data Structures:**\n"
        "   - **Array:** Continuous memory blocks, `O(1)` random access via index.\n"
        "   - **Linked List:** Nodes linked by pointers, dynamic size, `O(1)` insertion at head.\n"
        "   - **Stack:** LIFO (Last In First Out) principle (`push`, `pop`).\n"
        "   - **Queue:** FIFO (First In First Out) principle (`enqueue`, `dequeue`).\n\n"
        "2. **Non-Linear Data Structures:**\n"
        "   - **Trees (e.g. BST, AVL, Heap):** Hierarchical structure with root and child nodes.\n"
        "   - **Graphs:** Collection of vertices (nodes) and edges (connections).\n"
        "   - **Hash Tables:** Key-value pairs with `O(1)` average lookup and insertion."
    ),
    "python": (
        "### 🐍 Python Programming Essentials\n\n"
        "Python is a high-level, interpreted, dynamically-typed language known for clean syntax, high productivity, and rich AI/ML ecosystem.\n\n"
        "**Core Language Highlights:**\n"
        "- **Simple Syntax:** Uses indentation instead of curly brackets `{}`.\n"
        "- **Built-in Data Structures:** `list` (mutable), `tuple` (immutable), `dict` (hash map), `set` (unique elements).\n"
        "- **OOP Support:** Classes, objects, inheritance, polymorphism, encapsulation, dunder methods (`__init__`, `__repr__`).\n"
        "- **Generators & Iterators:** Memory efficient iteration using the `yield` keyword.\n"
        "- **Key Applications:** Artificial Intelligence, Data Science, Web Apps (FastAPI/Flask/Django), Automation."
    ),
    "machine learning": (
        "### 🤖 Machine Learning Fundamentals\n\n"
        "**Machine Learning (ML)** is a subset of AI enabling algorithms to learn patterns directly from data to make predictions or decisions without explicit programming.\n\n"
        "**Three Main Paradigms:**\n"
        "1. **Supervised Learning:** Training on labeled data (e.g., Linear Regression, Random Forest, Neural Networks).\n"
        "2. **Unsupervised Learning:** Discovering hidden clusters or representations in unlabeled data (e.g., K-Means, PCA).\n"
        "3. **Reinforcement Learning:** Agents learning optimal policies through state, actions, rewards, and penalties (e.g., Q-Learning, PPO).\n\n"
        "**Standard Workflow:** Data Ingestion ➔ Exploratory Analysis & Cleaning ➔ Feature Engineering ➔ Model Training ➔ Validation ➔ Production Deployment."
    ),
    "photosynthesis": (
        "### 🌿 Photosynthesis in Biology\n\n"
        "**Definition:** The biochemical process by which green plants, algae, and cyanobacteria convert solar light energy into chemical energy (glucose).\n\n"
        "**Balanced Chemical Equation:**\n"
        "$$\\text{6CO}_2 + \\text{6H}_2\\text{O} + \\text{Light Energy} \\rightarrow \\text{C}_6\\text{H}_{12}\\text{O}_6 + \\text{6O}_2$$\n\n"
        "**Two Critical Stages:**\n"
        "1. **Light-Dependent Reactions:** Occurs across thylakoid membranes in chloroplasts; splits water, produces ATP & NADPH, releases Oxygen ($O_2$).\n"
        "2. **Light-Independent Reactions (Calvin Cycle):** Occurs in the stroma; fixes Carbon Dioxide ($CO_2$) into high-energy sugars."
    ),
    "newton": (
        "### 🍎 Newton's Three Laws of Motion\n\n"
        "1. **First Law (Law of Inertia):** An object at rest stays at rest, and an object in uniform motion continues at constant velocity unless acted upon by a net external force.\n"
        "2. **Second Law ($F = ma$):** The rate of change of momentum is proportional to the applied force. In constant mass systems: $\\vec{F} = m \\cdot \\vec{a}$.\n"
        "3. **Third Law (Action & Reaction):** For every action, there is an equal and opposite reaction ($F_{A \\rightarrow B} = -F_{B \\rightarrow A}$)."
    ),
    "recursion": (
        "### 🔄 Recursion in Programming\n\n"
        "**Definition:** A programming technique where a function solves a problem by calling smaller instances of itself.\n\n"
        "**Two Essential Components:**\n"
        "1. **Base Case:** Termination condition that returns directly without further recursion (prevents `RecursionError: maximum recursion depth exceeded`).\n"
        "2. **Recursive Case:** Step that reduces the problem size towards the base case and calls the function.\n\n"
        "**Example: Factorial Calculation**\n"
        "```python\n"
        "def factorial(n: int) -> int:\n"
        "    if n <= 1:  # Base case\n"
        "        return 1\n"
        "    return n * factorial(n - 1)  # Recursive case\n"
        "```"
    ),
    "ohm": (
        "### ⚡ Ohm's Law (Physics)\n\n"
        "**Fundamental Formula:** $V = I \\times R$\n\n"
        "- **$V$**: Voltage / Potential Difference in Volts (V)\n"
        "- **$I$**: Current in Amperes (A)\n"
        "- **$R$**: Resistance in Ohms ($\\Omega$)\n\n"
        "**Principle:** In an electrical circuit at constant temperature, the current passing through a metallic conductor is directly proportional to the potential difference across its terminals."
    )
}

def safe_eval_math(expression: str) -> Tuple[bool, Any]:
    """Safely calculate basic arithmetic expressions using AST without eval risks."""
    clean_expr = re.sub(r"[^0-9+\-*/().^% ]", "", expression.replace("^", "**"))
    if not clean_expr.strip():
        return False, None

    def solve(node):
        if isinstance(node, ast.Expression):
            return solve(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](solve(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = solve(node.left)
            right = solve(node.right)
            return OPERATORS[type(node.op)](left, right)
        raise ValueError("Unsupported node")

    try:
        tree = ast.parse(clean_expr, mode="eval")
        result = solve(tree)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        elif isinstance(result, float):
            result = round(result, 6)
        return True, result
    except Exception:
        return False, None

def call_groq_api(
    messages: List[Dict[str, str]],
    model: str = "",
    api_key: str = "",
    temperature: float = 0.3,
    max_tokens: int = 1500
) -> Tuple[bool, str]:
    """
    Calls Groq Cloud API using standard urllib.
    Returns (success: bool, response_or_error: str).
    """
    key_to_use = (api_key or config.GROQ_API_KEY).strip()
    if not key_to_use:
        return False, "Groq API Key is not configured."

    model_to_use = (model or config.GROQ_DEFAULT_MODEL).strip()
    if model_to_use.startswith("groq:"):
        model_to_use = model_to_use[len("groq:"):]

    payload = {
        "model": model_to_use,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    req = urllib.request.Request(
        config.GROQ_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key_to_use}",
            "Content-Type": "application/json",
            "User-Agent": "StudySyncPro/3.0 (Personal AI Study Assistant)"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            data = json.loads(response.read().decode("utf-8"))
            choices = data.get("choices", [])
            if choices:
                content = choices[0].get("message", {}).get("content", "")
                return True, content
            return False, "Empty response from Groq."
    except urllib.error.HTTPError as e:
        try:
            err_data = json.loads(e.read().decode("utf-8"))
            err_msg = err_data.get("error", {}).get("message", str(e))
        except Exception:
            err_msg = f"HTTP Error {e.code}: {e.reason}"
        return False, f"Groq API Error: {err_msg}"
    except Exception as e:
        return False, f"Groq Connection Error: {str(e)}"

def call_gemini_api(question: str, api_key: str) -> str:
    """Call Google Gemini REST API directly using standard urllib as fallback."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{config.GEMINI_DEFAULT_MODEL}:generateContent?key={api_key}"
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"System Rule: {config.STUDY_ONLY_SYSTEM_PROMPT}\n\nStudent Question: {question}"
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 1000,
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
            candidate = data.get("candidates", [{}])[0]
            parts = candidate.get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "")
            return "No response received from Gemini."
    except Exception as e:
        return f"Gemini API Error: {str(e)}"

def get_ai_response(
    question: str,
    custom_api_key: str = "",
    model: str = "",
    mode: str = "explainer",
    conversation_history: Optional[List[Dict[str, str]]] = None,
    return_details: bool = False
) -> Any:
    """
    Main entry point for answering academic questions:
    1. Check study guardrail. If not study-related, return polite refusal.
    2. Try math evaluation if applicable.
    3. Construct persona-tailored prompt.
    4. Call Groq high-speed model with conversation context.
    5. Fallback to Gemini or comprehensive offline knowledge base.
    """
    question = question.strip()
    if not question:
        msg = "Please ask a study-related question. 📚"
        if return_details:
            return {
                "answer": msg,
                "is_study_related": True,
                "model_used": "system",
                "mode": mode
            }
        return msg

    # STRICT STUDY FILTER ENFORCEMENT
    if not is_study_related(question):
        if return_details:
            return {
                "answer": SORRY_MESSAGE,
                "is_study_related": False,
                "model_used": "guardrail",
                "mode": mode
            }
        return SORRY_MESSAGE

    # Check for direct arithmetic or simple math calculation
    if is_math_expression(question):
        math_part = re.sub(r"(what is|solve|calculate|calculate:|find|=|answer)", "", question, flags=re.IGNORECASE).strip()
        success, val = safe_eval_math(math_part)
        if success:
            math_ans = (
                f"### 🧮 Instant Math Solution\n\n"
                f"**Expression:** `{math_part}`\n\n"
                f"**Result:** **`{val}`**\n\n"
                f"*Step-by-step verification: The expression evaluates to `{val}` without error.*"
            )
            if return_details:
                return {
                    "answer": math_ans,
                    "is_study_related": True,
                    "model_used": "fast-math-engine",
                    "mode": mode
                }
            return math_ans

    # Build system instructions based on Study Mode
    persona_info = config.STUDY_MODES.get(mode, config.STUDY_MODES["explainer"])
    mode_instruction = persona_info["instruction"]
    full_system_prompt = (
        f"{config.STUDY_ONLY_SYSTEM_PROMPT}\n\n"
        f"Active Study Persona ({persona_info['title']}):\n{mode_instruction}\n\n"
        f"Instructions:\n"
        f"- Always answer in structured, readable GitHub-flavored Markdown.\n"
        f"- Use bold headings, bullet points, and code fences with language names (e.g., ```python).\n"
        f"- For formulas, format clearly using standard math notations.\n"
        f"- If the student is asking in Hinglish/Hindi, explain clearly in bilingual Hindi+English for effortless understanding."
    )

    # Prepare message list for Groq
    messages: List[Dict[str, str]] = [{"role": "system", "content": full_system_prompt}]

    # Include recent conversation context (up to 6 turns)
    if conversation_history:
        for turn in conversation_history[-6:]:
            role = turn.get("role")
            content = turn.get("content", "")
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": question})

    # 1. Try Groq API
    groq_key = custom_api_key or config.GROQ_API_KEY
    chosen_model = model or config.GROQ_DEFAULT_MODEL
    if chosen_model.startswith("groq:"):
        chosen_model = chosen_model[len("groq:"):]

    if groq_key:
        success, res = call_groq_api(
            messages=messages,
            model=chosen_model,
            api_key=groq_key,
            temperature=0.35,
            max_tokens=1800
        )
        if success and res:
            if return_details:
                return {
                    "answer": res,
                    "is_study_related": True,
                    "model_used": chosen_model,
                    "mode": mode
                }
            return res

    # 2. Try Gemini API as secondary fallback
    if config.GEMINI_API_KEY:
        gemini_res = call_gemini_api(question, config.GEMINI_API_KEY)
        if gemini_res and not gemini_res.startswith("Gemini API Error"):
            if return_details:
                return {
                    "answer": gemini_res,
                    "is_study_related": True,
                    "model_used": "Gemini 1.5 Flash",
                    "mode": mode
                }
            return gemini_res

    # 3. Offline Academic Knowledge Base Fallback
    q_lower = question.lower()
    for key, answer in KNOWLEDGE_BASE.items():
        if key in q_lower:
            if return_details:
                return {
                    "answer": answer,
                    "is_study_related": True,
                    "model_used": "offline-knowledge-base",
                    "mode": mode
                }
            return answer

    # 4. Structured Educational Concept Template
    fallback_text = (
        f"### 🎓 Study Concept: {question.title()}\n\n"
        f"Here is an educational overview for **'{question}'**:\n\n"
        f"1. **Core Concept:** To master this academic topic, break it down into core definitions, fundamental laws, and standard applications.\n"
        f"2. **Problem Solving Strategy:** Identify given inputs, known formulas, and isolate the target variable or algorithmic objective.\n"
        f"3. **Practical Practice:** Solve 2-3 standard textbook questions or implement a quick code snippet to reinforce understanding.\n\n"
        f"*(⚡ Pro Tip: Configure your Groq API Key in **Settings** to activate real-time Qwen/Llama AI responses at lightning speed!)*"
    )
    if return_details:
        return {
            "answer": fallback_text,
            "is_study_related": True,
            "model_used": "offline-fallback",
            "mode": mode
        }
    return fallback_text

def generate_study_quiz(
    topic: str = "Machine Learning",
    difficulty: str = "Intermediate",
    count: int = 4,
    custom_api_key: str = "",
    model: str = ""
) -> List[Dict[str, Any]]:
    """
    Generate dynamic interactive multiple choice questions for study revision using Groq.
    Outputs strict JSON array of quiz objects.
    """
    groq_key = custom_api_key or config.GROQ_API_KEY
    chosen_model = model or config.GROQ_DEFAULT_MODEL
    if chosen_model.startswith("groq:"):
        chosen_model = chosen_model[len("groq:"):]

    if groq_key:
        prompt = (
            f"You are a strict academic quiz creator for students. "
            f"Generate exactly {count} multiple-choice questions (MCQs) on the topic: '{topic}'. "
            f"Difficulty Level: {difficulty}.\n\n"
            f"Requirements:\n"
            f"1. Each question must have exactly 4 options.\n"
            f"2. Exactly one option must be correct.\n"
            f"3. 'answer' must be an integer index (0, 1, 2, or 3) corresponding to the correct option in 'options'.\n"
            f"4. Provide a clear educational 'explanation' for why that answer is correct.\n"
            f"5. Return ONLY a valid JSON array, with no other conversational markdown text.\n\n"
            f"Expected JSON schema:\n"
            f"[\n"
            f"  {{\n"
            f"    \"question\": \"Question text here?\",\n"
            f"    \"options\": [\"Option A\", \"Option B\", \"Option C\", \"Option D\"],\n"
            f"    \"answer\": 0,\n"
            f"    \"explanation\": \"Detailed explanation here.\"\n"
            f"  }}\n"
            f"]"
        )
        messages = [
            {"role": "system", "content": "You are a specialized JSON quiz generation engine. Output only valid JSON."},
            {"role": "user", "content": prompt}
        ]

        success, content = call_groq_api(
            messages=messages,
            model=chosen_model,
            api_key=groq_key,
            temperature=0.2,
            max_tokens=1600
        )

        if success and content:
            # Extract JSON array from LLM output
            try:
                # Find start and end bracket
                start = content.find("[")
                end = content.rfind("]")
                if start != -1 and end != -1:
                    json_str = content[start:end+1]
                    quiz_data = json.loads(json_str)
                    if isinstance(quiz_data, list) and len(quiz_data) > 0:
                        # Validate structure
                        valid_questions = []
                        for q in quiz_data:
                            if "question" in q and "options" in q and "answer" in q:
                                valid_questions.append({
                                    "question": str(q["question"]),
                                    "options": [str(opt) for opt in q["options"][:4]],
                                    "answer": int(q["answer"]) if 0 <= int(q.get("answer", 0)) < len(q["options"]) else 0,
                                    "explanation": str(q.get("explanation", "Correct academic answer."))
                                })
                        if valid_questions:
                            return valid_questions
            except Exception:
                pass

    # Built-in offline fallback quizzes
    quizzes = {
        "machine learning": [
            {
                "question": "Which of the following is an example of a Supervised Learning task?",
                "options": ["K-Means Clustering", "Spam Email Classification", "Dimensionality Reduction via PCA", "Apriori Association Mining"],
                "answer": 1,
                "explanation": "Spam email classification is supervised because the model trains on historical emails labeled as 'spam' or 'not spam'."
            },
            {
                "question": "What does 'Overfitting' in Machine Learning mean?",
                "options": [
                    "Model performs well on training data but generalizes poorly to unseen test data",
                    "Model performs poorly on both training and test data",
                    "Model converges too fast during gradient descent",
                    "Model uses insufficient feature dimensions"
                ],
                "answer": 0,
                "explanation": "Overfitting occurs when a model memorizes noise and sample-specific idiosyncrasies of the training set rather than learning true generalizable relationships."
            },
            {
                "question": "Which activation function is widely favored in hidden layers of deep neural networks to mitigate vanishing gradients?",
                "options": ["Sigmoid", "ReLU (Rectified Linear Unit)", "Linear", "Softmax"],
                "answer": 1,
                "explanation": "ReLU ($f(x) = \\max(0, x)$) maintains a constant gradient of 1 for positive activations, effectively mitigating the vanishing gradient problem."
            },
            {
                "question": "What is the primary role of a Validation dataset during model training?",
                "options": ["Final benchmark testing", "Hyperparameter tuning and early stopping", "Initial weight calculation", "Feature normalization"],
                "answer": 1,
                "explanation": "The validation set is used during training to tune hyperparameters (like learning rate) and detect overfitting before final testing."
            }
        ],
        "data structures": [
            {
                "question": "What is the average time complexity of searching an element in a Balanced Binary Search Tree (BST)?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
                "answer": 2,
                "explanation": "In a balanced BST (like AVL or Red-Black), each comparison halves the remaining search space, resulting in O(log n) time."
            },
            {
                "question": "Which data structure operates strictly on the LIFO (Last In First Out) principle?",
                "options": ["Queue", "Stack", "Linked List", "Priority Queue"],
                "answer": 1,
                "explanation": "A Stack works on LIFO where the most recently pushed element is the first one removed with pop()."
            },
            {
                "question": "What is the worst-case time complexity of QuickSort?",
                "options": ["O(n log n)", "O(n)", "O(n²)", "O(log n)"],
                "answer": 2,
                "explanation": "When an unbalanced pivot (such as the smallest or largest item) is chosen repeatedly on a sorted array, QuickSort degrades to O(n²)."
            },
            {
                "question": "Which data structure is fundamentally used for Breadth-First Search (BFS) in a Graph?",
                "options": ["Stack", "Queue", "Binary Tree", "Heap"],
                "answer": 1,
                "explanation": "BFS explores vertices level by level, requiring a FIFO Queue to process vertices in the exact order they were discovered."
            }
        ],
        "python": [
            {
                "question": "Which of the following data types in Python is IMMUTABLE?",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "answer": 2,
                "explanation": "Tuples, strings, and integers are immutable in Python; their contents cannot be altered after creation."
            },
            {
                "question": "What does `bool([])` evaluate to in Python?",
                "options": ["True", "False", "None", "Raises an Exception"],
                "answer": 1,
                "explanation": "Empty containers (empty lists, tuples, dicts, strings) have falsy truth values in Python, evaluating to False."
            },
            {
                "question": "How do you define a memory-efficient generator function in Python?",
                "options": ["Using the `return` statement", "Using the `yield` statement", "Using `async def`", "Using lambda expressions"],
                "answer": 1,
                "explanation": "The `yield` statement pauses function execution and emits a value, turning the function into an iterator/generator that produces items on demand."
            },
            {
                "question": "What is the output of `type(lambda x: x)` in Python?",
                "options": ["<class 'function'>", "<class 'lambda'>", "<class 'method'>", "<class 'generator'>"],
                "answer": 0,
                "explanation": "Lambdas create standard anonymous functions whose runtime type is `<class 'function'>`."
            }
        ]
    }

    t_lower = topic.lower()
    for key, q_list in quizzes.items():
        if key in t_lower:
            return q_list[:count]

    return quizzes["machine learning"][:count]

def analyze_document_content(
    filename: str,
    content: str,
    custom_api_key: str = "",
    model: str = ""
) -> Dict[str, Any]:
    """
    Analyzes student notes or uploaded documents using Groq:
    Extracts deep summary, key takeaways, flashcards, and exam questions.
    """
    word_count = len(content.split())
    groq_key = custom_api_key or config.GROQ_API_KEY
    chosen_model = model or config.GROQ_DEFAULT_MODEL
    if chosen_model.startswith("groq:"):
        chosen_model = chosen_model[len("groq:"):]

    if groq_key and content.strip():
        # Truncate content to safe token length if very large
        sample_text = content[:6000]
        prompt = (
            f"You are an academic analysis engine. Analyze the following study document '{filename}':\n\n"
            f"--- DOCUMENT CONTENT ---\n{sample_text}\n--- END DOCUMENT ---\n\n"
            f"Return a strict JSON object with these exact keys:\n"
            f"1. 'summary': A comprehensive 2-3 paragraph academic overview of the main concepts, core ideas, and significance.\n"
            f"2. 'key_takeaways': A list of 4-6 high-yield revision bullet points (formulas, definitions, key rules).\n"
            f"3. 'flashcards': A list of 3-5 flashcard objects with 'front' (question/term) and 'back' (definition/answer).\n"
            f"4. 'suggested_questions': A list of 4 high-probability exam/viva questions based on this content.\n\n"
            f"Output ONLY valid JSON."
        )

        messages = [
            {"role": "system", "content": "You are a professional educational document analyzer. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ]

        success, res = call_groq_api(
            messages=messages,
            model=chosen_model,
            api_key=groq_key,
            temperature=0.25,
            max_tokens=1800
        )

        if success and res:
            try:
                start = res.find("{")
                end = res.rfind("}")
                if start != -1 and end != -1:
                    parsed = json.loads(res[start:end+1])
                    return {
                        "filename": filename,
                        "word_count": word_count,
                        "summary": parsed.get("summary", f"Detailed analysis of {filename}."),
                        "key_takeaways": parsed.get("key_takeaways", []),
                        "flashcards": parsed.get("flashcards", []),
                        "suggested_questions": parsed.get("suggested_questions", [])
                    }
            except Exception:
                pass

    # High-quality fallback rule-based analysis
    clean_lines = [line.strip() for line in content.splitlines() if line.strip()]
    preview_points = clean_lines[:4] if clean_lines else ["Fundamental academic concepts extracted from notes."]

    return {
        "filename": filename,
        "word_count": word_count,
        "summary": (
            f"The document '{filename}' spans approximately {word_count} words covering essential study concepts. "
            f"Key focus areas encompass core theoretical definitions, analytical methodologies, and practical academic applications. "
            f"StudySync has prepared structured revision points and suggested exam questions below."
        ),
        "key_takeaways": [
            f"Core Theme: Structured learning material based on {filename}",
            "Foundational Theory: Essential definitions and standard formulas highlighted",
            "Exam Focus: High-yield concepts and revision checkpoints for retention",
            f"Key Section: {preview_points[0] if preview_points else 'Core Syllabus Chapter'}"
        ],
        "flashcards": [
            {"front": f"What is the primary topic of {filename}?", "back": "Covers core principles, formulas, and practical applications."},
            {"front": "Key Revision Checkpoint", "back": "Focus on step-by-step problem solving and standard definitions."},
            {"front": "Exam Strategy", "back": "Review derivations, boundary conditions, and real-world examples."}
        ],
        "suggested_questions": [
            f"What are the fundamental principles explained in {filename}?",
            "Can you explain the key formulas and step-by-step derivations?",
            "What are the common viva questions asked from this chapter?",
            "How do the concepts in this document apply to practical problem solving?"
        ]
    }

def generate_flashcards(
    topic: str,
    count: int = 5,
    custom_api_key: str = "",
    model: str = ""
) -> List[Dict[str, str]]:
    """Generate dynamic revision flashcards on any topic."""
    groq_key = custom_api_key or config.GROQ_API_KEY
    chosen_model = model or config.GROQ_DEFAULT_MODEL
    if chosen_model.startswith("groq:"):
        chosen_model = chosen_model[len("groq:"):]

    if groq_key:
        prompt = (
            f"Generate exactly {count} study flashcards for topic '{topic}'. "
            f"Return ONLY a JSON array with 'front' (question or concept to recall) and 'back' (clear, concise answer/explanation).\n"
            f"Schema: [ {{\"front\": \"...\", \"back\": \"...\"}} ]"
        )
        messages = [
            {"role": "system", "content": "You are a flashcard generator. Return only valid JSON."},
            {"role": "user", "content": prompt}
        ]
        success, res = call_groq_api(messages=messages, model=chosen_model, api_key=groq_key, temperature=0.3, max_tokens=1000)
        if success and res:
            try:
                start = res.find("[")
                end = res.rfind("]")
                if start != -1 and end != -1:
                    cards = json.loads(res[start:end+1])
                    if isinstance(cards, list) and len(cards) > 0:
                        return [{"front": str(c["front"]), "back": str(c["back"])} for c in cards if "front" in c and "back" in c]
            except Exception:
                pass

    # Fallback flashcards
    return [
        {"front": f"What is {topic}?", "back": f"{topic} is an essential academic subject focused on foundational principles and systematic methods."},
        {"front": f"Why is {topic} important in exams?", "back": "It tests analytical thinking, formula retention, and practical application skills."},
        {"front": f"How to master {topic}?", "back": "Break complex problems into smaller sub-problems, solve daily practice problems, and revise flashcards regularly."}
    ]

def test_groq_connection(api_key: str = "", model: str = "") -> Dict[str, Any]:
    """Test Groq API connection and latency."""
    key = (api_key or config.GROQ_API_KEY).strip()
    target_model = (model or config.GROQ_DEFAULT_MODEL).strip()
    if target_model.startswith("groq:"):
        target_model = target_model[len("groq:"):]

    if not key:
        return {"status": "error", "message": "Groq API Key is not set in .env or settings."}

    messages = [
        {"role": "user", "content": "Respond with: 'Groq Engine Connected Successfully!' in exactly 5 words."}
    ]
    success, res = call_groq_api(messages=messages, model=target_model, api_key=key, max_tokens=30)
    if success:
        return {
            "status": "connected",
            "message": res.strip(),
            "model": target_model,
            "provider": "Groq Cloud"
        }
    return {
        "status": "error",
        "message": res,
        "model": target_model
    }
