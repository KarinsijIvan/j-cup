from pydantic import BaseModel, conlist
from typing import List

Coordinate = conlist(float)

class PointCreate(BaseModel):
    name: str
    description: str
    coordinates: List[Coordinate]
    user_token: str
    sphere: str