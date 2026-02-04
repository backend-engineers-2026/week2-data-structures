import math

points = [(0, 0),  (1, 21), (3, 12), (7, 12)]

# Calculate distance for each point
for point in points:
    x, y = point
    distance = math.sqrt(x**2 + y**2)
    print(f"Point {point} is {distance:.2f} units from origin")  

# Find the furthest point
furthest_point = max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))
print("\nThe point furthest from the origin is:", furthest_point)







from collections import defaultdict

# ============================================================================
# EXERCISE 2: Group Students by Grade
# ============================================================================

print("\n" + "=" * 75)
print("EXERCISE 2: Group Students by Grade")
print("=" * 75)

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "C")
]

print(f"\nStudent list: {students}\n")

# Method 1: Using a regular dictionary
print("1. Grouping students by grade (using dict):")
grade_groups = {}

for student_name, grade in students:  # Tuple unpacking
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(student_name)

for grade, names in sorted(grade_groups.items()):
    print(f"   Grade {grade}: {names}")

# Method 2: Using defaultdict (cleaner)
print("\n2. Using defaultdict (more elegant):")
grade_groups_v2 = defaultdict(list)

for name, grade in students:
    grade_groups_v2[grade].append(name)

for grade, names in sorted(grade_groups_v2.items()):
    print(f"   Grade {grade}: {names}")

# Task 2: Count students per grade
print("\n3. Count students per grade:")
grade_counts = {grade: len(names) for grade, names in grade_groups.items()}
for grade, count in sorted(grade_counts.items()):
    print(f"   Grade {grade}: {count} student(s)")

# Alternative: Count directly from original list
print("\n4. Alternative counting method:")
from collections import Counter
all_grades = [grade for name, grade in students]
grade_distribution = Counter(all_grades)
for grade, count in sorted(grade_distribution.items()):
    print(f"   Grade {grade}: {count} student(s)")

# Bonus: Statistics
print("\n5. BONUS - Additional Statistics:")
print(f"   Total students: {len(students)}")
print(f"   Number of different grades: {len(grade_groups)}")
print(f"   Most common grade: {grade_distribution.most_common(1)[0][0]}")
print(f"   Grades with only one student: {[g for g, c in grade_counts.items() if c == 1]}")

# Bonus: Create reverse mapping (grade -> students)
print("\n6. BONUS - Students sorted by name within each grade:")
for grade in sorted(grade_groups.keys()):
    sorted_names = sorted(grade_groups[grade])
    print(f"   Grade {grade}: {', '.join(sorted_names)}")


# ============================================================================
# EXERCISE 3: Product Catalog
# ============================================================================

print("\n" + "=" * 75)
print("EXERCISE 3: Product Catalog")
print("=" * 75)

products = [
    (1, "Laptop", 999.99, "Electronics"),
    (2, "Desk", 199.99, "Furniture"),
    (3, "Mouse", 29.99, "Electronics"),
    (4, "Chair", 149.99, "Furniture"),
    (5, "Keyboard", 79.99, "Electronics"),
    (6, "Monitor", 299.99, "Electronics")
]

print(f"\nTotal products: {len(products)}\n")

# Display all products
print("All Products:")
print("-" * 75)
for product_id, name, price, category in products:  # Tuple unpacking
    print(f"ID: {product_id} | {name:<15} | ${price:>7.2f} | {category}")
print("-" * 75)

# Task 1: Find all electronics
print("\n1. All Electronics:")
electronics = [product for product in products if product[3] == "Electronics"]
# Or with tuple unpacking:
electronics_v2 = [(pid, name, price, cat) for pid, name, price, cat in products if cat == "Electronics"]

for product_id, name, price, category in electronics:
    print(f"   {name}: ${price:.2f}")

# Task 2: Calculate average price per category
print("\n2. Average price per category:")

# Group by category first
category_prices = defaultdict(list)
for product_id, name, price, category in products:
    category_prices[category].append(price)

# Calculate averages
for category, prices in sorted(category_prices.items()):
    avg_price = sum(prices) / len(prices)
    print(f"   {category}: ${avg_price:.2f} (based on {len(prices)} items)")

# Alternative: More detailed statistics
print("\n3. Detailed category statistics:")
for category, prices in sorted(category_prices.items()):
    print(f"   {category}:")
    print(f"      Count: {len(prices)}")
    print(f"      Average: ${sum(prices) / len(prices):.2f}")
    print(f"      Min: ${min(prices):.2f}")
    print(f"      Max: ${max(prices):.2f}")
    print(f"      Total value: ${sum(prices):.2f}")

# Task 3: Sort by price
print("\n4. Products sorted by price (ascending):")
sorted_by_price = sorted(products, key=lambda p: p[2])
for product_id, name, price, category in sorted_by_price:
    print(f"   ${price:>7.2f} - {name} ({category})")

print("\n5. Products sorted by price (descending):")
sorted_by_price_desc = sorted(products, key=lambda p: p[2], reverse=True)
for product_id, name, price, category in sorted_by_price_desc[:3]:  # Top 3
    print(f"   ${price:>7.2f} - {name} ({category})")

# Bonus: Multiple sorting criteria
print("\n6. BONUS - Sort by category, then by price within category:")
sorted_multi = sorted(products, key=lambda p: (p[3], p[2]))
current_category = None
for product_id, name, price, category in sorted_multi:
    if category != current_category:
        print(f"\n   {category}:")
        current_category = category
    print(f"      ${price:>7.2f} - {name}")

# Bonus: Find most expensive item per category
print("\n7. BONUS - Most expensive item per category:")
for category in sorted(category_prices.keys()):
    category_products = [(name, price) for pid, name, price, cat in products if cat == category]
    most_expensive = max(category_products, key=lambda x: x[1])
    print(f"   {category}: {most_expensive[0]} - ${most_expensive[1]:.2f}")

# Bonus: Product name to price lookup
print("\n8. BONUS - Price lookup dictionary:")
price_lookup = {name: price for pid, name, price, cat in products}
print(f"   {price_lookup}")

# Bonus: Filter products by price range
print("\n9. BONUS - Products between $100 and $300:")
mid_range = [(name, price) for pid, name, price, cat in products if 100 <= price <= 300]
for name, price in mid_range:
    print(f"   {name}: ${price:.2f}")
