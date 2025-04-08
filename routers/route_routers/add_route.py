from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from schemas.point import RouteCreate
from db.point_db import get_db

router = APIRouter(prefix="/route", tags=["Route"])


@router.post("/add_route/")
async def add_route(route: RouteCreate, db: Session = Depends(get_db)):
    new_route = Point(**route.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return {"message": "Route add"}