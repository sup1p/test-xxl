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

```
git clone https://github.com/sup1p/test-xxl.git
cd test-xxl
cp .env.example .env
docker-compose up --build
```

```
├── app/ # код приложения
│ ├── main.py # точка входа
│ ├── routers/ # роутеры FastAPI
│ ├── core/ # конфигурации (настройка БД и др.)
│ ├── schemas/ # Pydantic-схемы (DTO)
│ └── models  # SQLAlchemy-модели
│
├── alembic/ # миграции Alembic
├── Dockerfile # Docker-образ приложения
├── docker-compose.yml # конфигурация Docker-сервисов
├── .env.example # пример переменных окружения
└── requirements.txt # зависимости проекта
```

# создать миграцию
alembic revision --autogenerate -m "msg"

# применить
alembic upgrade head

Если есть проблемы с алембиком то следует сначало сделать "alembic downgrade base"

# Swagger 
по пути localhost:8002/docs

# SMTP
Для отправки email требуется заполнить данные описанные в .env.example и подключение к интернету