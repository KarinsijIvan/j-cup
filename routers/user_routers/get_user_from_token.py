from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from db.user_db import get_db

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/get_user_from_token/")
def get_user_from_token(token: str, db: Session = Depends(get_db)):
    try:
        user_id = int(token)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token format")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user