from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from db.user_db import get_db

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/sign-up/")
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter((User.login == user.login)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="The user already exists")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"token": str(new_user.id)}