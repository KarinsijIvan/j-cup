from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.estimation_db import get_db as estimation_get_db
from models.estimation import Estimation
from schemas.estimation import EstimationDelite

router = APIRouter(prefix="/estimations", tags=["Estimations"])

@router.post("/get_user_estimation/")
async def get_user_estimation(estimation_data: EstimationDelite, estimation_db: Session = Depends(estimation_get_db)):
    estimation = estimation_db.query(Estimation).filter(
        Estimation.point_id == estimation_data.point_id,
        Estimation.user_token == estimation_data.user_token
    ).first()

    if estimation:
        return {"message": estimation.estimation}
    else:
        return {"message": 0}
