'restate:Ek sentence se saare numbers re.findall(r"\d+") se nikaalo.'

# example:I am 17 year old and born in 2009.

# pseudocode:
            # 1.import re
            # 2.create variable nums = re.findall(r"\d+","I am 17 year old and born in 2009.")
            # 3.print(nums)

import re

nums = re.findall(r"\d+","I am 17 year old and born in 2009.")
print(nums)

# dry run:
# ['17', '2009']