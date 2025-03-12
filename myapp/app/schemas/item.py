from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)

class ItemResponse(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
