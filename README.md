# OmarTest

Проект на FastAPI + PostgreSQL, с Alembic, асинхронным SQLAlchemy и Docker.

## 📦 Стек

- FastAPI
- PostgreSQL (через asyncpg)
- SQLAlchemy (async)
- Alembic (миграции)
- Docker / docker-compose
- Pydantic

## 🚀 Быстрый старт


git clone https://github.com/sup1p/test-xxl.git
cd test-xxl
cp .env.example .env
docker-compose up --build

.
├── app/              # код приложения
│   ├── main.py       # вход
│   ├── models/       # SQLAlchemy модели
│   ├── schemas/      # Pydantic DTO
│   ├── api/          # роутеры
│   └── services/     # бизнес-логика
│
├── alembic/          # миграции
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── requirements.txt

# создать миграцию
alembic revision --autogenerate -m "msg"

# применить
alembic upgrade head

Если есть проблемы с алембиком то следует сначало сделать "alembic downgrade base"