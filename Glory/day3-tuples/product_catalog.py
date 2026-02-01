# List of tuples: (product_id, name, price, category)
products = [
    (1, "Laptop", 999.99, "Electronics"),
    (2, "Desk", 199.99, "Furniture"),
    (3, "Mouse", 29.99, "Electronics")
]

# - Find all electronics
electronics = [product for product in products if product[3] == "Electronics"]
print("Electronics:", electronics)

# - Calculate average price per category
category_totals = {}
category_counts = {}

for product in products:
    category = product[3]
    if category not in category_totals:
        category_totals[category] = 0.0
        category_counts[category] = 0
    category_totals[category] += product[2]
    category_counts[category] += 1
average_prices = {cat: category_totals[cat] / category_counts[cat] for cat in category_totals}
   
print("Average price per category:", average_prices)

# - Sort by price
sorted_products = sorted(products, key=lambda x: x[2])
print("Sorted by price:", sorted_products)
