from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.stats import StatsResponse
from app.crud.stats import get_system_stats
from app.utils.dependencies import get_db, get_current_admin_user

router = APIRouter()

@router.get('/dashboard', response_model=StatsResponse)
def dashboard(db: Session = Depends(get_db), current_user: dict = Depends(get_current_admin_user)):
    return get_system_stats(db)
