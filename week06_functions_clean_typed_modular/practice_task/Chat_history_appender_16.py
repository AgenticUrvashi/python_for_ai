'''EN: Write add_message(text, history=None) that appends {"role": "user", "content": text} to the history and returns it.
 Start two SEPARATE conversations and prove their histories do not mix.
हिंदी: add_message(text, history=None) बनाओ जो {"role": "user", "content": text} को history में जोड़ कर उसे return करे।
 दो अलग बातचीत शुरू करके साबित करो कि उनकी history आपस में नहीं मिलती।
Concepts: None default, list of dicts, .append()
Hint: if history is None: history = [] — otherwise both chats share one list (a privacy bug!).
'''

# restate:ek function banao jo chat histroy alag alag list me represent kare mix na kare.

# example:chat1=role:user, content:hi,how are you?   chat2=role:user, content:hello, I am fine.

# pseudocode:
            # 1.create function add_message(text, history=None).
            # 2.if history is None then history = [].
            # 3.add chat with the help of append as dict({"role":"user", "content":text}).
            # 4.returns history.
            # 5.create new lists chat1 and chat2
            # 6.call the functions and after comma write "chat1"/"chat2"

# translate:
def add_message(text, history=None):
    if history is None:                      ### history = [] — otherwise both chats share one list (a privacy bug!)
        history = []
    history.append({"role":"user", "content":text})
    return history

chat1 = []
add_message("Hi,how are you?", chat1)
add_message("I am also fine, Thank You!", chat1)

chat2 = []
add_message("Hello,I am fine! how about you?", chat2)
add_message("very nice.",chat2)

print("=============================================chat history=====================================================")
print(chat1)
print("--------------------------------------------------------------------------------------------------------------")
print(chat2)
print("--------------------------------------------------------------------------------------------------------------")

# dry run:

# =============================================chat history=====================================================
# [{'role': 'user', 'content': 'Hi,how are you?'}, {'role': 'user', 'content': 'I am also fine, Thank You!'}]   
# --------------------------------------------------------------------------------------------------------------
# [{'role': 'user', 'content': 'Hello,I am fine! how about you?'}, {'role': 'user', 'content': 'very nice.'}]   
# --------------------------------------------------------------------------------------------------------------