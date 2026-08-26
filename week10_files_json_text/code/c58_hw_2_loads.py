'ek JSON string "{"city":"mumbai","pin":400001}" ko dict mein load karke city print karo.'

# restate: given string ko json me load karo aur uski city print karo.
# example: output = mumbai

# pseudocode:
            # 1.import json
            # 2.create variable Json = '{"city":"mumbai","pin":400001}'
            # 3.create another variable ans = json.loads(Json)
            # 4.print(ans["city"])

import json

Json = '{"city":"mumbai","pin":400001}'

ans = json.loads(Json)
print(ans["city"])

# dry run:
# mumbai