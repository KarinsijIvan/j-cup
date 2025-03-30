from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.point import Point
from models.estimation import Estimation
from schemas.estimation import EstimationCreate
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




@router.post("/add_estimation/")
def add_estimation(estimation_input: EstimationCreate, point_db, estimation_db: Session = Depends(get_db)):
    point = point_db.query(Point).filter(Point.id == estimation_input.point_id).first()
    estimation = estimation_db.query(Point).filter(Estimation.point_id == estimation_input.point_id).first()
    new_estimation = Estimation(**estimation_input.dict())
    if point is None:
        raise HTTPException(status_code=404, detail="Point not found")
    if estimation is None:
        estimation_db.add(new_estimation)
    else:
        estimation.estimation=estimation_input.estimation
    estimation_db.commit()
    estimation_db.close()