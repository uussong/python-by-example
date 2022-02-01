num = int(input('party guest: '))

if num < 10:
    for i in range(0, num):
        name = input('name: ')
        print(f'{name} has been invited')
else:
    print('Too many people')