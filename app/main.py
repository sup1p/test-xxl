from fastapi import FastAPI
from .core.database import Base, engine
from .core.logger import setup_logging
import logging

from .routers import furniture, order


setup_logging()
app = FastAPI()


@app.get("/")
async def root():
    logging.info("Root accessed")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    logging.info("Hello %s", name)
    return {"message": f"Hello {name}"}

app.include_router(furniture.router)
app.include_router(order.router)


