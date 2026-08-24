'Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).'

# restate: 4 attempts ke liye wait time dikhao delay = 1 lo.

# example: output aana chahiye Attempt 1 : wait 1s

# pseudocode:
            # 1.delay = 1
            # 2.for attempt in range(1,5):
            # 3.print("Attempt {attempt} : wait {(delay * (2 ** (attempt - 1)))}")

delay = 1
for attempt in range(1, 5):
    print(f"Attempt {attempt} : wait {(delay * (2 ** (attempt - 1)))}s")

# dry run:
# Attempt 1 : wait 1s
# Attempt 2 : wait 2s
# Attempt 3 : wait 4s
# Attempt 4 : wait 8s