from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schema.login_schema import LoginSchema
from app.schema.user_schema import UserSchema
from app.utils.jwt_handler import create_access_token
from app.utils.password_handler import hash_password
from app.utils.password_handler import verify_password
router = APIRouter()

# SIGNUP
@router.post("/signup")
def signup(data: UserSchema, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(data.password)

    new_user = User(
        name=data.name,
        email=data.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(
        data={"user_id": new_user.id, "email": new_user.email}
    )

    return {
        "message": "Signup successful",
        "access_token": access_token,
        "token_type": "bearer"
    }
# LOGIN
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password,user.password):
        raise HTTPException(status_code=-401,detail="incorrect password")
    access_token = create_access_token(
        data={"user_id": user.id, "email": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }