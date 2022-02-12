dict = {}
for i in range(4):
    name = input('name: ')
    age = int(input('age: '))
    size = int(input('shoes size: '))
    dict[name] = {'age': age, 'shoes size': size}

ask = input('Enter name: ')
print(dict[ask])
