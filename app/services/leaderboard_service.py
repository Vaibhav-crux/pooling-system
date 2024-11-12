from sqlalchemy.orm import Session

from app.models.pools_schema import Poll

def get_leaderboard(db: Session):
    polls = db.query(Poll).order_by((Poll.option1 + Poll.option2 + Poll.option3 + Poll.option4).desc()).all()
    
    leaderboard = {
        "leaderboard": [
            {"poll_id": poll.id, "question": poll.question, 
             "option1": poll.option1, "option2": poll.option2, 
             "option3": poll.option3, "option4": poll.option4}
            for poll in polls
        ]
    }
    
    return leaderboard
