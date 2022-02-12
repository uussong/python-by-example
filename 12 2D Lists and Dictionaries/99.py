list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input('row: '))
print(list[row])
col = int(input('col: '))
print(list[row][col])

change = input('wanna change? y/n: ')
if change == 'y':
    new_num = int(input('new number: '))
    list[row][col] = new_num
    print(list[row])