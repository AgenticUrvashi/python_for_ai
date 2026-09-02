'Restate: ek @count_calls decorator jo gine function kitni baar call hua.'

# example: when we call 1st time then printed 1 then another time its 2 then 3 then more than.

# pseudocode:
            # 1.create variable count = 0.
            # 2.create decorator count_calls(func): then create function wrapper():
            # 3.create variable result = func() then print(result)
            # 4.return function wrapper
            # 5.write decorator @count_calls.
            # 6.create function calls():
            # 7.write global count
            # 8.update variable count = count + 1 then result count
            # 9.call the function calls().

count = 0
def count_calls(func):
    def wrapper():
        result = func()
        print(result)
    return wrapper

@count_calls
def calls():
    global count
    count = count + 1
    return count

calls()
calls()
calls()

# dry run:
1
2
3