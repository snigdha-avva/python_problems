#sum of even numbers
a = [3, 4, 5, 6,8,7]
sum=0
for x in range(len(a)):
    if(a[x]%2==0):
        sum=sum+a[x]
print(sum)