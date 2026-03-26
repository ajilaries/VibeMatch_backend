from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.utils.dependencies import get_current_user
from app.schema.profile_schema import UpdateProfileSchema

router=APIRouter(prefix="/api",tags=["profile"])


@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "bio": current_user.bio,
        "dob": str(current_user.dob) if current_user.dob else None,
        "profile_image": current_user.profile_image,
        "profile_video": current_user.profile_video,
        "location": current_user.location,
        "latitude": current_user.latitude,
        "longitude": current_user.longitude
    }


@router.put("/profile")
def update_profile(
        data:UpdateProfileSchema,
        current_user:User=Depends(get_current_user),
        db:Session=Depends(get_db)
):
    if data.username:
        #check if username already exists
        existing_user=db.query(User).filter(User.username==data.username).first()
        if existing_user and existing_user.id !=current_user.id:
            raise HTTPException(status_code=400,detail="Username already taken")
        current_user.username=data.username

    if data.bio is not None:
        current_user.bio-data.bio
    if data.dob:
        current_user.dob=data.dob
    if data.profile_image:
        current_user.profile_image=data.profile_image
    if data.profile_video:
        current_user.profile_video=data.profile_video

    if data.location:
        current_user.location=data.location
    db.commit()
    db.refresh(current_user)

    return{
        "message":"profile updated sucessfully",
        "user":{
            "username":current_user.username,
            "bio":current_user.bio,
            "location":current_user.location
        }
    }