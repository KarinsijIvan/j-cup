from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from schemas.point import PointCreate
from db.point_db import get_db

router = APIRouter(prefix="/point", tags=["Point"])


@router.post("/add_point/")
async def add_point(point: PointCreate, db: Session = Depends(get_db)):
    new_point = Point(**point.dict())
    db.add(new_point)
    db.commit()
    db.refresh(new_point)
    return {"message": "Point add"}