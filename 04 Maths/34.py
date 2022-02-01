print('1) Square \n2) Triangle\n')
num = int(input('Enter a number: '))

if num == 1:
    side = int(input('side: '))
    print(side**2)
elif num == 2:
    base = int(input('base: '))
    height = int(input('height: '))
    print((base*height)/2)
else:
    print('Error')