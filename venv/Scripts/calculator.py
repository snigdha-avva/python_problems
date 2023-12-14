def cal(a,op,b):
    if op == '*':
        result = a * b
        print('the result is : ',result)
    elif op == '/':
        result = a / b
        print('the result is : ',result)
    elif op == '+':
        result = a + b
        print('the result is : ',result)
    elif op == '-':
        result = a - b
        print('the result is : ',result)

    else:
        print('wrong input')
cal(2,'+',5)

