# 27. Create a dictionary containing product names and quantities. Perform add a product, update quantity, delete a product, search for a product, and display products with quantity below 10.

products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15,
    "Pencil": 8
}

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Products Below 10")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity

    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print("Quantity:", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, ":", quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice")