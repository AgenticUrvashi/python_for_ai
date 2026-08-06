# que : recursion se 5 se 1 tak countdown karo.

# restate: 5 se 1 tak ulta print karo.

# example:countdown(5)  and the output is 5,4,3,2,1

# pseudocode:
            # 1.create function countdown(n).
            # 2.print n .
            # 3.if n == 1 print countdown completed.
            # 4.return
            # 5.countdown(n-1)
            # 6.call the countdown(5).

# translate:
def countdown(n):
    print(n)

    if n == 1:
        print("countdown completed")
        return

    countdown(n-1)

countdown(5)

# dry run:
5
4
3
2
1
