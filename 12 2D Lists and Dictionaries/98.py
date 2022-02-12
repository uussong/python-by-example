list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input('row: '))
print(list[row])
new_num = int(input('Enter new number: '))
list[row].append(new_num)
print(list[row])