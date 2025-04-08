from pydantic import BaseModel, conlist
from typing import List

Coordinate = conlist(float)

class PointCreate(BaseModel):
    name: str
    description: str
    coordinates: List[float]
    user_token: str

class ProposalCreate(BaseModel):
    name: str
    description: str
    sphere: str
    user_token: str

class RouteCreate(BaseModel):
    name: str
    description: str
    coordinates: List[Coordinate]
    user_token: str

class DelPoint(BaseModel):
    point_id: int
    user_token: str