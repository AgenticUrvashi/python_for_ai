'restate:Ek text se saare hashtags (#word) nikaalo.'

# example:this is #my #fav food,and #most #nutriant food

# pseudocode:
            # 1.import re
            # 2.create hashtag = re.findall(r"#\w+","this is #my #fav food,and #most #nutriant food")
            # 3.print(hashtag)

import re

hashtag = re.findall(r"#\w+","this is #my #fav food,and #most #nutriant food")

print(hashtag)

# dry run:
# ['#my', '#fav', '#most', '#nutriant']