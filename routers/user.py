from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserSignIn  # Добавили UserSignIn
from db.user_db import SessionLocal
import re

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sign-up")
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter((User.login == user.login)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="The user already exists")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "The user was successfully created"}

@router.post("/sign-in")
def sign_in(user: UserSignIn, db: Session = Depends(get_db)):
    if not user.login or not user.password:
        raise HTTPException(status_code=400, detail="Write login and password")

    db_user = db.query(User).filter(User.login == user.login).first()

    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid login or password")

    return {"token": str(db_user.id)}


def get_user_from_token(token: str, db: Session = Depends(get_db)):
    try:
        user_id = int(token)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid token format")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user