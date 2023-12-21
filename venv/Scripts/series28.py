for i in range(1,26):
    if i % 5 == 0:
        if i < 25:
            print('divisible by five',end=',')
        else:
            print('divisible by five')
    elif i % 2 !=0:
        if i<25:
            print(i,end=',')
        else:
            print(i)