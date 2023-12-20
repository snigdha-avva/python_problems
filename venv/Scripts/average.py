def avg_even():
    count=0
    sum=0
    for i in range(24,100+1):
        if i % 2 == 0:
            sum=sum+i
            count=count+1
    avg=sum/count
    print('the avg is : ',avg)
avg_even()

