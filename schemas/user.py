from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str

class UserSignIn(BaseModel):
    login: str = None
    password: str