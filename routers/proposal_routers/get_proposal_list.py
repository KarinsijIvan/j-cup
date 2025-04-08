from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from db.point_db import get_db

router = APIRouter(prefix="/proposal", tags=["Proposal"])


@router.get("/list/")
def get_proposal_list(db: Session = Depends(get_db)):
    points = db.query(Point).filter(
        Point.type == "proposal"
    ).first()

    return points