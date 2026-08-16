'que : Ek Counter class banao jisme class attribute total ho jo har object par badhe.'

# restate:counter naam ka class banao jisme total naam ka class attribute banao jo har obj pr bhade by 1.

# example:call Counter one time then the output is 1.

# pseudocode:
            # 1.create class Counter.create class attribute total = 0
            # 2.create special method __init__(self) then Counter.total += 1
            # 3.call class then print Counter.total

# translate:
class Counter:
    total = 0

    def __init__(self):
    
        Counter.total += 1

Counter()
print(Counter.total)
Counter()
Counter()
print(Counter.total)

# dry run:
1
3