class Inventory:
    def __init__(self, filename="inventory.txt"):
        self.items = {}
        self.filename = filename
        self._load()
    
    def _load(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    name, qty, price = line.strip().split('|')
                    self.items[name] = {"qty": int(qty), "price": float(price)}
        except FileNotFoundError:
            pass
    
    def _save(self):
        with open(self.filename, 'w') as f:
            for name, data in self.items.items():
                f.write(f"{name}|{data['qty']}|{data['price']}\n")
    
    def add(self, name, qty, price):
        if qty <= 0 or price <= 0:
            print("Values must be positive"); return
        if name in self.items:
            print("Item exists. Use update."); return
        self.items[name] = {"qty": qty, "price": price}
        self._save()
        print(f"Added {name}")
    
    def update(self, name, delta):
        if name not in self.items:
            print("Item not found"); return
        new_qty = self.items[name]['qty'] + delta
        if new_qty < 0:
            print("Insufficient stock"); return
        self.items[name]['qty'] = new_qty
        self._save()
        print(f"{name}: {new_qty} in stock")
    
    def search(self, name):
        if name in self.items:
            d = self.items[name]
            print(f"{name}: {d['qty']} units @ ${d['price']:.2f}")
        else:
            print("Not found")
    
    def value(self):
        total = sum(d['qty'] * d['price'] for d in self.items.values())
        print(f"Total Value: ${total:,.2f}")
        return total
    
    def list_all(self):
        print(f"{'Item':<15}{'Qty':<8}{'Price':>10}{'Value':>12}")
        print("-" * 45)
        for name, d in self.items.items():
            val = d['qty'] * d['price']
            print(f"{name:<15}{d['qty']:<8}${d['price']:>9.2f}${val:>11.2f}")

# Demo
inv = Inventory()
inv.add("laptop", 10, 999.99)
inv.add("mouse", 50, 29.99)
inv.update("laptop", -2)  # Sale
inv.update("mouse", 20)   # Restock
inv.search("laptop")
inv.list_all()
inv.value()