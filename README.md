# OmarTest

Проект на FastAPI + PostgreSQL, с Alembic, SQLAlchemy и Docker.

## Стек

- FastAPI
- PostgreSQL (через asyncpg)
- SQLAlchemy (async)
- Alembic (миграции)
- Docker / docker-compose
- Pydantic

##  Быстрый старт

```bash
git clone https://github.com/sup1p/test-xxl.git
cd test-xxl
cp .env.example .env
docker-compose up --build
```

##  Структура проекта

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

##  Управление миграциями

```bash
# создать миграцию
alembic revision --autogenerate -m "msg"

# применить миграции
alembic upgrade head
```

##  API Документация

### Swagger UI
Доступен по адресу: `http://localhost:8002/docs`

##  API Эндпоинты

### Основные эндпоинты

#### `GET /`
- **Описание**: Корневой эндпоинт
- **Ответ**: `{"message": "Hello World"}`

#### `GET /hello/{name}`
- **Описание**: Приветствие с именем
- **Параметры**: `name` (string) - имя для приветствия
- **Пример**: `GET /hello/John`
- **Ответ**: `{"message": "Hello John"}`

### Управление мебелью (Furniture)

#### `GET /furniture`
- **Описание**: Получить весь список мебели или отфильтровать по категории
- **Параметры**: 
  - `category` (optional, string) - категория для фильтрации
- **Примеры**:
  - `GET /furniture` - получить всю мебель
  - `GET /furniture?category=chair` - получить мебель категории "chair"
- **Ответ**: Массив объектов мебели
- **Ошибки**: 404 - если мебель не найдена

#### `GET /furniture/{furniture_id}`
- **Описание**: Получить конкретную мебель по ID
- **Параметры**: `furniture_id` (integer) - ID мебели
- **Пример**: `GET /furniture/1`
- **Ответ**: Объект мебели
- **Ошибки**: 404 - если мебель с указанным ID не найдена

#### `POST /furniture/add`
- **Описание**: Добавить новую мебель
- **Тело запроса**:
  ```json
  {
    "name": "Стул офисный",
    "price": 1500.0,
    "category": "chair"
  }
  ```
- **Ответ**: Созданный объект мебели с ID
- **Пример**: 
  ```bash
  curl -X POST "http://localhost:8002/furniture/add" \
       -H "Content-Type: application/json" \
       -d '{"name": "Стол письменный", "price": 5000.0, "category": "table"}'
  ```

###  Управление заказами (Orders)

#### `GET /orders`
- **Описание**: Получить все заказы пользователя по email
- **Параметры**: `email` (EmailStr) - email клиента
- **Пример**: `GET /orders?email=user@example.com`
- **Ответ**: Массив заказов пользователя
- **Ошибки**: 404 - если заказы не найдены

#### `POST /orders`
- **Описание**: Создать новый заказ
- **Тело запроса**:
  ```json
  {
    "email": "user@example.com",
    "furniture_ids": [1, 2, 3]
  }
  ```
- **Ответ**:
  ```json
  {
    "order_id": 1,
    "total_price": 8000.0,
    "items": [
      {"id": 1, "name": "Стул", "price": 1500.0},
      {"id": 2, "name": "Стол", "price": 5000.0},
      {"id": 3, "name": "Лампа", "price": 1500.0}
    ]
  }
  ```
- **Функциональность**:
  - Автоматически рассчитывает общую стоимость
  - Проверяет существование всех товаров
  - Отправляет email с деталями заказа
  - Создает связи между заказом и товарами
- **Ошибки**: 404 - если указанные ID мебели не найдены

##  Email функциональность

Для отправки email требуется:
1. Заполнить данные SMTP в `.env.example`
2. Подключение к интернету
3. Корректные настройки SMTP сервера

Email отправляется автоматически при создании заказа с деталями заказа.

##  Docker

Проект полностью контейнеризирован с помощью Docker Compose:

```bash
# Запуск всех сервисов
docker-compose up --build

# Запуск в фоновом режиме
docker-compose up -d

# Остановка сервисов
docker-compose down
```

##  Логирование

Все API запросы логируются с помощью встроенного логгера FastAPI. Логи включают:
- HTTP метод и путь
- Параметры запроса
- Результат выполнения

##  Docker Compose особенности

В `docker-compose.yml` настроена задержка в 5 секунд после инициализации базы данных. Это гарантирует, что бэкенд запустится только после полной инициализации PostgreSQL, а не с полуинициализированной базой данных.
