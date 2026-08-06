'filter + lambda se [3,8,1,9,4] mein se sirf 5 se bade rakho.'

# restate: hame sirf 5 se bade numbers hi print karne hai.

# example: nums=[3,8,1,9,4] then the output is [8,9]

# pseudocode:
            # 1.starts with given nums = [3,8,1,9,4].
            # 2.create variable greater = store in list then filter then use lambda.
            # 3.print greater.

nums = [3,8,1,9,4]

greater = list(filter(lambda x: x > 5, nums))

print(greater)

# dry run:
[8,9]
