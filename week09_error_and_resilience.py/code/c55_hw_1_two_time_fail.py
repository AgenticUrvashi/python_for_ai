'retry function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.'

# incomplete

import random

def retry(amount:float,max_attempts = 3) -> str:
    '''payment processing, 50% chance of failure'''

    try:
        for attempt in range(1, max_attempts+1):
            if random.choice([True,False]):
                raise ConnectionError("Network Interrupted")

            return f"Payment of rupees {amount:.2f} processed successfully"

    except ConnectionError:
        print("Network Interrupted")
            

retry(788)