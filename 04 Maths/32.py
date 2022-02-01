import math

radius = int(input('radius: '))
depth = int(input('depth: '))
area = (radius**2)*math.pi
volume = area * depth
print(round(volume, 3))