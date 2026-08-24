'retry mein ek case add karo jahan saare attempts fail hon — aakhri error dekho.'

# src source code    bond paper


# restate: jo code week 09 ke file me hai uske retry me add karo isa function jo har bar fail ho aur last me error de.
# example:

# pseudocode:
            # 1.copy from Week09 (retry)
            # 2.create another function func() then raise ValueError("nothing")
            # 3.try: retry(func,max_attempts=3, delay = 1.0)
            # 4.except ValueError as e then print(f"Error:{e}")

import time

def retry(func, max_attempts: int = 3, delay: float = 1.0):
    """Run func, retrying on failure with a wait between attempts.

    Args:
        func: A no-argument function to call.
        max_attempts: How many times to try before giving up.
        delay: Base seconds to wait between attempts.

    Returns:
        Whatever func returns on success.

    Raises:
        The last exception if all attempts fail.
    """
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            return func()                       # koshish
        except Exception as e:                  # koi bhi failure
            last_error = e
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                wait = delay * (2 ** (attempt - 1))    # backoff
                print(f"Retrying in {wait}s...")
                time.sleep(wait)
    raise last_error


def func():
    raise ValueError("Nothing")

try:
    retry(func, max_attempts = 3, delay= 1.0)
except ValueError as e:
    print(f"Error: {e}")

# dry run:
# Attempt 1 failed: Nothing
# Retrying in 1.0s...
# Attempt 2 failed: Nothing
# Retrying in 2.0s...
# Attempt 3 failed: Nothing
# Error: Nothing