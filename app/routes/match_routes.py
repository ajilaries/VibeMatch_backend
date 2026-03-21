from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.match import Match
from app.models.message import Message


router=APIRouter()

@router.get("/matches")
def get_matches(user_id:int, db:Session=Depends(get_db)):
    matches=db.query(Match).filter(
        (Match.user1_id==user_id)|
    (Match.user2_id==user_id)
    ).all()

    return matches


from app.models.message import Message

@router.get("/chats")
def get_chats(user_id: int, db: Session = Depends(get_db)):

    chats = db.query(Message).filter(
        (Message.sender_id == user_id) |
        (Message.receiver_id == user_id)
    ).all()

    return chats