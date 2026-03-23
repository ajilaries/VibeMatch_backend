from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schema.login_schema import LoginSchema
from app.schema.user_schema import UserSchema
from app.utils.jwt_handler import create_access_token
from app.utils.password_handler import hash_password,verify_password

router=APIRouter()

#signup

@router.post("/signup")
def signup(data:UserSchema,db:Session=Depends(get_db)):

    existing_user=db.query(User).filter(User.email==data.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    
    hashed_password=hash_password(data.password)

    new_user=User(
        username=data.username,
        email=data.email,
        password=hashed_password,
        dob=data.bob,
        bio=data.bio,
        location=data.location
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token=create_access_token(
        data={"user_id":new_user.id,"email":new_user.email}
    )
    return {
        "message":"signup successful",
        "access_token":access_token,
        "token_type":"bearer",
        "user":{
            "id":new_user.id,
            "username":new_user.username,
            "email":new_user.email
        }
    }

#login

@router.post("/login")
def login(data:LoginSchema,db:Session=Depends(get_db)):
    user=db(User).filter(User.email==data.email).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    if not verify_password(data.password,user.password):
        raise HTTPException(status_code=401,detail="Incorrect password")
    
    access_token=create_access_token(
        data={"user_id":user.id,"email":user.email}
    )

    return{
        "access_token":access_token,
        "token_type":"bearer",
        "user":{
            "id":user.id,
            "username":user.username,
            "email":user.email
        }
    }

#profile

@router.get("/profile/{user_id}")
def get_profile(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    
    return{
        "id":user.id,
        "username":user.username,
        "dob":user.dob,
        "bio":user.bio,
        "location":user.location,
        "latitude":user.latitude,
        "longitude":user.longitude,
        "profile_image":user.profile_image,
        "profile_video":user.profile_video
    }