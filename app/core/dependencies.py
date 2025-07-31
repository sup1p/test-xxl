from typing import List
from sqlalchemy.orm import Session

from aiosmtplib import send
from email.message import EmailMessage
import os
from dotenv import load_dotenv

from ..models import Furniture



load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_PORT = os.getenv("SMTP_PORT")


async def send_order_detail_email(email: str, furnitures: List[int], price: int, db: Session):

    furniture_items = db.query(Furniture).filter(Furniture.id.in_(furnitures)).all()


    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = email
    message["Subject"] = "Покупка товара на сайте ТЕСТ"
    message.set_content(
        f"Здравствуйте!\n\nВот ваш заказ с сайта ТЕСТ: \n\n {furniture_items} \n\nОбщая сумма: {price}"
    )

    await send(
        message,
        hostname=SMTP_HOST,
        port=SMTP_PORT,
        username=SMTP_USER,
        password=SMTP_PASS,
        start_tls=True,
    )