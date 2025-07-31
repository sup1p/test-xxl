from fastapi import Depends, Query, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models import Furniture
from ..schemas import CreateFurnitureSchema
from typing import Optional
from dotenv import load_dotenv
import logging
load_dotenv()

router = APIRouter()

@router.get("/furniture", tags=["Furniture"])
def get_all_furniture(category: Optional[str] = Query(None),db: Session = Depends(get_db)):
    logging.info("/furniture route accessed")

    if category is None:
        furnitures = db.query(Furniture).all()
        logging.info(f"/furniture - got furnitures without categories")

    else:
        logging.info(f"/furniture - getting with category: {category}")
        furnitures = db.query(Furniture).filter(Furniture.category == category).all()
        if furnitures is None or len(furnitures) == 0:
            logging.info(f"/furniture - no furnitures for category: {category}")
            raise HTTPException(
                status_code=404,
                detail="No furnitures found"
            )

    if furnitures is None or len(furnitures) == 0:
        logging.info("/furniture - no furnitures found")
        raise HTTPException(
            status_code=404,
            detail="No furnitures in DB"
        )

    logging.info("/furniture - returning all furnitures")
    return furnitures

@router.get("/furniture/{furniture_id}", tags=["Furniture"])
def get_furniture(furniture_id: int,db: Session = Depends(get_db)):
    logging.info(f"/furniture/id route accessed with id:{furniture_id}")
    furniture = db.query(Furniture).filter(Furniture.id == furniture_id).first()

    if furniture is None:
        logging.info(f"/furniture/id - no furniture found with ID: {furniture_id}")
        raise HTTPException(
            status_code=404,
            detail=f"Furniture with ID: {furniture_id} not found"
        )

    logging.info(f"/furniture/id - returning furniture with ID: {furniture_id}")
    return furniture

@router.post("/furniture/add", tags=["Furniture"])
def add_furniture(data: CreateFurnitureSchema, db: Session = Depends(get_db)):
    logging.info("/furniture/add - route accessed")
    logging.info(f"/furniture/add - creating furniture with name:{data.name}, price:{data.price}, category: {data.category}")
    new_furniture = Furniture(name = data.name, price = data.price, category = data.category)

    db.add(new_furniture)
    db.commit()
    db.refresh(new_furniture)

    logging.info(f"/furniture/add - created new furniture with name:{data.name}")
    return new_furniture