from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Match(Base):
    __tablename__="matches"

    id=Column(Integer,primary_key=True,index=True)
    user1_id=Column(Integer,ForeignKey("users.id"))
    user2_id=Column(Integer,ForeignKey("users.id"))
    