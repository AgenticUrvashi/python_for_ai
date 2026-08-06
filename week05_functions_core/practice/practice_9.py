# Ek sentinel _MISSING banake ek function likho jo "given vs not given" bataye.


__MISSING = object()

def num(value = __MISSING):
    if value == __MISSING:
        print("not given")
    else:
        print(f"given : {value}")

num()
num(8)