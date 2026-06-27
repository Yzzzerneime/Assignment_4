from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=list[BookResponse])
def get_books(
    skip: int = 0,
    limit: int = 100,
    category_id: int | None = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    # Получить список книг с возможностью фильтрации по категории
    if category_id is not None:
        books = crud.get_books_by_category(db, category_id)
    else:
        books = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    # Получить книгу по ID
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Создать новую книгу
    # Проверяем, существует ли категория
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Указанная категория не существует")
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url or ""
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    # Обновить книгу
    # Если меняется категория — проверяем ее существование
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=400, detail="Указанная категория не существует")
    
    # Обновляем только переданные поля
    update_data = book.model_dump(exclude_unset=True)
    updated = crud.update_book(db, book_id, **update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return updated


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    # Удалить книгу
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return
