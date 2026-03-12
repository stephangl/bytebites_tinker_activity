# ByteBites UML Class Diagram

+-----------------------------+
|          Customer           |
+-----------------------------+
| - name: String              |
| - purchaseHistory: List     |
+-----------------------------+
| + verifyUser(): Boolean     |
+-----------------------------+

+-----------------------------+
|          FoodItem           |
+-----------------------------+
| - name: String              |
| - price: Float              |
| - category: String          |
| - popularityRating: Float   |
+-----------------------------+

+-----------------------------+
|            Menu             |
+-----------------------------+
| - items: List<FoodItem>     |
+-----------------------------+
| + filterByCategory(): List  |
| + getAllItems(): List        |
+-----------------------------+

+-----------------------------+
|         Transaction         |
+-----------------------------+
| - selectedItems: List       |
| - totalCost: Float          |
+-----------------------------+
| + computeTotal(): Float     |
+-----------------------------+

## Relationships

Customer  "1"    -->  "0..*"  Transaction  (a customer has many transactions)
Menu      "1"    o->  "0..*"  FoodItem     (menu aggregates food items)
Transaction "1"  -->  "1..*"  FoodItem     (a transaction contains one or more items)

## Class Summary

- **Customer** — represents a verified user identified by name with a history of past purchases.
- **FoodItem** — a sellable product with a name, price, category, and popularity rating.
- **Menu** — the full catalogue of FoodItems, supporting filtering by category (e.g. "Drinks", "Desserts").
- **Transaction** — groups one or more selected FoodItems into a single order and computes the total cost.