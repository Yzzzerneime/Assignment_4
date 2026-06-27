from fastapi import FastAPI
from app.api import books, categories
from app.db.db import engine, Base

# Создаем таблицы при старте (если еще нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(books.router)
app.include_router(categories.router)


@app.get("/health")
def health_check():
    # Проверка работоспособности сервиса
    return {"status": "ok", "message": "Сервис работает"}
