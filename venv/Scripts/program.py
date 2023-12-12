def program():
    num = int(input('please enter a number:'))
    
    if num >= 100 and num <= 1000:
        if num % 2 == 0:
            rem = num % 3
            print('the remainder is:',rem)
        else:
            rem= num % 2
            print('the remainder is:',rem)
    else:
        print('wrong number')

program()
