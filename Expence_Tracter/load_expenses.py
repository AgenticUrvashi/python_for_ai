import json

def load_expenses():
    with open('Expence_Tracter/expence.json','r') as f:
        result = json.load(f)
        return result
