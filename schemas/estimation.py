from pydantic import BaseModel

class EstimationCreate(BaseModel):
    estimation: int
    point_id: int
    user_token: str

class EstimationDelite(BaseModel):
    point_id: int
    user_token: str