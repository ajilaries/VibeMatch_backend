from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.interest_model import Interest

router = APIRouter(prefix="/api", tags=["Interests"])

@router.post("/add-interest")
def add_interest(user_id: int, interest: str, db: Session = Depends(get_db)):

    interest = interest.lower()

    new_interest = Interest(
        user_id=user_id,
        interest=interest
    )

    db.add(new_interest)
    db.commit()

    return {"message": "Interest added"}