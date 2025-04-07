from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.estimation_db import get_db as estimation_get_db
from db.point_db import get_db as point_get_db
from models.point import Point
from models.estimation import Estimation
from schemas.estimation import EstimationCreate

router = APIRouter(prefix="/estimations", tags=["Estimations"])

@router.post("/add_estimation/")
async def add_estimation(estimation_data: EstimationCreate, point_db: Session = Depends(point_get_db), estimation_db: Session = Depends(estimation_get_db)):
    if estimation_data.estimation not in (1, -1):
        raise HTTPException(status_code=400, detail="Estimation must be 1 or -1")

    point = point_db.query(Point).filter(Point.id == estimation_data.point_id).first()
    if not point:
        raise HTTPException(status_code=404, detail="Point not found")

    existing = estimation_db.query(Estimation).filter(
        Estimation.point_id == estimation_data.point_id,
        Estimation.user_token == estimation_data.user_token
    ).first()

    if existing:
            raise HTTPException(status_code=409, detail="User already rated this point")

    new_estimation = Estimation(
        estimation=estimation_data.estimation,
        point_id=estimation_data.point_id,
        user_token=estimation_data.user_token
    )

    estimation_db.add(new_estimation)

    point.estimation += new_estimation.estimation

    estimation_db.commit()
    point_db.commit()
    estimation_db.refresh(new_estimation)
    return {"message": "Estimation added successfully", "id": new_estimation.id}