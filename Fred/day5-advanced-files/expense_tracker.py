import os

EXPENSE_FILE = "expenses.txt"


def add_expense(date, category, amount, description):
    """Formats and appends a new expense to the file."""
    # Ensure file ends with newline or starts clean
    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{date}|{category}|{amount}|{description}\n")
    print(f"Added: {description} (${amount})")


def read_expenses():
    """Reads file and parses each line into a list of dictionaries."""
    if not os.path.exists(EXPENSE_FILE):
        return []

    expenses = []
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            if not line.strip():
                continue  # Skip empty lines
            parts = line.strip().split("|")
            if len(parts) == 4:
                expenses.append(
                    {
                        "date": parts[0],
                        "category": parts[1],
                        "amount": float(parts[2]),
                        "description": parts[3],
                    }
                )
    return expenses


def filter_by_category(category):
    """Returns only expenses matching a specific category."""
    all_expenses = read_expenses()
    return [e for e in all_expenses if e["category"].lower() == category.lower()]


def calculate_total(expense_list=None):
    """Sums amounts. If no list provided, sums all expenses in file."""
    if expense_list is None:
        expense_list = read_expenses()
    return sum(e["amount"] for e in expense_list)


def calculate_monthly_total(year_month):
    """Sums amounts for a specific month (format: 'YYYY-MM')."""
    all_expenses = read_expenses()
    monthly = [e for e in all_expenses if e["date"].startswith(year_month)]
    return calculate_total(monthly)


# Example Usage:
# add_expense("2026-01-15", "food", 25.50, "Lunch at cafe")
# print(filter_by_category("food"))
# print(f"Total spent: ${calculate_total()}")
