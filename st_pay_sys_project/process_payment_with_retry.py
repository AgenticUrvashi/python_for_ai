from simulate_bank_api import simulate_bank_api
import time

def process_payment_with_retry(amount:float, max_attempts: int = 3) -> str:
    '''Process payment with retry, if payment fails, retry with exponential backoff'''

    for attempt in range(1, max_attempts+1):
        try:

            print(f"Attempt {attempt} of {max_attempts} to process payment of rupees {amount:.2f}")

            result = simulate_bank_api(amount)
            return result

        except ConnectionError as e:
            print(f"Attempt {attempt} failed: {e}")

            if attempt < max_attempts:
                wait = 2 ** (attempt - 1)
                time.sleep(wait)
            else:
                raise ConnectionError("Max attempts reached, payment failed")
