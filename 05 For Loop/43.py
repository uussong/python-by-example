count = input('count down or up? (down/up) ')
if count == 'up':
    num = int(input('top number: '))
    for i in range(1, num+1):
        print(i)
elif count == 'down':
    num = int(input('number below 20: '))
    for i in range(20, num-1, -1):
        print(i)
else:
    print('I don\'t understand')
