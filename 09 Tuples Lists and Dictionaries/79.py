nums = []
count = 0

while count < 3:
    num = int(input('write number: '))
    nums.append(num)
    print(nums)
    count += 1

save = input('save last number? (y/n): ')
if save == 'n':
    nums.pop()
print(nums)