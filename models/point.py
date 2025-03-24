from sqlalchemy import Column, Integer, Float, String
from db.point_db import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    user_token = Column(String)