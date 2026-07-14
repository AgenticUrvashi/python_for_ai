print("="*100)


sentence = input("enter your dirty sentence: ")

raw_data = sentence.split(" ")

word = []
for text in raw_data:
    if text :
        word.append(text)


clean_data = " ".join(word)
print("dirty data :" ,sentence)
print("clean data: " ,clean_data)

print("="*100)