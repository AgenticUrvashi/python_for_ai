'math module use karke ek circle_area(radius) function tools.py mein add karo.'

# restate: hame tools me function banana hai jo circle ka area de.

# example: circle_area(7) then the output is 153.94.

# pseudocode:
            # 1.starts with importing math.
            # 2.make function circle_area(radius).
            # 3.type docstring .
            # 4.return math.pi * radius ** 2

# translate:
# in tools

import math 

def circle_area(radius: float) -> float:

    """Return the area of a circle given its radius."""

    return math.pi * radius ** 2

print(round(circle_area(7), 2))  

# dry run:
153.94