from fastapi import Depends, HTTPException, APIRouter
from pydantic import EmailStr
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..models import Furniture, Order, OrderElements
from ..schemas import MakeOrderSchema
from ..core.dependencies import send_order_detail_email
from ..core.logger import setup_logging

from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

setup_logging()
router = APIRouter()


@router.get("/orders", tags=["Orders"])
def get_orders(email: EmailStr, db: Session = Depends(get_db)):
    logging.info(f"GET - /orders - accessed with email:{email}")

    orders = db.query(Order).filter(Order.client_email == email).all()

    if orders is None or len(orders) == 0:
        logging.info(f"No orders found for email:{email}")
        raise HTTPException(
            status_code=404,
            detail=f"Orders with email: {email} not found"
        )

    logging.info(f"GET - /orders - returning {len(orders)} orders")
    return orders


@router.post("/orders", tags=["Orders"])
async def create_order(data: MakeOrderSchema, db: Session = Depends(get_db)):
    logging.info(f"POST - /orders - accessed with email:{data.email}")

    furniture_items = db.query(Furniture).filter(Furniture.id.in_(data.furniture_ids)).all()

    found_ids = {f.id for f in furniture_items}
    missing_ids = set(data.furniture_ids) - found_ids

    if missing_ids:
        logging.info(f"POST - /orders - Missing furniture ids: {missing_ids}")
        raise HTTPException(
            status_code=404,
            detail=f"Furniture IDs not found: {list(missing_ids)}"
        )

    total_price = sum(f.price for f in furniture_items)

    order = Order(
        client_email=data.email,
        full_price=total_price,
        created_at=datetime.utcnow()
    )
    db.add(order)
    db.flush()

    logging.info(f"POST - /orders - created order with email:{data.email}, price:{total_price}")

    order_elements = []

    for f in furniture_items:
        elem = OrderElements(order_id=order.id, furniture_id=f.id)
        order_elements.append(elem)

    db.add_all(order_elements)
    db.commit()
    db.refresh(order)

    await send_order_detail_email(str(data.email), data.furniture_ids, total_price, db)
    logging.info(f"POST - /orders - sent order detail to:{data.email}")

    logging.info(f"POST - /orders - returning {len(order_elements)} orders to user:{data.email}")
    return {
        "order_id": order.id,
        "total_price": total_price,
        "items": [{"id": f.id, "name": f.name, "price": f.price} for f in furniture_items]
    }