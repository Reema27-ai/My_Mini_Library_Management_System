# Mini Library Management System
Prepared by: Karimatu



A tiny, functional library system written in Python. Manage books, members, and who has borrowed what no DB drama, just in-memory structures and straightforward logic. Perfect for demos or rapid prototypes.


- `operations.py`  brains of the app (add/update/delete, borrow/return, search, auth).
- `Demo.py`  friendly CLI for Admin / Staff / Student actions.
- `tests.py`  quick assert tests to check main flows.


``bash
python Demo.py   # run the interactive demo
python tests.py  # run the simple tests


 Highlights
- Role-based access (Admin / Staff / Student).
- Borrow limit: 3 books for 7 days (easy to change in operations.py).
- Prevents deleting resources that are currently borrowed.
- Works offline: no external services required.

 Person B
 The logic is modular plugging in Flask or FastAPI is straightforward.
 Replace the in-memory dicts and lists with a SQLite or PostgreSQL backend.

