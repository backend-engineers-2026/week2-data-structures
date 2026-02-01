import math
points = [(0, 0), (3, 4), (1, 2), (5, 12)]

# - Calculate distance from origin for each 
for x, y in points:
    distance = math.sqrt(x**2 + y**2)
    print((x, y), "-", distance)

# - Find point furthest from origin
furthest = max(points, key=lambda p: p[0]**2 + p[1]**2)
print(furthest)

# - Use tuple unpacking
