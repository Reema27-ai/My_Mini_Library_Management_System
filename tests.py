
from operations import *

def run_tests():
    print("=== Running Tests ===")
    result1 = add_book("001", "Atomic Habits", "James Clear", "Non-Fiction", 2)
    assert result1 == "Book added successfully!", "Test 1 Failed: Add Book"

    result2 = add_member("M001", "Kareema", "kareema@email.com")
    assert result2 == "Member added successfully!", "Test 2 Failed: Add Member"

    result3 = borrow_book("M001", "001")
    assert result3 == "Book borrowed successfully!", "Test 3 Failed: Borrow Book"

    borrow_book("M001", "001")  # borrow last copy
    result4 = borrow_book("M001", "001")
    assert result4 in ["No copies left!", "Borrow limit reached!"], "Test 4 Failed: Borrow When No Copies Left"

    result5 = return_book("M001", "001")
    assert result5 == "Book returned successfully!", "Test 5 Failed: Return Book"

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()

