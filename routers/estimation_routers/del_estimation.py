from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.estimation import Estimation
from models.point import Point
from db.point_db import SessionLocal as PointSessionLocal
from db.estimation_db import SessionLocal as EstimationSessionLocal


router = APIRouter()

def get_db():
    point_db = PointSessionLocal()
    estimation_db = EstimationSessionLocal()
    try:
        yield point_db, estimation_db
    finally:
        point_db.close()
        estimation_db.close()



@router.post("/del_estimation/")
def del_estimation(point_id: int, point_db, estimation_db: Session = Depends(get_db)):

    point = point_db.query(Point).filter(Point.id == point_id).first()
    estimation = estimation_db.query(Estimation).filter(Estimation.point_id == point_id).first()

    if estimation is None:
        raise HTTPException(status_code=404, detail="Like not found")

    if estimation.estimation == 1:
        point.estimation -= 1

    elif estimation.estimation == -1:
        point.estimation += 1

    estimation_db.query.filter_by(point_id=point_id).delete()

    point_db.commit()
    estimation_db.commit()