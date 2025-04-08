from sqlalchemy import Column, Integer, String, JSON
from db.point_db import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    type = Column(String)

    coordinates = Column(JSON, default=None)
    sphere = Column(String, default=None)

    user_token = Column(String)

    like = Column(Integer, default=0)
    dislike = Column(Integer, default=0)