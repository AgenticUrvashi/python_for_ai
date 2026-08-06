'map + lambda se [1,2,3,4] ke har number ka cube banao.'

# restate: cube ko nikhale ke liye map+lambda use karo.

# example: we have nums=[1,2,3,4] then the output is [1,8,27,64].

# pseudocode:
            # 1.initilize with given.
            # 2.create a variable cube = store in list then apply map then use lambda.
            # 3.print cube.

# translate:

nums = [1,2,3,4]
cube = list(map(lambda x: x**3,nums ))

print(cube)

# dry run:
[1,8,27,64]