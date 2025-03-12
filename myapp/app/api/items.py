from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.crud.item import create_item, get_item, get_items, update_item, delete_item
from app.utils.dependencies import get_db, get_current_user

router = APIRouter()

@router.get('/', response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)

@router.post('/', response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def add_item(item: ItemCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return create_item(db, item, current_user.get('id'))

@router.get('/{item_id}', response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Item not found')
    return item

@router.put('/{item_id}', response_model=ItemResponse)
def modify_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return update_item(db, item_id, item)

@router.delete('/{item_id}', status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    delete_item(db, item_id)
    return None
