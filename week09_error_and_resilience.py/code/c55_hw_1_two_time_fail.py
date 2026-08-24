'retry function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.'

# restate: ek function banana hai jo run karo to 2 bar fail kare phir success de.

# example: amount = 788

# pseudocode:
            # 1.import random.
            # 2.create function retry(amount:float,max_attempts = 3):
            # 3.use for loop for attempt in range(1,max_attempts+1):
            # 4.try: if random.choice([False,False,True]): raise ConnectionError("Network Interrupted")
            # 5. return  f"Payment of rupees {amount:.2f} processed successfully"
            # 6.except ConnectionError: print("Network Interrupted")
            # 7.print(retry(788))

# translate:
import random


def retry(amount:float,max_attempts = 3) -> str:
    '''payment processing, 50% chance of failure'''

    for attempt in range(1, max_attempts+1):

        try:
            if random.choice([False,False,True]):
                raise ConnectionError("Network Interrupted")

            return f"Payment of rupees {amount:.2f} processed successfully"

        except ConnectionError:
            print("Network Interrupted")
                    

print(retry(788))

# dry run:
# Network Interrupted
# Network Interrupted
# Payment of rupees 788.00 processed successfully