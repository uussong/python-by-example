total = 0
for i in range(0, 5):
    num = int(input('number: '))
    answer = input('add? (y/n) ')
    if answer == 'y':
        total += num
print(total)