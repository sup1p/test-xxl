from sqlalchemy import String, Integer, Column, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .core.database import Base

class Furniture(Base):
    __tablename__ = 'furniture'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)

    order_elements = relationship('OrderElements', back_populates='furniture', cascade='all, delete-orphan')

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    client_email = Column(String)

    full_price = Column(Float)
    created_at = Column(DateTime)

    order_elements = relationship('OrderElements', back_populates='order', cascade='all, delete-orphan')

class OrderElements(Base):
    __tablename__ = 'order_elements'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    furniture_id = Column(Integer, ForeignKey('furniture.id'))

    order = relationship('Order', back_populates='order_elements')
    furniture = relationship('Furniture', back_populates='order_elements')