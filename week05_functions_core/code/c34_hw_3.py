#que: Ek sentinel _MISSING banake ek function likho jo "given vs not given" bataye.

# restate:missing ka concept dikhao.

# example: value =  , 4

# pseudocode:
            # 1.create variable __missing = object()
            # 2.create new function data(value = __missing)
            # 3.if value == __missing then print not given.
            # 4.else print given.
            # 5.call the function.

# translate:
__MISSING = object()

def data(value = __MISSING):
    if value == __MISSING:
        print("not given")
    else:
        print("given")

data()
data(4)

# dry run:
# not given
# given