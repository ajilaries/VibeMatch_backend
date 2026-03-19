from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models.user_model import User

router = APIRouter()

# SIGNUP
@router.post("/signup")
def signup(name: str, email: str, password: str):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=name,
        email=email,
        password=password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Signup successful"}


# LOGIN
@router.post("/login")
def login(email: str, password: str):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {
        "message": "Login successful",
        "user_id": user.id,
        "name": user.name
    }