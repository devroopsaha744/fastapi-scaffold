from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from app.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=settings.access_token_expire_minutes))
    to_encode.update({'exp': expire})
    encoded = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded
