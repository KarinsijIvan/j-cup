from sqlalchemy import Column, Integer, Float, String
from db.point_db import Base


class Estimation(Base):
    __tablename__ = "estimation"

    id = Column(Integer, primary_key=True, index=True)
    estimation = Column(Integer)
    point_id = Column(Integer)
    user_token = Column(String)
