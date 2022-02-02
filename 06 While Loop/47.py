a = int(input('number: '))
total = a
answer = 'y'

while answer == 'y':
    c = int(input('other number: '))
    total += c
    answer = input('add more? (y/n): ')
print(total)
