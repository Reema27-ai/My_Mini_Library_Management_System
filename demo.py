
from operations import *

print("=== Library Management System Demo ===")

# Add Books
print(add_book("001", "Atomic Habits", "James Clear", "Non-Fiction", 4))
print(add_book("002", "Harry Potter", "J.K. Rowling", "Fiction", 3))

# Add Members
print(add_member("M001", "Kareema", "kareema@email.com"))
print(add_member("M002", "Halima", "halima@email.com"))

# Borrow Book
print(borrow_book("M001", "001"))
print(borrow_book("M001", "002"))

# Return Book
print(return_book("M001", "001"))

# Search Book
print("Search Results:", search_books("Harry"))

# Update Book
print(update_book("002", title="Harry Potter and the Goblet of Fire"))

# Delete Book
print(delete_book("001"))

print("=== Demo Complete ===")
