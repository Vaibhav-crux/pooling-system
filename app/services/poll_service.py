from sqlalchemy.orm import Session
from app.models.pools_schema import Poll

def create_poll(poll_data: dict, db: Session):
    poll = Poll(**poll_data)
    db.add(poll)
    db.commit()
    db.refresh(poll)
    return {"id": poll.id, **poll.__dict__}

def get_poll_results(poll_id: int, db: Session):
    poll = db.query(Poll).filter_by(id=poll_id).first()
    if not poll:
        return None
    return poll.__dict__
