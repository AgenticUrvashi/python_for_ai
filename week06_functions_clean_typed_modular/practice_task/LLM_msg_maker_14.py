'''EN: Write make_message(text, role="user") that returns a dict {"role": role, "content": text}. 
Make a normal user message and a role="system" message. (This is exactly how AI chat messages look!)
हिंदी: make_message(text, role="user") बनाओ जो dict {"role": role, "content": text} return करे। 
एक normal user message और एक role="system" message बनाओ। (AI chat messages बिल्कुल ऐसे ही दिखते हैं!)
Concepts: default value, returning a dict, agentic link
Hint: return {"role": role, "content": text}.'''

# restate:ek function banao jo AI chat jaisa dikhe.

# example:print(make_message("hello Mr. chohan!!","system")) >>>> role:system ; content:hello Mr. chohan!!

# pseudocode:
            # 1.create function make_message(text, role="user")
            # 2.return {"role": role, "content": text}
            # 3.print function with one or two parameter.

# translate:
def make_message(text, role="user"):
    return {"role": role, "content": text}

print("------------------chatgpt------------------")
print(make_message("hello Mr. chohan!!","system"))
print("------------------- we --------------------")
print(make_message("Hi!!"))
print("-------------------------------------------")

# dry run:
# -----------------chatgpt------------------
# {'role': 'system', 'content': 'hello Mr. chohan!!'}
# ------------------- we --------------------       
# {'role': 'user', 'content': 'Hi!!'}
# -------------------------------------------