# Task 10 — To-Do List Manager (menu loop)
# Ek khaali list todos = [] banao. Ek while True menu chalao: 1) Add  2) Remove  3) Show  4) Quit.
#  User ke choice ke hisaab se task add/remove/show karo. 4 par loop break karo.

# Concepts: while True, match/case (ya if/elif), list .append()/.remove(), break
# Hint: remove karte waqt check karo item list mein hai ya nahi (warna crash), if item in todos:.
# ans:


print("===================================To-Do List Manager (menu loop)=================================")

todos = []

while True:
    print("1. add")
    print("2.remove")
    print("3.show")
    print("4.quit")

    print("---------------------------------------------------")

    user_input = input("enter your choice: ")

    if user_input=="1":
        task = input("what is task: ")
        todos.append(task)
        
        print("--------------------------------------------------")

    elif user_input=="2":
        task = input("enter task to remove: ")
        if task in todos:
            todos.remove(task)
        else:
            print("task not found")

            print("------------------------------------------------")

    elif user_input=="3":
        print(todos)

        print("---------------------------------------------------------")

    else:
        break

print("==================================end the program====================================")