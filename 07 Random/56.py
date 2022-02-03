import random

num = random.randint(1, 10)

while True:
    guess = int(input('1 between 10: '))
    if guess == num:
        break