from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.like import Like
from app.models.match import Match

router=APIRouter(prefix="/api")


@router.post("/like")
def like_user(receiver_id:int,sender_id:int,db:Session=Depends(get_db)):

    like=Like(sender_id=sender_id,receiver_id=receiver_id)
    db.add(like)
    db.commit()

    #check if reverse like exists

    reverse=db.query(Like).filter(
        Like.sender_id==receiver_id,
        Like.receiver_id==sender_id
    ).first()

    if reverse:
        match=Match(user1_id=sender_id,user2_id=receiver_id)
        db.add(match)
        db.commit()

        return {"message":"its a match"}
    return{"message": "user liked"}