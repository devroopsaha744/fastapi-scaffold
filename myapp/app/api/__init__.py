from fastapi import APIRouter

api_router = APIRouter()

from app.api import users, items, admin, ml, health

api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(items.router, prefix='/items', tags=['items'])
api_router.include_router(admin.router, prefix='/admin', tags=['admin'])
api_router.include_router(ml.router, prefix='/ml', tags=['machine learning'])
api_router.include_router(health.router, prefix='/health', tags=['health'])
