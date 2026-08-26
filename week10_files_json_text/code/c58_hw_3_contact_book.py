'apni Week 4 ki contact book (list of dicts) ko JSON file mein save aur reload karo.'

# restate: contact book ko json file me load karo.
# example:

# pseudocode:
            # 1.import json
            # 2.create variable contacts_book = [{"name": "Asha", "phone": "98765"}, {"name": "Rahul", "phone": "91234"},{"name":"Priya", "phone": "90000"}]
            # 3.with open("contacts.json", "w", encoding="utf-8") as f:
            # 4.json.dump(contacts_book, f, indent=2)
            # 5.with open("contacts.json", "r", encoding="utf-8") as f:
            # 6.print(json.load(f))

import json

contacts_book = [{"name": "Asha", "phone": "98765"}, {"name": "Rahul", "phone": "91234"},{"name":"Priya", "phone": "90000"}]


with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts_book, f, indent=2)


with open("contacts.json", "r", encoding="utf-8") as f:
    print(json.load(f))

# dry run:
# [{'name': 'Asha', 'phone': '98765'}, {'name': 'Rahul', 'phone': '91234'}, {'name': 'Priya', 'phone': '90000'}]

