
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

    def get_items(self):
        return self.items

    def filter_by_category(self, category):
        return [item for item in self.items if item.get_category().lower() == category.lower()]

    def __repr__(self):
        return f"Menu(items={len(self.items)})"


class Transaction:
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Transaction requires a Customer instance.")
        self.customer = customer
        self.items = []

    def add_item(self, food_item):
        if not isinstance(food_item, FoodItem):
            raise TypeError("Transaction only accepts FoodItem instances.")
        self.items.append(food_item)

    def get_items(self):
        return self.items

    def compute_total(self):
        if not self.items:
            raise ValueError("Transaction must contain at least one FoodItem.")
        return sum(item.get_price() for item in self.items)

    def __repr__(self):
        return f"Transaction(customer={self.customer.get_name()!r}, total={self.compute_total()}, items={len(self.items)})"
