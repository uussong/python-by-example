vowel = ['a', 'e', 'i', 'o', 'u']
count = 0

name = input('write name: ')
for i in name:
    if i in vowel:
        count += 1
print(count)
