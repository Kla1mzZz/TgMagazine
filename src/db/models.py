from sqlalchemy import Column, Integer, String

from .database import Base


class Brands(Base):
    __tablename__ = 'brands'

    id = Column(Integer,primary_key=True)
    brandName = Column(String)

class Items(Base):
    __tablename__ = 'Items'

    id = Column(Integer,primary_key=True)
    item = Column(String)
    brand = Column(String)
    modelName = Column(String)
    size = Column(String)
    price = Column(String)
    photo = Column(String)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer,primary_key=True)
    item = Column(String)
    brand = Column(String)
    modelName = Column(String)
    size = Column(String)
    price = Column(String)
    photo = Column(String)
    fullName = Column(String)
    phoneNumber = Column(String)
    address = Column(String)
    username = Column(String)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)

class VereficationOrder(Base):
    __tablename__ = 'verification_order'

    id = Column(Integer,primary_key=True)
    item = Column(String)
    brand = Column(String)
    modelName = Column(String)
    size = Column(String)
    price = Column(String)
    photo = Column(String)
    fullName = Column(String)
    phoneNumber = Column(String)
    address = Column(String)
    payment = Column(String)
    user_id = Column(Integer)
    username = Column(String)