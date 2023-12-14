def even(range1,range2):
    list1 = []
    for i in range(range1,range2+1):
        if i % 2 == 0:
            list1.append(i)
    print(list1[::2])


even(20,40)