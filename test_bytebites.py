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


import unittest


class TestTotalCalculation(unittest.TestCase):

    def test_calculate_total_with_multiple_items(self):
        # A $10 burger and $5 soda should total $15
        order = Transaction()
        order.add_item(FoodItem("Burger", 10.00, "Mains", 4.0))
        order.add_item(FoodItem("Soda", 5.00, "Drinks", 3.0))
        self.assertEqual(order.compute_total(), 15.00)

    def test_calculate_total_with_single_item(self):
        # A single item transaction should return that item's price
        order = Transaction()
        order.add_item(FoodItem("Cake", 6.50, "Desserts", 4.5))
        self.assertEqual(order.compute_total(), 6.50)

    def test_order_total_is_zero_when_empty(self):
        # An empty transaction should raise an error, not silently return 0
        order = Transaction()
        with self.assertRaises(ValueError):
            order.compute_total()

    def test_total_cost_stored_after_compute(self):
        # total_cost attribute should reflect the computed value after calling compute_total
        order = Transaction()
        order.add_item(FoodItem("Wrap", 7.00, "Mains", 3.8))
        order.compute_total()
        self.assertEqual(order.total_cost, 7.00)

    def test_order_total_sums_all_item_prices(self):
        # Total must reflect every item in the order, not just the first or last
        order = Transaction()
        order.add_item(FoodItem("Spicy Burger", 9.99, "Mains", 4.7))
        order.add_item(FoodItem("Iced Tea", 2.00, "Drinks", 4.1))
        order.add_item(FoodItem("Chocolate Cake", 5.00, "Desserts", 4.9))
        self.assertAlmostEqual(order.compute_total(), 16.99, places=2)

    def test_empty_transaction_raises_value_error(self):
        # Computing the total of a transaction with no items must raise a ValueError
        order = Transaction()
        with self.assertRaises(ValueError):
            order.compute_total()


class TestCategoryFiltering(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.menu.add_item(FoodItem("Cola", 2.50, "Drinks", 3.5))
        self.menu.add_item(FoodItem("Burger", 9.99, "Mains", 4.7))
        self.menu.add_item(FoodItem("Cake", 5.00, "Desserts", 4.9))

    def test_filter_by_category_returns_only_matching_items(self):
        # Filtering "Drinks" should return only drink items
        results = self.menu.filter_by_category("Drinks")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get_name(), "Cola")

    def test_filter_by_category_is_case_insensitive(self):
        # "drinks", "DRINKS", and "Drinks" should all return the same result
        self.assertEqual(
            self.menu.filter_by_category("drinks"),
            self.menu.filter_by_category("DRINKS")
        )

    def test_filter_returns_empty_for_unknown_category(self):
        # A category with no items should return an empty list, not raise an error
        results = self.menu.filter_by_category("Sushi")
        self.assertEqual(results, [])

    def test_filter_excludes_items_from_other_categories(self):
        # Filtering "Desserts" must not return items from Drinks or Mains
        results = self.menu.filter_by_category("Desserts")
        categories = [item.get_category() for item in results]
        self.assertTrue(all(c == "Desserts" for c in categories))

    def test_filter_returns_all_items_in_matching_category(self):
        # When multiple items share a category, all of them should be returned
        self.menu.add_item(FoodItem("Lemonade", 3.00, "Drinks", 4.0))
        results = self.menu.filter_by_category("Drinks")
        self.assertEqual(len(results), 2)


class TestMenuSorting(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.menu.add_item(FoodItem("Cake", 5.00, "Desserts", 4.9))
        self.menu.add_item(FoodItem("Cola", 2.50, "Drinks", 3.5))
        self.menu.add_item(FoodItem("Burger", 9.99, "Mains", 4.7))

    def test_menu_sorted_by_price_ascending(self):
        # Items sorted by price should go from cheapest to most expensive
        sorted_items = sorted(self.menu.get_all_items(), key=lambda i: i.get_price())
        prices = [item.get_price() for item in sorted_items]
        self.assertEqual(prices, [2.50, 5.00, 9.99])

    def test_menu_sorted_by_popularity_descending(self):
        # Items sorted by popularity should go from highest to lowest rating
        sorted_items = sorted(self.menu.get_all_items(), key=lambda i: i.get_popularity_rating(), reverse=True)
        ratings = [item.get_popularity_rating() for item in sorted_items]
        self.assertEqual(ratings, [4.9, 4.7, 3.5])


class TestCustomer(unittest.TestCase):

    def test_verify_user_returns_true_for_named_customer(self):
        # A customer with a name should be verified
        customer = Customer("Alice")
        self.assertTrue(customer.verify_user())

    def test_purchase_history_records_transaction(self):
        # After adding a transaction to history, it should appear in purchase history
        customer = Customer("Alice")
        order = Transaction()
        order.add_item(FoodItem("Burger", 9.99, "Mains", 4.7))
        customer.add_to_history(order)
        self.assertEqual(len(customer.get_purchase_history()), 1)


class TestTypeGuards(unittest.TestCase):

    def test_menu_rejects_non_food_item(self):
        # Adding a non-FoodItem to Menu should raise a TypeError
        menu = Menu()
        with self.assertRaises(TypeError):
            menu.add_item("not a food item")

    def test_transaction_rejects_non_food_item(self):
        # Adding a non-FoodItem to Transaction should raise a TypeError
        order = Transaction()
        with self.assertRaises(TypeError):
            order.add_item(42)


if __name__ == "__main__":
    unittest.main()