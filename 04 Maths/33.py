a, b = map(int, input().split())
share = a // b
remainder = a % b
print(f'{a} divided by {b} is {share} with {remainder} remaining')