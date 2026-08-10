"""20.	Create a list of books.
Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books
"""
books = ["Python", "Java", "C++", "HTML"]

new_book = input("Enter new book: ")
books.append(new_book)

search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("All books:", books)
print("Total books:", len(books))