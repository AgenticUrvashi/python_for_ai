# {1,2,3,4} ke har number ka cube ek dict comprehension se banao {num: cube}.

nums = {1,2,3,4}

new = {num: num ** 3 for num in nums}
print(new)