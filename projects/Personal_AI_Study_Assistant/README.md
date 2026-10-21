# ⚡ StudySync - Personal AI Study Assistant

**StudySync** ek modern AI-powered learning platform hai jo **sirf aur sirf study-related** (academic, coding, math, science, homework) sawaalon ke jawab deta hai. Agar koi non-study sawaal poochha jaaye (jaise movies, sports score, gossip, ya casual chitchat), toh yeh turant politely mana kar deta hai:
> *"Sorry! Main sirf study-related aur educational questions ke jawab de sakta hoon. Kripya apne subject, notes ya concept se juda koi sawaal poochhein. 📚"*

---

## 🎨 Interface Features (As Designed in Image)

1. **Left Hero Promo Banner**:
   - `1 StudySync` Badge & Subtitle
   - Feature Highlights:
     - 📄 AI Document Analysis
     - ❓ Quiz Generation
     - 📝 AI Summaries
     - 📊 Learning Analytics
   - **3D Glowing Open Book & Brain Hologram** futuristic graphic.
2. **Top Navigation Bar**:
   - StudySync Logo, Global search bar, notifications popup, bookmarks, aur **Roshan** user profile badge.
3. **Sidebar**:
   - Features, Dashboard, My Library, AI Tutor, Quizzes, Analytics, Settings.
4. **Three Quick Action Cards**:
   - 📄 **Upload & Learn**: Upload any document and get AI insights & summaries.
   - 🤖 **AI Tutor**: Dedicated academic chat interface with strict study guardrail.
   - 📝 **Generate Quiz**: Interactive 3-question MCQ quiz generator with live explanations & scoring.
5. **Recent Documents**:
   - `Machine Learning Basics.pdf` (12 pages • PDF)
   - `Data Structures Notes.pdf` (8 pages • PDF)
6. **Learning Progress**:
   - **75% Overall Progress** SVG circular donut meter with glowing cyan/blue gradient.
   - **Weekly Study Activity** bar chart (Mon - Sun).

---

## 🚀 How to Run

Application ko run karne ke liye terminal mein yeh command chalayein:

```bash
uv run .\main.py
```

Command chalte hi local server start ho jayega aur aapke default browser mein StudySync ka dark-themed dashboard automatically open ho jayega:
👉 `http://127.0.0.1:5000`

---

## 🔒 Strict Study Guardrail

| Question Type | Example | Response |
| :--- | :--- | :--- |
| **Academic / Coding** | *"Explain Binary Search in Python"* | ✅ Full step-by-step algorithm, time complexity `O(log n)`, and code block |
| **Mathematics** | *"Calculate 25 * 4 + 10"* | ✅ Evaluates and returns `110` with verification |
| **Science** | *"What is Photosynthesis formula?"* | ✅ Chemical formula & explanation |
| **Non-Study / Entertainment** | *"Who is Salman Khan?"* | ❌ *"Sorry! Main sirf study-related aur educational questions ke jawab de sakta hoon..."* |
| **Sports / Gossip** | *"What is the IPL cricket match score?"* | ❌ *"Sorry! Main sirf study-related aur educational questions ke jawab de sakta hoon..."* |

---

## ⚙️ Configuration (Optional)

- Settings modal mein jaakar aap apna **Google Gemini API Key** add kar sakte hain live LLM responses ke liye.
- Agar koi API key nahi di gayi, toh assistant automatically **built-in academic knowledge engine** ka use karta hai.
