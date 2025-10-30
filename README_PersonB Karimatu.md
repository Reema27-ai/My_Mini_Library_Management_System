# Mini Library Management System — Quick Guide
**Prepared for:** Person B (Casual)
**Generated on:** 2025-10-29 17:38 UTC

## TL;DR
A tiny, functional library system written in Python. Manage books, members, and who has borrowed what no DB drama, just in-memory structures and straightforward logic. Perfect for demos or rapid prototypes.

## What's inside
- `operations.py`  brains of the app (add/update/delete, borrow/return, search, auth).
- `Demo.py`  friendly CLI for Admin / Staff / Student actions.
- `tests.py`  quick assert tests to check main flows.

## Quick start
``bash
python Demo.py   # run the interactive demo
python tests.py  # run the simple tests
```

## Highlights
- Role-based access (Admin / Staff / Student).
- Borrow limit: 3 books for 7 days (easy to change in operations.py).
- Prevents deleting resources that are currently borrowed.
- Works offline: no external services required.

## Tips for Person B
- Want a web UI? The logic is modular plugging in Flask or FastAPI is straightforward.
- Want persistence? Replace the in-memory dicts and lists with a SQLite or PostgreSQL backend.

