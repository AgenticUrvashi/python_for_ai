from process_payment_with_retry import process_payment_with_retry
from simulate_bank_api import simulate_bank_api

class InsufficientBalanceError(Exception):
    'raised when the balance is less than exam fee'
    pass


def get_valid_bank_balance(bank_balance = 2000):
    return bank_balance

def valid_sub_fee():
    no_of_sub = int(input("enter subject number: "))
    per_subject_exam_fee = 200
    total_fee = per_subject_exam_fee * no_of_sub

    student_bank_balance = get_valid_bank_balance()

    if student_bank_balance < total_fee:
        raise InsufficientBalanceError(f"Insufficient balance in the bank account, you need to pay {total_fee:.2f} ruppes.")


    receipt = process_payment_with_retry(total_fee)

    return receipt
    
if __name__ == "__main__":

    valid_sub_fee()


