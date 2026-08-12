# 29. Create a dictionary containing book IDs and book names. Implement add a book, search a book, remove a book, display all books, and count total books.

books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Remove Book")
    print("4. Display All Books")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found")

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")

    elif choice == 4:
        for book_id, name in books.items():
            print(book_id, ":", name)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")