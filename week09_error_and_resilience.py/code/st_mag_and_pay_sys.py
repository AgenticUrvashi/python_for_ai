## student marks should be in between 0 - 100 in number format

import random
import time


class InvalidMarksError(Exception):
    'Raised when the marks are not in between 0 - 100'
    pass

class InsufficientBalanceError(Exception):
    'raised when the balance is less than exam fee'
    pass

def get_valid_marks(subject_name:str) -> float:

    while True:
        try:
            raw_marks = input(f"♻ Enter the marks for {subject_name} in between 0 - 100: ")
            marks = float(raw_marks)
            
            if marks < 0 or marks > 100:
                raise InvalidMarksError(f"Invalid marks for {subject_name}, must be in between 0 - 100")

            return marks

        except ValueError as e:
            print(f"Error: {e}")

        except InvalidMarksError as e:
            print(f"Error: {e}")


def simulate_bank_api(amount:float) -> str:
    '''Simulate bank API payment processing, 50% chance of failure'''

    if random.choice([True,False]):
        raise ConnectionError("Bank API is not available/ Bank Timeout/Network Interrupted")
        
    return f"Payment of rupees {amount:.2f} processed successfully"

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

def main():
    print("="*50)
    print("Welcome to the Student Marks and Payment system")
    print("="*50)

    student_bank_balance = 1000.00
    per_subject_exam_fee = 200



    try:
        mark_phy = get_valid_marks("physics")
        mark_maths = get_valid_marks("maths")
        maark_chem = get_valid_marks("chemistry")

        total_marks = mark_phy + mark_maths + maark_chem
        percentage = (total_marks / 300) * 100

        if percentage < 50 or mark_phy < 50 or mark_maths < 50 or maark_chem < 50:
            print("Sorry, you are failed in the exam")
            print("You need to pay the exam fee again")

        else:
            print(f"Congratulations, you are passes in the exam with {percentage:.2f}%")
            print("You don't need to pay the exam fee again")
            return None

        total_fee = per_subject_exam_fee * 3

        if student_bank_balance < total_fee:
            raise InsufficientBalanceError(f"Insufficient balance in the bank account, you need to pay {total_fee:.2f} ruppes.")

        receipt = process_payment_with_retry(total_fee)

    except InsufficientBalanceError as e:
        print(f"❌ Registration canceled: {e}")

    except ConnectionError as e:
        print(f"❌ Network Failure: {e}")

    except Exception as e:
        print(f"❌ An unexcpected error occurred: {e}")

    else:
        print("✅Registration successful")
        print(f"Student registration receipt: {receipt}")

    finally:
        print("🔒 Session closed securely. Thank you for using our system.")


if __name__ == "__main__":

    main()
