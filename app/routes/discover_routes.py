from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User

router = APIRouter(prefix="/api", tags=["Discover"])

@router.get("/discover")
def discover_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]