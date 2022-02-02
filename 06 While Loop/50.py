num = int(input('10 between 20: '))

while num < 10 or num > 20:
    if num < 10:
        print('Too low')
    elif num > 20:
        print('Too high')
    num = int(input('Try again: '))
print('Thank you')
