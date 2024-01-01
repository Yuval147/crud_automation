from sqlalchemy import Column , Integer , String
from database import Base

class footballs(Base) :
    __tablename__ = "football"

    id = Column(Integer, primary_key=True, nullable=False)
    player_name = Column(String)
    team = Column(String)
    num_player = Column(Integer)
    goals = Column(Integer)
    assist = Column(Integer)
    transfer_market = Column(Integer)
    country = Column(String)
