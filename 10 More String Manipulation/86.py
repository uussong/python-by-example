password = input('write password: ')
password_confirm = input('write password again: ')

if password == password_confirm:
    print('Thank you')
elif password.lower() == password_confirm.lower():
    print('They must be in the same case')
else:
    print('Incorrect')
