# Exercise 1: Coordinate system
from unicodedata import category


points = [(0, 0), (3, 4), (1, 2), (5, 12)]

# Initialize variables to store the running maximum
max_distance = 0
furthest_point = None

# - Calculate distance from origin for each
# - Use tuple unpacking (x, y) directly in the loop definition
for x, y in points:
    distance = (x**2 + y**2) ** 0.5
    print(f"Point ({x}, {y}) is distance {distance:.2f} from origin")

    # - Find point furthest from origin
    # This logic must be INSIDE the loop to check every point
    if distance > max_distance:
        max_distance = distance
        furthest_point = (x, y)

print(f"Furthest point is {furthest_point} with distance {max_distance}")
