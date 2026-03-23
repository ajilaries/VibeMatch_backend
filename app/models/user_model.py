from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    dob = Column(Date)

    bio = Column(String, nullable=True)

    profile_image = Column(String, nullable=True)
    profile_video = Column(String, nullable=True)

    location = Column(String, nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)