message = input('write a message in uppercase: ')

while True:
    if message.isupper():
        print(message)
        break
    else:
        message = input('write a message in uppercase: ')