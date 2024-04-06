from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from .database import Base
from datetime import datetime

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    location_id = Column(Integer, index=True)
    day_of_week = Column(Integer, index=True)
    free_day = Column(Boolean, index=True)
    month = Column(Integer, index=True)
    pretocnost_7 = Column(Integer, index=True)
    pretocnost_3 = Column(Integer, index=True)
    pretocnost_q = Column(Integer, index=True)
