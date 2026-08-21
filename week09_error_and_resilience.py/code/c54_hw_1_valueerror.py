'Ek function set_marks(m) jo 0 - 100 ke bahar value par Valueerror raise kare.'

# restate: ek function banao jo 0 - 100 tak ke marks hi le baki ValueError dikhaye.

# example: marks = -78 gives error

# pseudocode:
            # 1.create function set_marks(m)
            # 2.if m not in range(1,101) then raise ValueError("marks must be between 0-100")
            # 3.else: print("congrats! you enter right marks")

def set_marks(m):
    if m not in  range(0,101):
        raise ValueError("marks must be between 0 - 100.")

    else:
        print("congrats! you enter right marks")

set_marks(-78)

# dry run:
# raise error of type ValueError.