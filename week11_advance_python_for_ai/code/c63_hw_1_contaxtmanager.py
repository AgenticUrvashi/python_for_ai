'Restate: Apna context manager @contextmanager se banao jo "Enter"/"Exit" print kare.'
# example: 

# pseudocode:
            # 1.from contextlib import contextmanager
            # 2.write @contextmanager
            # 3.create function my(): print("Enter"), yield , print("Exit")
            # 4.with my(): print("Inside the function")

# translate:
from contextlib import contextmanager

@contextmanager
def my():
    print("Enter")
    yield
    print("Exit")

with my():
    print("Inside the function")
    
# dry run:
# Enter
# Inside the function
# Exit