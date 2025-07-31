# OmarTest

Проект на FastAPI + PostgreSQL, с Alembic, SQLAlchemy и Docker.

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
│   ├── routers/       # routers
│   ├── core/        #configuration: db settings and etc 
│   ├── schemas      # Pydantic DTO
│   └── models    # db-models
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

Swagger по пути localhost:8002/docs

Для отправки email требуется заполнить данные описанные в .env.example и подключение к интернету