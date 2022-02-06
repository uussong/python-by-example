num_list = [123, 234, 345, 456]
for num in num_list:
    print(num)

num = int(input('write number in the list: '))
if num in num_list:
    print(num_list.index(num))
else:
    print('That is not in the list')