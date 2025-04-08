from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from sqlalchemy.orm import Session
from db.estimation_db import get_db as estimation_get_db
from db.point_db import get_db as point_get_db
from models.point import Point
from models.estimation import Estimation
from schemas.estimation import EstimationDelite

router = APIRouter(prefix="/estimations", tags=["Estimations"])

@router.post("/del_estimation/")
async def del_estimation(estimation_data: EstimationDelite, point_db: Session = Depends(point_get_db), estimation_db: Session = Depends(estimation_get_db)):

    point = point_db.query(Point).filter(Point.id == estimation_data.point_id).first()
    estimation = estimation_db.query(Estimation).filter(
        Estimation.point_id == estimation_data.point_id,
        Estimation.user_token == estimation_data.user_token
    ).first()

    if estimation is None:
        raise HTTPException(status_code=404, detail="Like not found")

    if estimation.estimation == 1:
        point.like -= 1

    elif estimation.estimation == -1:
        point.dislike -= 1

    # estimation_db.query(Estimation).filter(Point.id == estimation_data.point_id).first().delete()

    # Estimation.delete().where(
    #     Estimation.point_id == estimation_data.point_id,
    #     Estimation.user_token == estimation_data.user_token
    # )

    point_db.commit()
    estimation_db.commit()