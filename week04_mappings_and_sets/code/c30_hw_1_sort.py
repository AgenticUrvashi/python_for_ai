# 3 dicts ki list banao (naam, age) aur age ke hisaab se sort karke print karo.

home = [
    {"name":"amol","age":27},
    {"name":"shanta","age":25},
    {"name":"anu","age":20}
]

home.sort(key=lambda x:x["age"])
print(home)
