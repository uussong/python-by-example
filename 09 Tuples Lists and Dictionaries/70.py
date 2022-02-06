country_tuple = ('Korea', 'Japan', 'China', 'Russia', 'USA')
print(country_tuple)

country = input('write one country: ')
print(f'{country}\'s index: {country_tuple.index(country)}')

num = int(input('number between 0 and 4: '))
print(country_tuple[num])