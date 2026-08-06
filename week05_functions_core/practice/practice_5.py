def average():
    marks = [40, 55, 70, 90]
    total = 0
    for i in marks:
        total = total + i

    average = total /len(marks)
    print(average)

average()
