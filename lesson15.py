from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase

dsn = 'sqlite:///test.db'

engine = create_engine(dsn)


class Base(DeclarativeBase):
    pass


class Seller(Base):
    __tablename__ = "Sellers"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    company = Column(String(64), unique=True, nullable=False)
    phone = Column(String(64), unique=True, nullable=False)


class Products(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(200), unique=True, nullable=False)
    cost = Column(Integer, unique=False, nullable=False)
    count = Column(Integer, unique=False, nullable=False, default=0)
    seller_id = Column(Integer, ForeignKey("Sellers.id"))


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(200), unique=True, nullable=False)
    password = Column(String(64), unique=False, nullable=False)
    email = Column(String(200), unique=False, nullable=True)


class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    product_id = Column(Integer, ForeignKey("Products.id"))
    user_id = Column(Integer, ForeignKey("Users.id"))


def create_table():
    Base.metadata.create_all(engine)


create_table()
