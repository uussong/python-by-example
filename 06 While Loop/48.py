answer = 'y'
count = 0

while answer == 'y':
    name = input('name: ')
    print(f'{name} has now been invited')
    count += 1
    answer = input('more? (y/n): ')
print(f'{count} people have been invited')