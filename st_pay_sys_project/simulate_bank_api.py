import random

def simulate_bank_api(amount:float) -> str:
    '''Simulate bank API payment processing, 50% chance of failure'''

    if random.choice([True,False]):
        raise ConnectionError("Bank API is not available/ Bank Timeout/Network Interrupted")
        
    return f"Payment of rupees {amount:.2f} processed successfully"
