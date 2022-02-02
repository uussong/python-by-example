num = 10
while num > 0:
    print(f'There are {num} green bottles hanging on the wall, {num} greenbottles hanging on the wall, and if 1green bottle should accidentally fall')
    num -= 1
    answer = int(input('how many green bottles will be hanging on the wall? '))
    if num == answer:
        print(f'There will be {num} green bottles hanging on the wall')
    else:
        while num != answer:
            answer = int(input('try again: '))
print('There are no more green bottles hanging on the wall')