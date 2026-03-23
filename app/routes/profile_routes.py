from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User

router=APIRouter(prefix="/api",tags=["profile"])

@router.get("/profile")
def get_profile(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    return{
        "id":user.id,
        "name":user.name,
        "email":user.email
    }