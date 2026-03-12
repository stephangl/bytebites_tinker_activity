+---------------------------+
|         Customer          |
+---------------------------+
| - name: String            |
| - purchaseHistory: List   |
+---------------------------+
|                           |
+---------------------------+

+---------------------------+
|         FoodItem          |
+---------------------------+
| - name: String            |
| - price: Float            |
| - category: String        |
| - popularityRating: Float |
+---------------------------+
|                           |
+---------------------------+

+---------------------------+
|           Menu            |
+---------------------------+
| - items: List<FoodItem>   |
+---------------------------+
| + filterByCategory()      |
+---------------------------+

+---------------------------+
|       Transaction         |
+---------------------------+
| - selectedItems: List     |
| - totalCost: Float        |
+---------------------------+
| + computeTotal()          |
+---------------------------+

Relationships:
Customer "1" --> "0..*" Transaction
Menu "1" o--> "0..*" FoodItem
Transaction "1" --> "1..*" FoodItem

---

- Customer — represents a verified user, storing their name and past purchases. 
- FoodItem — represents a sellable product with name, price, category, and popularity rating. 
- Menu — a digital collection of all FoodItems that supports filtering by category (e.g. "Drinks", "Desserts"). 
- Transaction — groups a customer's selected items into one order and computes the total cost.
