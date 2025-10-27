"""
Inventory Management System
----------------------------
This module provides basic inventory operations such as adding, removing,
loading, and saving stock data. It also checks for low stock and prints data.
"""

import json  # Removed unused 'logging' import

# Global stock data (used minimally)
stock_data = {}


def add_item(item_name, quantity=None):
    """Add a new item to the inventory."""
    if quantity is None:
        quantity = []
    stock_data[item_name] = quantity
    print(f"Added {item_name} with quantity {quantity}")


def remove_item(item_name):
    """Remove an existing item from the inventory."""
    try:
        del stock_data[item_name]
        print(f"Removed {item_name} from inventory")
    except KeyError as e:
        print(f"Error: Item '{item_name}' not found. ({e})")


def get_qty(item_name):
    """Return the quantity of a specific item."""
    return stock_data.get(item_name, 0)


def load_data(filename):
    """Load inventory data from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        stock_data.update(data)
        print("Inventory data loaded successfully.")
    except FileNotFoundError as e:
        print(f"Error: File '{filename}' not found. ({e})")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON data. ({e})")


def save_data(filename):
    """Save inventory data to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        print("Inventory data saved successfully.")
    except OSError as e:
        print(f"Error writing to file: {e}")


def print_data():
    """Print all items and their quantities."""
    for item, qty in stock_data.items():
        print(f"{item}: {qty}")


def check_low_items(threshold):
    """Check for items with quantity below the given threshold."""
    low_items = [item for item, qty in stock_data.items() if qty < threshold]
    if low_items:
        print(f"Low stock items: {low_items}")
    else:
        print("No low stock items.")


def main():
    """Main function to test inventory operations."""
    add_item("Apples", 20)
    add_item("Bananas", 5)
    remove_item("Grapes")
    print_data()
    check_low_items(10)
    save_data("inventory.json")
    load_data("inventory.json")
    print_data()


if __name__ == "__main__":
    main()
