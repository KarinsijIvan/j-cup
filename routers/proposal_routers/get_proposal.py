from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from models.point import Point
from db.point_db import get_db

router = APIRouter(prefix="/proposal", tags=["Proposal"])


@router.get("/{proposal_id:int}/")
def get_proposal(proposal_id: int, db: Session = Depends(get_db)):
    proposal = db.query(Point).filter(Point.id == proposal_id).first()
    if proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return proposal
