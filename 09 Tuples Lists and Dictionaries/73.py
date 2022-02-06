food_dictionary = {}
food = list(map(str, input('write favourite food: ').split()))
for i in range(1, len(food)+1):
    food_dictionary[i] = food[i-1]
print(food_dictionary)
dislike = int(input('write food number you dislike: '))
food_dictionary.pop(dislike)
print(sorted(food_dictionary.values()))