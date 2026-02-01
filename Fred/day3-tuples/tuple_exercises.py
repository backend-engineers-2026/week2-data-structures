# Exercise 2: Group students by grade
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("Diana", "C")]
# Create dict to group: {"A": ["Alice", "Charlie"], ...}
groups = {}
for name, grade in students:  # unpack tuple
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)
# Count students per grade by dict comprehension
counts = {grade: len(names) for grade, names in groups.items()}
print("Grouped Students:", groups)
print("Counts per grade:", counts)

# Exercise 3: Product catalog
# List of tuples: (product_id, name, price, category)
products = [
    (1, "Laptop", 999.99, "Electronics"),
    (2, "Desk", 199.99, "Furniture"),
    (3, "Mouse", 29.99, "Electronics"),
]
# - Find all electronics
electronics = [p for p in products if p[3] == "Electronics"]
# - Calculate average price per category
category_totals = {}
for _, _, price, category in products:  # unpack and ignore unused values
    if category not in category_totals:
        category_totals[category] = (0, 0)  # (total_price, count)
    total, count = category_totals[category]
    category_totals[category] = (total + price, count + 1)
    averages = {
        category: total / count for category, (total, count) in category_totals.items()
    }

# - Sort by price
sorted_products = sorted(products, key=lambda p: p[2])

print("Electronics:", electronics)
print("Average price per category:", averages)
print("Sorted by price:", sorted_products)
