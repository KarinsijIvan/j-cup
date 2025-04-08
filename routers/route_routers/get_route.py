from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from models.point import Point
from db.point_db import get_db

router = APIRouter(prefix="/route", tags=["Route"])


@router.get("/{route_id:int}/")
def get_route(route_id: int, db: Session = Depends(get_db)):
    route = db.query(Point).filter(Point.id == route_id).first()
    if route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return route
