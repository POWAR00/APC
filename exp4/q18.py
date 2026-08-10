"""18.	Create a shopping cart using a list.
Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items
"""
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

cart.remove("Mouse")

item = "Keyboard"

if item in cart:
    print("Item found:", item)
else:
    print("Item not found")

print("Cart:", cart)
print("Total items:", len(cart))