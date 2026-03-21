from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.connection import Connection

router=APIRouter()
def send_request(sender_id:int,receiver_id:int,db:Session=Depends(get_db)):

    request=Connection(
        sender_id=sender_id,
        receiver_id=receiver_id,
        status="pending"
    )

    db.add(request)
    db.commit()

    return {"message":"Request sent"}

@router.post("/accept-request")
def accept_request(request_id:int, db:Session=Depends(get_db)):
    request =db.query(Connection).filter(
        Connection.id==request_id

    ).first()

    request.status="accepted"

    db.commit()

    return {"message":"Request accepted"}

@router.get("/connection-request")
def get_request(user_id:int,db:Session=Depends(get_db)):
    requests=db.query(Connection).filter(
        Connection.receiver_id==user_id,
        Connection.status=="pending"
    ).all()

    return requests