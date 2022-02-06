guest_list = list(map(str, input('write 3 guest: ').split()))
another_guest = input('another guest? (y/n): ')

while another_guest == 'y':
    guest_list.append(input('write guest: '))
    another_guest = input('another guest? (y/n): ')
print(guest_list)

name = input('write one of name in the list: ')
print(name, guest_list.index(name))

confirm = input('really invite? (y/n): ')
if confirm == 'n':
    guest_list.remove(name)
print(guest_list)