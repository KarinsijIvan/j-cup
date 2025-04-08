from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
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


#add_estimation нет, но вы держитесь

# @router.post("/add_estimation")
# def add_estimation(point_id: int, estimation: EstimationCreate, point_db, estimation_db: Session = Depends(get_db)):
#     point = point_db.query(Point).filter(Point.id == point_id).first()
#     estimation = estimation_db.query(Point).filter(Estimation.point_id == point_id).first()
#     if point is None:
#         raise HTTPException(status_code=404, detail="Point not found")
#
#     point_db.commit()
#     estimation_db.close()