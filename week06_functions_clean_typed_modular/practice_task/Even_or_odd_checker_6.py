'''
EN: Write a function is_even(n) that returns True if the number is even, else False.
 Use it in a loop to print which numbers in [3, 8, 15, 22, 41] are even.
हिंदी: एक function is_even(n) बनाओ जो number even होने पर True, वरना False return करे। 
इसे loop में इस्तेमाल करके बताओ [3, 8, 15, 22, 41] में कौन-से numbers even हैं।
Concepts: returning a boolean, %, using a function in a loop
Hint: return n % 2 == 0.
'''

# restate:ek function banao jo batai konsi value even hai.

# example:list = [3, 8, 15, 22, 41] then the output is 8 :even

# pseudocode:
            # 1.create a function is_even(n)
            # 2.use for loop for n list.
            # 3.if i%2==0 then return i is even.
            # 4.print the function.

# translate to code:
def is_even(n=list) -> str:
    for i in n:
        if i % 2 == 0:
            return f"{i} : even"

print(is_even([3, 8, 15, 22, 41]))

# dry run:
# 8 : even