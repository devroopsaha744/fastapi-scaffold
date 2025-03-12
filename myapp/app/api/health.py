from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.dependencies import get_db
from app.services.health import check_system

router = APIRouter()

@router.get('/liveness')
def liveness():
    return {'status': 'alive'}

@router.get('/readiness')
def readiness(db: Session = Depends(get_db)):
    status = check_system(db)
    return status
