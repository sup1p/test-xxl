from typing import List

from pydantic import BaseModel, EmailStr

class CreateFurnitureSchema(BaseModel):
    name: str
    price: float
    category: str


class GetFurnitureSchema(BaseModel):
    id: int
    name: str
    price: float
    category: str

class MakeOrderSchema(BaseModel):
    email: EmailStr
    furniture_ids : List[int]