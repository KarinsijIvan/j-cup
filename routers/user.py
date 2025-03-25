from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from db.user_db import SessionLocal
import re

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sign-up")
async def sign_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        (User.login == user.login)
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Пользователь уже существует")
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Пользователь успешно создан"}

@router.get("/sign-in")
def sign_in(login: str, password: str, db: Session = Depends(get_db)):
    if not login or not password:
        raise HTTPException(status_code=400, detail="Введите логин и пароль")

    user = db.query(User).filter(User.login == login).first()

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if user.password != password:
        raise HTTPException(status_code=401, detail="Неверный пароль")

    return {"message": "Вход выполнен успешно", "user_id": user.id, "token": user.id}