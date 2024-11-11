from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.pools_schema import Poll
from app.services.poll_service import create_poll, get_poll_results

router = APIRouter()

@router.post("/polls", response_model=dict)
def create_poll_route(poll_data: dict, db: Session = Depends(get_db)):
    return create_poll(poll_data, db)

@router.get("/polls/{poll_id}", response_model=dict)
def get_poll_results_route(poll_id: int, db: Session = Depends(get_db)):
    poll = get_poll_results(poll_id, db)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")
    return poll
