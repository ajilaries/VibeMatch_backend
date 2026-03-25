from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User

router=APIRouter(prefix="/api",tags=["profile"])

@router.get("/profile")
def get_profile(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
        return{
            "id":user.id,
            "username":user.username,
            "bio":user.bio,
            "profile_image":user.profile_image,
            "profile_video":user.profile_video,
            "location":user.location
        }
    
@router.put("/profile")
def update_profile(data:dict,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==data["user_id"]).filter()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    user.bio=data.get("bio")
    user.location=data.get("location")

    db.commit()

    return{"message":"profile updated"}