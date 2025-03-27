from pydantic import BaseModel

class EstimationCreate(BaseModel):
    estimation: str
    point_id: str
    user_token: str