'Restate: Ek sentence mein har word ki frequency Counter se nikaalo.'

# example:I can learn, learn, and learn, because practice makes me better every day

# pseudocode:
            # 1.from collections import Counter
            # 2.we use print then counter then enter line then split it.
            # like this:
            #       print(Counter("I can learn, learn, and learn, because practice makes me better every day".split()))

from collections import Counter

print(Counter("I can learn, learn, and learn, because practice makes me better every day".split()))

# dry run:
# Counter({'learn,': 3, 'I': 1, 'can': 1, 'and': 1, 'because': 1, 'practice': 1, 
#           'makes': 1, 'me': 1, 'better': 1, 'every': 1, 'day': 1})