from fastapi import APIRouter, HTTPException, Depends, Header
#from user import get_user_from_token
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from models.point import Point
from schemas.point import PointCreate
from db.point_db import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/addLike")
def addLike(point_id: int, db: Session = Depends(get_db)):
    point = db.query(Point).filter(Point.id == point_id).first()
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    point.likes+=1
    db.commit()