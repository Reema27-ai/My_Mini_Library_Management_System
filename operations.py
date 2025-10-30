# operations.py

# Tuple for valid genres
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Crime", "Horror")

# Dictionary to store books
books = {}

# List to store members
members = []

# Add Book
def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists!"
    if genre not in GENRES:
        return "Invalid genre!"
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully!"

# Add Member
def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists!"
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return "Member added successfully!"

# Search Book
def search_books(keyword):
    results = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            results.append({isbn: info})
    return results

# Update Book
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found!"
    if genre and genre not in GENRES:
        return "Invalid genre!"
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies:
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] = total_copies
    return "Book updated successfully!"

# Delete Book
def delete_book(isbn):
    if isbn not in books:
        return "Book not found!"
    for m in members:
        if isbn in m["borrowed_books"]:
            return "Cannot delete, book is borrowed!"
    del books[isbn]
    return "Book deleted successfully!"

# Borrow Book
def borrow_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found!"
    if isbn not in books:
        return "Book not found!"
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached!"
    if books[isbn]["available_copies"] <= 0:
        return "No copies left!"

    member["borrowed_books"].append(isbn)
    books[isbn]["available_copies"] -= 1
    return "Book borrowed successfully!"

# Return Book
def return_book(member_id, isbn):
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member or isbn not in member["borrowed_books"]:
        return "Invalid return!"
    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return "Book returned successfully!"



