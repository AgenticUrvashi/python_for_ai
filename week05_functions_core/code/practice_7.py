def even_count():
    nums = [1,4,6,7,10,3]
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1

    print(count)

even_count()
