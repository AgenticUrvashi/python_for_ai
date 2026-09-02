from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
import json
import re

def log_tool(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Tool is running...")
        result = func(*args,**kwargs)
        print("Tool finished")
        return result

    return wrapper

class Tool(ABC):

    def __init__(self,name,description):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self,*args):
        pass

    def needs_command(self):
        return True

class CalculatorTool(Tool):

    def __init__(self):
        super().__init__("Calculator","Performs basic calculations")
        self.allowed_operators = ["+","-","*","/"]

    @log_tool
    def run(self,expression):
        while True:
            try:
                pattern = r"^-?\d+(\.\d+)?\s*[+\-*/]\s*-?\d+(\.\d+)?$"

                if not re.match(pattern,expression):
                    return "Invalid expression"

                result = eval(expression)
                return result


            except SyntaxError:
                print("Invalid calculation")

            except ZeroDivisionError:
                print("division by zero is not possible")

            choice = input("Try again yes/no: ")

            if choice == "yes":
                expression = input("Enter new expression: ")

            elif choice == "no":
                print("Calculation cancelled")
                break

            else:
                print("Invalid input")

class NoteTool(Tool):
    
    def __init__(self):
        super().__init__("Notes","Add notes and show")

    def add(self,note):
        try:
            with open("notes.json", "r") as f:
                notes = json.load(f)

            notes.append(note)

            with open('notes.json','w') as f:
                json.dump(notes, f)

        except FileNotFoundError:
            print("Notes file not found")

        except json.JSONDecodeError:
            print("Json file is empty or invalid data")

    def show(self):
        try:
            with open("notes.json", "r") as f:
                notes = json.load(f)
                
                for index, note in enumerate(notes, start = 1):
                    print(index, note)
                    
        except FileNotFoundError:
            print("Notes file not found")

        except json.JSONDecodeError:
            print("Json file is empty or invalid data")


    @log_tool
    def run(self,command):
        command = command.strip().lower()

        if command == "add":
            note = input("Enter your note: ")
            self.add(note)

        elif command == "show":
            self.show()

        else:
            print("Invalid choice")

class ToolManager:
    def __init__(self) -> None:
        self.tools = []

    def add_tool(self,tool):
        self.tools.append(tool)

    def show_tools(self):
        for tool in self.get_tools():
            print(tool.name, "-", tool.description)

    def get_tool(self,name):
        name = name.strip().lower()
        for tool in self.tools:
            if name == tool.name.lower():
                return tool

        return None

    def get_tools(self):
        for tool in self.tools:
            yield tool

class Assistant:

    def __init__(self,manager) -> None:
        self.manager = manager

    @log_tool
    def run(self): 
        while True:
            name = input("enter tool name : ")

            if name == "exit":
                print("Goodbye!")
                break

            tool = self.manager.get_tool(name)

            if tool is None:
                print("Tool not found...!")
                continue

            if tool.needs_command():
        
                command = input("enter command: ")

                result = tool.run(command)

            else:
                result = tool.run()

            if result is not None:
                print(result)


class TimeTool(Tool):
    
    def __init__(self):
        super().__init__("Time","Show current time")

    def needs_command(self):
        return False

    @log_tool
    def run(self):
        return datetime.now().strftime("%H:%M:%S")

class DateTool(Tool):

    def __init__(self):
        super().__init__("Date","Show current date")

    def needs_command(self):
        return False

    @log_tool
    def run(self):
        return datetime.now().strftime("%d-%m-%Y")


manager = ToolManager()

manager.add_tool(CalculatorTool())
manager.add_tool(NoteTool())
manager.add_tool(TimeTool())
manager.add_tool(DateTool())

assistant = Assistant(manager)
assistant.run()