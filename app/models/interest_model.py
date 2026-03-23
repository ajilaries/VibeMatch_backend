from sqlalchemy import Column,Integer,String,ForeignKey
from app.database import Base

class Interest(Base):
    __tablename__="interests"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("user_id"))
    interest=Column(String)