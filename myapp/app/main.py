from fastapi import FastAPI
from app.api import api_router
from app.middleware import add_middlewares
from app.database import db_engine
from app.models import Base

app = FastAPI()
add_middlewares(app)
Base.metadata.create_all(bind=db_engine)
app.include_router(api_router, prefix='/api')

@app.get('/')
def root():
    return {'message': 'Enhanced FastAPI App'}
