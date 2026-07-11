
print("================= Simple Calculator =================")

first_num = float(input("First number: "))

sencond_num = float(input("Second number: "))

op = input("Operation (+ - * /): ")

match op:

    case "+":

        print(f"Result: {first_num+ sencond_num}")

    case "-":

        print(f"Result: {first_num - sencond_num}")

    case "*":

        print(f"Result: {first_num * sencond_num}")

    case "/":

        if sencond_num == 0:

            print("Cannot divide by zero!")

        else:

            print(f"Result: {first_num / sencond_num}")

    case _:

        print("Unknown operation")

print("="*50)