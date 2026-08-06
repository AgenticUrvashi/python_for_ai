# que : recursion se ek list [1,2,3,4,5] ka sum nikaalo (loop use NA karo).

# restate:list ke andar ke nums ka sum nikalo.

# example:list = [1,2,3,4,5]  then the output is 15.

# psudocode:
            # 1.create function nums_sum(list_data).
            # 2.create variable total = 0.
            # 3.use for loop for list_data.
            # 4.update total by adding i.
            # 5.return total.
            # 6.print nums_sum with list.

# translate:

def nums_sum(list_data):
    total = 0
    for i in list_data:
        total = total + i
    
    return total


print(nums_sum([1,2,3,4,5]))

# dry run:
15

def nums_sum(list_data,index = 0):
    if list_data == len(list_data):
        return 0

    return list_data[index]+nums_sum(list_data[index+1])

print(nums_sum([3,5,7,3,7]))