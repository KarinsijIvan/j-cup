from fastapi import APIRouter, HTTPException, Depends, Header
#from user import get_user_from_token
from sqlalchemy.orm import Session
from models.point import Point
from schemas.point import PointCreate
from db.point_db import SessionLocal
import math

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/list/")
def get_point_list(person_latitude:float,
                   person_longitude:float,
                   radius:float,
                   db: Session = Depends(get_db)):
    points = db.query(Point).all()

    R = 6371000  # Радиус Земли в метрах

    result=[
        {"id": point.id, "longitude": point.longitude, "latitude": point.latitude}
        for point in points
        if (
            R * math.acos(
                math.sin(math.radians(person_latitude)) * math.sin(math.radians(point.latitude)) +
                math.cos(math.radians(person_latitude)) * math.cos(math.radians(point.latitude)) *
                math.cos(math.radians(person_longitude - point.longitude))
            )
        ) <= radius
    ]
    return result