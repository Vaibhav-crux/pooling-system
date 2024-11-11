from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Poll(Base):
    __tablename__ = "polls"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    option1 = Column(Integer, default=0)
    option2 = Column(Integer, default=0)
    option3 = Column(Integer, default=0)
    option4 = Column(Integer, default=0)
