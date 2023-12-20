def sumAllEven(r1,r2):
    sum = 0
    for i in range(r1+1,r2):
        if i % 2 == 0:
            sum = sum + i
    print(sum)

sumAllEven(382,582)