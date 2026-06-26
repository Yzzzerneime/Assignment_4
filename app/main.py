import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books
from app.db.models import Category, Book

def print_books_and_categories():
    db = SessionLocal()
    categories = get_categories(db)
    print("|Категории|")
    for cat in categories:
        print(f"ID: {cat.id}, Название: {cat.title}")

    print("\n|Книги|")
    books = get_books(db)
    for book in books:
        print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, "
              f"Категория: {book.category.title if book.category else '—'}")

    print("\n|Детальная информация по категориям|")
    for cat in categories:
        print(f"Категория: {cat.title}")
        for book in cat.books:
            print(f"  - {book.title} ({book.price} руб.)")
        print()

    db.close()

if __name__ == "__main__":
    print_books_and_categories()
