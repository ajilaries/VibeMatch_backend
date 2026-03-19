from fastapi import APIRouter
from fastapi import HTTPException
from app.schema.login_schema import LoginRequest
from sqlalchemy.orm import Session
from app.schema.user_schema import UserCreate
from app.models.user_model import User
from app.database import SessionLocal
router=APIRouter()


@router.post("/login")
def login(user):
    db = SessionLocal()

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}
@router.post("/signup")
def signup(user:UserCreate):
    db:Session=SessionLocal()

    new_user=User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message":"User created successfully"}