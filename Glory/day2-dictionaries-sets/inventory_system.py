# Inventory management system
inventory = {
    "laptop": {"quantity": 10, "price": 999.99},
    "mouse": {"quantity": 25, "price": 19.99},
    "keyboard": {"quantity": 30, "price": 49.99}
}

# - Add item (name, quantity, price)
def add_item():
    name = input("Enter item name: ").lower()
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))

    inventory[name] = {"quantity": quantity, "price": price}
    print(f"Item '{name}' added to inventory.")


# - Update quantity (restock/sale)
def update_quantity():
    name = input("Enter item: ").lower()

    if name not in inventory:
        print(f"Item not found in inventory.")
        return
    
    change = int(input("Enter quantity change (+/-): "))
    inventory[name]["quantity"] += change
    print(f"Quantity updated.")

# - Search item
def search_item():
    name = input("Item name: ").lower()
    item = inventory.get(name)

    if not item:
        print("Item not found in inventory.")
    else:
        print(f"{name} - Quantity: {item['quantity']}, Price: {item['price']}")


# - Calculate total inventory value
def total_value():
    total = sum(item["quantity"] * item["price"] for item in inventory.values())
    print("Total inventory value:", total)

# - view inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\nInventory:")
    for name in sorted(inventory):
        item = inventory[name]
        print(f"{name}: Quantity={item['quantity']}, Price={item['price']}")

def main():
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add item")
        print("2. Update quantity")
        print("3. Search item")
        print("4. View inventory")
        print("5. Total inventory value")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            search_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            total_value()
        elif choice == "6":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()