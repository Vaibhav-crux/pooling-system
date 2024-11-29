from sqlalchemy.orm import Session
from app.models.pools_schema import Poll, Vote

def create_poll(question: str, db: Session):
    # Removed unused parameters option1, option2, option3, option4 and so on
    poll = Poll(question=question, option1=0, option2=0, option3=0, option4=0)
    db.add(poll)
    db.commit()
    db.refresh(poll)
    
    return poll

def vote_on_poll(poll_id: int, option: int, user_id: str = None, db: Session = None):
    # Corrected the order of arguments to ensure non-default args come first
    if db is None:
        raise ValueError("Database session is required")
    
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise ValueError("Poll not found")
    
    vote = Vote(poll_id=poll_id, option=option, user_id=user_id)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    
    return vote

def get_poll_results(poll_id: int, db: Session):
    # Corrected the order of arguments to ensure non-default args come first
    if db is None:
        raise ValueError("Database session is required")
    
    poll = db.query(Poll).filter(Poll.id == poll_id).first()
    if not poll:
        raise ValueError("Poll not found")
    
    total_votes = poll.option1 + poll.option2 + poll.option3 + poll.option4
    results = {
        "option1": round(poll.option1 / total_votes * 100, 2) if total_votes > 0 else 0,
        "option2": round(poll.option2 / total_votes * 100, 2) if total_votes > 0 else 0,
        "option3": round(poll.option3 / total_votes * 100, 2) if total_votes > 0 else 0,
        "option4": round(poll.option4 / total_votes * 100, 2) if total_votes > 0 else 0
    }
    
    return results
