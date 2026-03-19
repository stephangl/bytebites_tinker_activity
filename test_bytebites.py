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