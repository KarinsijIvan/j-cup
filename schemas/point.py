from pydantic import BaseModel

class PointCreate(BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float
    user_token: str