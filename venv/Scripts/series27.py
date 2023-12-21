for i in range(1,25):
    if i % 3 == 0:
        if i<24:
            print('factor of three',end=',')
        else:
            print('factor of three')
    else:
        if i < 24:
            print(i,end=',')
        else:
            print(i)