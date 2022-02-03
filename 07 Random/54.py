import random

choice = random.choice(['h', 't'])
guess = input('h or t: ')

if choice == guess:
    print('You win')
else:
    print('Bad luck')
print(choice)