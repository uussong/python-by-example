name = input('name: ')
num = int(input('number: '))

if num < 10:
    for i in range(0, num):
        print(name)
else:
    print('Too high')