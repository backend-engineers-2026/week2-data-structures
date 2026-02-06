import math

# ============================================================================
# EXERCISE 1: Coordinate System
# ============================================================================

print("=" * 75)
print("EXERCISE 1: Coordinate System")
print("=" * 75)

points = [(0, 0), (3, 4), (1, 2), (5, 12)]
print(f"\nPoints: {points}\n")

# Task 1: Calculate distance from origin for each point
print("1. Distance from origin for each point:")

distances = []
for point in points:
    x, y = point  # Tuple unpacking
    distance = math.sqrt(x**2 + y**2)
    distances.append((point, distance))
    print(f"   Point {point}: {distance:.2f}")

# Alternative: Using list comprehension with tuple unpacking
distances_v2 = [(point, math.sqrt(x**2 + y**2)) for x, y in points]
print(f"\n2. Using list comprehension:")
for point, dist in distances_v2:
    print(f"   Point {point}: {dist:.2f}")

# Task 2: Find point furthest from origin
furthest_point, max_distance = max(distances, key=lambda item: item[1])
print(f"\n3. Furthest point from origin:")
print(f"   Point: {furthest_point}")
print(f"   Distance: {max_distance:.2f}")

# Alternative method: Using max with generator expression
furthest_v2 = max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
furthest_distance_v2 = math.sqrt(furthest_v2[0]**2 + furthest_v2[1]**2)
print(f"\n4. Alternative method:")
print(f"   Furthest point: {furthest_v2} at distance {furthest_distance_v2:.2f}")
