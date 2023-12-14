def even(range1,range2):
    count=0
    for i in range(range1,range2+1):
        if i % 2 == 0:
            count = count +1
    print(count)
even(1,10)