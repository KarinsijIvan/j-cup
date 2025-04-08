from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from db.point_db import get_db

router = APIRouter(prefix="/point", tags=["Point"])


@router.get("/get_all/")
def get_point_list(db: Session = Depends(get_db)):
    points = db.query(Point).all()

    return points