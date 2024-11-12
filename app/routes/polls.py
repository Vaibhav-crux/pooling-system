from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.services.poll_service import create_poll, vote_on_poll, get_poll_results

router = APIRouter()

@router.post("/polls/", response_model=dict)
def create_poll_route(question: str, db: Session = Depends(get_db)):
    # Now using the service function to create a poll
    try:
        poll = create_poll(question, db)
        return {"id": poll.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/polls/{poll_id}/vote/", response_model=dict)
def vote_on_poll_route(poll_id: int, option: int, user_id: str = None, db: Session = Depends(get_db)):
    # Now using the service function to register a vote
    try:
        vote = vote_on_poll(poll_id, option, user_id, db)
        return {"id": vote.id}
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/polls/{poll_id}", response_model=dict)
def get_poll_results_route(poll_id: int, db: Session = Depends(get_db)):
    # Now using the service function to get poll results
    try:
        results = get_poll_results(poll_id, db)
        return results
    except ValueError:
        raise HTTPException(status_code=404, detail="Poll not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
