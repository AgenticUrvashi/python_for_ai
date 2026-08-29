import json

def save_expences(data):
    try:
        with open('Expence_Tracter/expence.json','w') as f:
            json.dump(data ,f,indent=4)

    except PermissionError:
        print("You don't have permission to write this file!")

    except TypeError:
        print("Data cannot be stored in JSON format!")