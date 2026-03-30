from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User

router = APIRouter(prefix="/api", tags=["Discover"])

@router.get("/discover")
def discover_users(db: Session = Depends(get_db)):

    users=db.query(User).all()

    result=[]

    for user in users:
        result.append({
            "id":user.id,
            "username":user.username,
            "bio":user.bio,
            "profile_image":user.profile_image,
            "location":user.location
        })

    return result