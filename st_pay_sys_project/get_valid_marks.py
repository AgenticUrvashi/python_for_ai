class InvalidMarksError(Exception):
    'Raised when the marks are not in between 0 - 100'
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

