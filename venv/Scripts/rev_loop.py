def odd(range1,range2):
    for i in range(range1,range2-1,-1):
        if i % 2 != 0:
            print(i)


odd(251,51)