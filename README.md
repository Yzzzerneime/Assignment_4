1. Клонирование репозитория

git clone 
cd ./Assignment_4

2. Создание и активация виртуального окружения

python -m venv venv
source venv/bin/activate

3. Установка зависимостей

pip install -r requirements.txt

Файл requirements.txt должен содержать:

SQLAlchemy
psycopg2-binary
python-dotenv
fastapi
uvicorn

4. Настройка окружения

Убедитесь, что в PostgreSQL уже создан пользователь octagon и база данных octagon_db:
sql

CREATE USER octagon WITH PASSWORD '12345';
CREATE DATABASE octagon_db OWNER octagon;

5. Инициализация базы данных

При первом запуске необходимо создать таблицы и наполнить их начальными данными. Для этого выполните:

python -m app.init_db

6. Запуск API-сервера

Из корня проекта выполните:

uvicorn app.main:app --reload

После запуска сервер будет доступен по адресу:
http://127.0.0.1:8000