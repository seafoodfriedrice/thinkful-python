from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey


engine = create_engine('postgresql://postgres:postgres@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    auction_id = Column(Integer, ForeignKey('users.id'))
    bids = relationship('Bid', backref='item')


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    auctions = relationship('Item', backref='user')
    bids = relationship('Bid', backref='user')


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

    item_id = Column(Integer, ForeignKey('items.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


Base.metadata.create_all(engine)
