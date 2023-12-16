def even(range1,range2):
    alternate = 'yes'
    for i in range(range1,range2+1):
            if i % 2 == 0:
                if alternate == 'yes':
                    print(i)
                    alternate = 'no'
                else:
                    alternate = 'yes'


even(20,40)