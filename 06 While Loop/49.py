compnum = 50
guess = int(input('guess number: '))
count = 1

while compnum != guess:
    if guess < compnum:
        print('Too low')
    else:
        print('Too high')
    count += 1
    guess = int(input('another guess: '))
print(f'Well done, you took {count} attempts')