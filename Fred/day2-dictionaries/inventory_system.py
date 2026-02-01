# Inventory management system
inventory = {}


# Add item (name, quantity, price)
def add_item(name, quantity, price):
    if name in inventory:  # check if item exists
        print(f"'{name}' already exists. Updating item.")
        inventory[name]["qty"] = quantity
        inventory[name]["price"] = price
    else:  # create a new nested dict
        inventory[name] = {"qty": quantity, "price": price}
        print(f"Added '{name}' to inventory")


# Update quantity (restock or sale)
def update_quantity(name, quantity_change):
    if name not in inventory:
        print(f"Item '{name}' not found")
        return

    current_qty = inventory[name]["qty"]
    new_qty = current_qty + quantity_change

    if new_qty < 0:
        print("Not enough stock for this operation")
        return

    inventory[name]["qty"] = new_qty

    if quantity_change > 0:
        print(f"Restocked '{name}' by {quantity_change}")
    else:
        print(f"Sold {-quantity_change} of '{name}'")


# Search item
def search_item(name):
    if name in inventory:
        item = inventory[name]
        print(
            f"Item found: {name}, "
            f"Quantity: {item['qty']}, "
            f"Price: {item['price']}"
        )
    else:
        print(f"Item '{name}' not found")


# Calculate total inventory value
def total_inventory_value():
    total_value = 0

    for item in inventory.values():
        total_value += item["qty"] * item["price"]

    return total_value
