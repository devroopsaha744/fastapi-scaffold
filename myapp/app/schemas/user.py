from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=50)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

    @validator('password')
    def validate_password(cls, v):
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must include a digit')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must include an uppercase letter')
        return v

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    password: Optional[str] = Field(None, min_length=8)

    @validator('password')
    def validate_password(cls, v):
        if v is None:
            return v
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must include a digit')
        if not any(c.isupper() for c in v):
            raise ValueError('Password must include an uppercase letter')
        return v

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
