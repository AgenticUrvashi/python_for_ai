'Restate: Ek TypedDict User banao (name: str, age: int).'

# example:"name": "Urvashi", "age": 17

# pseudocode:
            # 1.from typing import Typeddict
            # 2.create class Person(TypedDict): name: str , age: int
            # 3.p: Person = {"name": "Urvashi", "age": 17}
            # 4.print(p)

# translate:
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

p : Person = {"name": "Urvashi", "age": 17}

print(p)

# dry run:
# {"name": "Urvashi", "age": 17}