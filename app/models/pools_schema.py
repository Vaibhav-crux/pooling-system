from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db_config import Base

class Poll(Base):
    __tablename__ = "polls"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    option1 = Column(Integer, default=0)
    option2 = Column(Integer, default=0)
    option3 = Column(Integer, default=0)
    option4 = Column(Integer, default=0)

class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey("polls.id"), index=True)
    option = Column(Integer, index=True)
    user_id = Column(String, index=True)
