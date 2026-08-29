import json

def load_expenses():
    try:
        with open('Expence_Tracter/expence.json','r') as f:
            result = json.load(f)
            return result
    except FileNotFoundError:
        print("File not Found...!")
        return []

    except json.JSONDecodeError:
        print("Please enter correct json format!")
        return []