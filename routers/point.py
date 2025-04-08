from fastapi import APIRouter, HTTPException, Depends, Header
#from user import get_user_from_token
from sqlalchemy.orm import Session
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

@router.post("/add_point")
async def add_point(point: PointCreate, db: Session = Depends(get_db)):
    new_point = Point(**point.dict())
    db.add(new_point)
    db.commit()
    db.refresh(new_point)
    return {"message": "Point add"}


@router.get("/list")
def get_point_list(db: Session = Depends(get_db)):
    points = db.query(Point).all()
    result = [
    {"id": point.id, "longitude": point.longitude, "latitude": point.latitude}
    for point in points
    ]
    return result


@router.get("/{point_id}")
def get_point(point_id: int, db: Session = Depends(get_db)):
    point = db.query(Point).filter(Point.id == point_id).first()
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    return point

