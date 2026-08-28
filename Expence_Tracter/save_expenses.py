import json

def save_expences(data):
    with open('Expence_Tracter/expence.json','w') as f:
        result = json.dump(data ,f,indent=4)
        return result
