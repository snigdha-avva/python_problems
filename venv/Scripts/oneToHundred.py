def oneToHundred():
    marks=int(input('please enter your marks:'))
    if marks >= 0 and marks <=100:
        if marks in range(90,100):
            print('super smart')
        elif marks in range(80,90):
            print('smart')
        elif marks in range(70,80):
            print('smart enough')
        elif marks in range(60,70):
            print('just smart')
        elif marks in range(35,60):
            print('no smart')
        else:
            print('dumb')
    else:
        print('invalid input')
oneToHundred()