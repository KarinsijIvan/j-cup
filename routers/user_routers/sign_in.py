from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserSignIn
from db.user_db import SessionLocal

router = APIRouter(prefix="/user", tags=["User"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post("/sign-in/")
def sign_in(user: UserSignIn, db: Session = Depends(get_db)):
    if not user.login or not user.password:
        raise HTTPException(status_code=400, detail="Write login and password")

    db_user = db.query(User).filter(User.login == user.login).first()

    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid login or password")

    return {"token": str(db_user.id)}