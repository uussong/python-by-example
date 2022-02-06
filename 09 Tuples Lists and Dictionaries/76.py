guest_list = list(map(str, input('write 3 guest: ').split()))
another_guest = input('another guest? (y/n): ')

while another_guest == 'y':
    guest_list.append(input('write guest: '))
    another_guest = input('another guest? (y/n): ')
print(f'total guest: {len(guest_list)}')