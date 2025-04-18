from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from db.point_db import get_db

router = APIRouter(prefix="/all_types", tags=["All types"])


@router.get("/list/")
def get_route_list(db: Session = Depends(get_db)):
    routes = db.query(Point).filter(
        Point.type == "route"
    ).all()

    return routes