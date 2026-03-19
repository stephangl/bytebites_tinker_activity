
# Customer — represents a verified user identified by name with a history of past purchases.
# FoodItem — a sellable product with a name, price, category, and popularity rating.
# Menu — the full catalogue of FoodItems, supporting filtering by category (e.g. "Drinks", "Desserts").
# Transaction — groups one or more selected FoodItems into a single order and computes the total cost.

class FoodItem:
    def __init__(self, name, price, category, popularityRating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularityRating

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def get_popularity_rating(self):
        return self.popularity_rating

    def __repr__(self):
        return f"FoodItem(name={self.name!r}, price={self.price}, category={self.category!r}, popularity_rating={self.popularity_rating})"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def get_name(self):
        return self.name

    def get_purchase_history(self):
        return self.purchase_history

    def verify_user(self):
        return bool(self.name)

    def add_to_history(self, transaction):
        self.purchase_history.append(transaction)

    def __repr__(self):
        return f"Customer(name={self.name!r}, purchases={len(self.purchase_history)})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        if not isinstance(food_item, FoodItem):
            raise TypeError("Menu only accepts FoodItem instances.")
        self.items.append(food_item)

    def get_all_items(self):
        return self.items

    def filter_by_category(self, category):
        return [item for item in self.items if item.get_category().lower() == category.lower()]

    def __repr__(self):
        return f"Menu(items={len(self.items)})"


class Transaction:
    def __init__(self):
        self.selected_items = []
        self.total_cost = 0.0

    def add_item(self, food_item):
        if not isinstance(food_item, FoodItem):
            raise TypeError("Transaction only accepts FoodItem instances.")
        self.selected_items.append(food_item)

    def get_items(self):
        return self.selected_items

    def compute_total(self):
        if not self.selected_items:
            raise ValueError("Transaction must contain at least one FoodItem.")
        self.total_cost = sum(item.get_price() for item in self.selected_items)
        return self.total_cost

    def __repr__(self):
        return f"Transaction(total={self.total_cost}, items={len(self.selected_items)})"


# --- Scenario ---

# Build menu
menu = Menu()
menu.add_item(FoodItem("Spicy Burger", 9.99, "Mains", 4.7))
menu.add_item(FoodItem("Veggie Wrap", 7.49, "Mains", 3.9))
menu.add_item(FoodItem("Large Soda", 2.50, "Drinks", 3.5))
menu.add_item(FoodItem("Iced Tea", 2.00, "Drinks", 4.1))
menu.add_item(FoodItem("Chocolate Cake", 5.00, "Desserts", 4.9))

# All items sorted by price
print("=== Menu by Price ===")
for item in sorted(menu.get_all_items(), key=lambda i: i.get_price()):
    print(f"  {item.get_name():<20} ${item.get_price():.2f}")

# Filter by category
print("\n=== Drinks ===")
for item in menu.filter_by_category("drinks"):
    print(f"  {item.get_name()} (popularity: {item.get_popularity_rating()})")

# Verify customer
customer = Customer("Alice")
print(f"\n=== Customer ===")
print(f"  {customer.get_name()} — verified: {customer.verify_user()}")

# Build and compute transaction
order = Transaction()
order.add_item(menu.filter_by_category("mains")[0])   # Spicy Burger
order.add_item(menu.filter_by_category("drinks")[1])  # Iced Tea
order.add_item(menu.filter_by_category("desserts")[0])  # Chocolate Cake

print("\n=== Order ===")
for item in order.get_items():
    print(f"  {item.get_name():<20} ${item.get_price():.2f}")
print(f"  {'TOTAL':<20} ${order.compute_total():.2f}")

# Record in customer history
customer.add_to_history(order)
print(f"\n=== Purchase History ===")
print(f"  {customer.get_name()} has {len(customer.get_purchase_history())} order(s) on record.")
