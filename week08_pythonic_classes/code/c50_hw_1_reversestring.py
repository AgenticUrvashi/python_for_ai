'que: Upar wale Agent project mein ek teesra tool add karo: ReverseTool jo string ulta kare.'

# restate:sir ne jo agent bana ke dikhaya usme hi reversetool naam ka aur ek class add karo jo string ko ulta kare

# pseudocode:
            # 1.create class ReverseTool.
            # 2.create special method __init__(self) then super().__init__("reverse","reverse the string")
            # 3.create method run(self,text) then word = "" then use for i in text: word = i + word
            # 4.return word

# translate:
from abc import ABC, abstractmethod


class Tool(ABC):
    """Base class — har tool ka naam, description aur run() hona zaroori."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, *args):
        ...

    def __repr__(self):
        return f"Tool(name='{self.name}')"


class CalculatorTool(Tool):
    def __init__(self):
        super().__init__("calculator", "Adds two numbers")

    def run(self, a: float, b: float) -> float:
        return a + b


class GreetTool(Tool):
    def __init__(self):
        super().__init__("greet", "Greets a person by name")

    def run(self, name: str) -> str:
        return f"Hello, {name}!"

'-----------------------------add kiya hua-------------------------------'

class ReverseTool(Tool):
    def __init__(self):
        super().__init__("reverse", "reverse the string")

    def run(self,text):
        word = ""
        for i in text:
            word = i + word 
        return word

'--------------------------------------------------------------------------'

class Agent:
    """An agent HAS-A list of tools (composition)."""
    def __init__(self, name: str):
        self.name = name
        self.tools = []           

    def add_tool(self, tool: Tool):
        self.tools.append(tool)

    def list_tools(self):
        print(f"{self.name}'s tools:")
        for tool in self.tools:
            print(f"  - {tool.name}: {tool.description}")

    def use_tool(self, tool_name: str, *args):
        for tool in self.tools:
            if tool.name == tool_name:   
                return tool.run(*args)
        return f"Tool '{tool_name}' not found"

