def divBy11(range1,range2):
    for i in range(range1,range2+1):
        if i % 11 == 0:
            print(i)
divBy11(250,550)