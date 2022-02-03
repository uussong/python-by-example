import random

color = random.choice(['pink', 'yellow', 'blue', 'green', 'purple'])
tryagain = True

while True:
    guess = input('choice color (pink/yellow/blue/green/purple): ')
    if guess == color:
        print('Well done')
        break
    else:
        if color == 'pink':
            print('Feeling like p..')
        elif color == 'yellow':
            print('Feeling like y..')
        elif color == 'blue':
            print('Feeling like b..')
        elif color == 'green':
            print('Feeling like g..')
        elif color == 'purple':
            print('Feeling like p..')