from get_valid_marks import get_valid_marks
from process_payment_with_retry import process_payment_with_retry
from bank_balance import get_valid_bank_balance
from bank_balance import valid_sub_fee

class InsufficientBalanceError(Exception):
    'raised when the balance is less than exam fee'
    pass

def main():
    print("="*50)
    print("Welcome to the Student Marks and Payment system")
    print("="*50)


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
            
        receipt = valid_sub_fee()

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
