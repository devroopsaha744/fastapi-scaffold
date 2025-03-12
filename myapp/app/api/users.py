from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.crud.user import create_user, get_users, get_user, update_user, delete_user
from app.utils.dependencies import get_db, get_current_user

router = APIRouter()

@router.get('/', response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return create_user(db, user)

@router.get('/{user_id}', response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.put('/{user_id}', response_model=UserResponse)
def modify_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_user(db, user_id, user)

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_user(user_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    delete_user(db, user_id)
    return None
