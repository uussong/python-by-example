import random

score = 0

for i in range(5):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2
    print(f'{num1}+{num2}')
    guess = int(input('number: '))
    print()
    if answer == guess:
        score += 1
print(f'score: {score}/5')