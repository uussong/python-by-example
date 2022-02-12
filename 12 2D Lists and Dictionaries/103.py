dict = {}
for i in range(4):
    name = input('name: ')
    age = int(input('age: '))
    size = int(input('shoes size: '))
    dict[name] = {'age': age, 'shoes size': size}

for name in dict:
    print(name, dict[name]['age'])
