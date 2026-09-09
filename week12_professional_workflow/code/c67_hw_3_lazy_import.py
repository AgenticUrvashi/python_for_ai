'Que: ek function banao jisme heavy import (import json) andar ho (lazy style).'



def save_data():
    import json

    data = {"name": "Urvashi"}

    with open("data.json", "w") as f:
        json.dump(data, f)