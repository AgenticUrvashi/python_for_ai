'''EN: Make a quiz. Store questions as a list of dicts (question, answer). 
Write ask(question, answer) that takes the user's input and returns 1 if correct else 0. 
Loop all questions, add up the score with a score accumulator, then print a final result with a pass/fail message.
हिंदी: एक quiz बनाओ। questions को dicts की list में रखो (question, answer)। 
ask(question, answer) बनाओ जो user का input लेकर सही होने पर 1 वरना 0 return करे। 
सभी questions पर loop चलाओ, score accumulator से जोड़ो, फिर pass/fail message के साथ final result print करो।
Concepts: list of dicts, function returning a number, accumulator, input()
Hint: return 1 if user.strip().lower() == answer.lower() else 0.'''

# restate : hame isa code likhana hai jo question puchhe aur ham aagr sahi ans de to hamara score badhe.
            # 2 se jyada score ho to pass.

# example:agar hamne 2 ans sahi diye hai to hamara score hoga 2 aur hum pass honge.

# pseudocode:
            # 1.create variables score=0 and system which is store que and ans in dict and no. of que and ans store in list.
            # 2.create function ask(que , ans)
            # 3.use for loop update score if ans is right. 
            # 4.print score.
            # 5.if score >= 2 then pass
            # 6.else fail.

# translate:

print("====================================== QUIZ CHALLENGE =======================================")

system = [
    {"question":"python is programming language(yes/no) : ","answer":"yes"},
    {"question":"capital of india? : ","answer":"Delhi"},
    {"question":"3 * 7 = ? : ","answer":"21"}
]

score = 0

def ask(question, answer):
    user = input(question)
    if user.strip().lower() == answer.lower():
        return 1
    else:
        return 0

for q in system:
    score = score + ask(q["question"],q["answer"])
    print("---------------------------------------")

print("======================")

print(score)

print("=======================")

if score >= 2:
    print("Pass")
else:
    print("Fail")

print("============================================= END =========================================")

# dry run:
# ====================================== QUIZ CHALLENGE =======================================
# python is programming language(yes/no) : yes
# ---------------------------------------
# capital of india? : delhi
# ---------------------------------------
# 3 * 7 = ? : 4
# ---------------------------------------
# ======================
# 2
# =======================
# Pass
# ============================================= END =========================================
