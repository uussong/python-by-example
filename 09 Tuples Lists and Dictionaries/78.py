tv = ['drama', 'news', 'music show', 'talk show']
for i in tv:
    print(i)

another_tv = input('write another tv program: ')
index = int(input('index you want: '))

tv.insert(index, another_tv)
print(tv)