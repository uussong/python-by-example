word = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
if word[0] in vowels:
    word = word + 'way'
    print(word)
else:
    word = word[1:] + word[0] + 'ay'
    print(word)