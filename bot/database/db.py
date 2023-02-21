from sqlalchemy import BINARY, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.sqlite", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class BotUser(Base):
    __tablename__ = "BotUsers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    first_name = Column(String(200))
    balance = Column(Integer)

    def __init__(self, user_id, first_name, balance):
        self.user_id = user_id
        self.first_name = first_name
        self.balance = balance


class Cards(Base):
    __tablename__ = "Cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    cards = Column(String)

    def __init__(self, user_id, cards):
        self.user_id = user_id
        self.cards = cards


Base.metadata.create_all(bind=engine)
