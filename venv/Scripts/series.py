def series():
    for i in range(2,17):
        if i < 16:
            print('%d * %d'%(i,i+1),end=',')
        else:
            print('16 * 17')

def seriesMul():
    for i in range(2,17):
        if i < 16:
            print(i*(i+1),end=',')
        else:
            print(16*17)

series()
seriesMul()