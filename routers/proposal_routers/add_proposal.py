from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.point import Point
from schemas.point import ProposalCreate
from db.point_db import get_db

router = APIRouter(prefix="/proposal", tags=["Proposal"])


@router.post("/add_proposal/")
async def add_proposal(proposal: ProposalCreate, db: Session = Depends(get_db)):
    new_proposal = Point(**proposal.dict())
    db.add(new_proposal)
    db.commit()
    db.refresh(new_proposal)
    return {"message": "Proposal add"}