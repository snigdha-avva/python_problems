def arr_fun(array1):
    l=len(array1)-1
    for i in range(0,l):
        count=0
        for j in range(i+1,l+1):
            if(array1[i]==array1[j]):
                count+=1
        print('count of '+str
        (array1[i])+'is:',count)

#arr_example = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9, 2, 3, 4, 10]
arr_example = [1, 2, 3, 1, 2, 3, 1, 2, 3]
arr_fun(arr_example)


