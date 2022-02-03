import random

num = random.randint(1, 10)

while True:
    guess = int(input('1 between 10: '))
    if guess > num:
        print('Too high')
    elif guess < num:
        print('Too low')
    elif guess == num:
        break