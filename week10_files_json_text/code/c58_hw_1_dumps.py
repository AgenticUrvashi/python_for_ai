'ek dict banao aur use json.dumps(indent=2) se sunder print karo.'

# restate:dict ko json me convert karo aur indent = 2 ke sath print karo.
# example:

# pseudocode:
            # 1.import json
            # 2.create variable data =  {
                                    #     'name':"Asha",
                                    #     'age':17,
                                    #     'sub':['math','sci'],
                                    #     'is_student':True
                                    # }
            # 3.create variable ans = json.dumps(data,indent=2) then print(ans)

import json

data = {
    'name':"Asha",
    'age':17,
    'sub':['math','sci'],
    'is_student':True
}

ans = json.dumps(data,indent=2)
print(ans)

# dry run:
# {
#   "name": "Asha",   
#   "age": 17,        
#   "sub": [
#     "math",
#     "sci"
#   ],
#   "is_student": true
# }