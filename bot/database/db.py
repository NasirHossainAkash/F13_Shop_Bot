from sqlalchemy import String,Column,Integer,create_engine,BINARY
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine("sqlite:///database.sqlite",echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class BotUser(Base):
    __tablename__ = "BotUsers"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    balance = Column(Integer)
    cards = Column(BINARY)

    def __init__(self,user_id,balance,cards):
        self.user_id = user_id
        self.balance = balance
        self.cards = cards


Base.metadata.create_all(bind=engine)



