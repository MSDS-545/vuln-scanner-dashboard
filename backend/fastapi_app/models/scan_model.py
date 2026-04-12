from sqlalchemy import Column, Integer, String
from ..config.database import Base

class Scan(Base):

    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    severity = Column(String)
    vulnerability = Column(String)