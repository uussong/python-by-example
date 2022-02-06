from re import sub


subject_list = ['english', 'math', 'society', 'science', 'korean', 'history']
print(subject_list)
dislike = input('write subject you dislike: ')
subject_list.remove(dislike)
print(subject_list)