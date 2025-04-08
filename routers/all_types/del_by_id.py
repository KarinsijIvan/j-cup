from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, or_
from sqlalchemy.orm import Session
from db.point_db import get_db as point_get_db
from models.point import Point
from schemas.point import DelPoint

router = APIRouter(prefix="/all_types", tags=["All types"])

@router.post("/del_by_id/")
async def del_by_id(point_data: DelPoint, point_db: Session = Depends(point_get_db)):
    if point_data.user_token == "-1":
        point = point_db.query(Point).filter(Point.id == point_data.point_id).first()
    else:
        point = point_db.query(Point).filter(
            Point.id == point_data.point_id,
            Point.user_token == point_data.user_token
        ).first()

    if not point:
        raise HTTPException(status_code=404, detail="Point not found or user is not the creator")

    point_db.delete(point)

    point_db.commit()