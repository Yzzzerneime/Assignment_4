import sys
import os

# Добавляем корневую папку проекта в sys.path, чтобы можно было импортировать app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.db import engine, SessionLocal, Base
from app.db import models
from app.db.crud import create_category, create_book

def init_db():
    # Создаём таблицы если их нет
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Проверяем, есть ли уже категории
    if db.query(models.Category).count() == 0:
        # Добавляем категории
        cat1 = create_category(db, "Художественная литература")
        cat2 = create_category(db, "Научно-популярная")
        cat3 = create_category(db, "Программирование")

        # Добавляем книги
        create_book(db,
                    title="Мастер и Маргарита",
                    description="Роман Михаила Булгакова",
                    price=450.0,
                    category_id=cat1.id,
                    url="http://example.com/master")
        create_book(db,
                    title="Преступление и наказание",
                    description="Роман Фёдора Достоевского",
                    price=500.0,
                    category_id=cat1.id,
                    url="http://example.com/crime")
        create_book(db,
                    title="Краткая история времени",
                    description="Стивен Хокинг о Вселенной",
                    price=650.0,
                    category_id=cat2.id,
                    url="http://example.com/time")
        create_book(db,
                    title="Сознание и мозг",
                    description="Как мозг кодирует мысли",
                    price=720.0,
                    category_id=cat2.id,
                    url="http://example.com/brain")
        create_book(db,
                    title="Чистый код",
                    description="Роберт Мартин о программировании",
                    price=890.0,
                    category_id=cat3.id,
                    url="http://example.com/clean")
        create_book(db,
                    title="Изучаем Python",
                    description="Марк Лутц, классика",
                    price=1200.0,
                    category_id=cat3.id,
                    url="http://example.com/python")
        create_book(db,
                    title="Структуры данных и алгоритмы",
                    description="Адитья Бхаргава",
                    price=950.0,
                    category_id=cat3.id,
                    url="http://example.com/algorithms")
        print("База данных инициализирована с тестовыми данными.")
    else:
        print("В базе уже есть данные. Ничего не добавлено.")

    db.close()

if __name__ == "__main__":
    init_db()
