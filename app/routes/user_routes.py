from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate
from app.models.user_model import User
from app.database import sessionLocal

router=APIRouter()

@router.post("/signup")
def signup(user:UserCreate):
    db:Session=sessionLocal()

    new_user=User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User created successfully"}