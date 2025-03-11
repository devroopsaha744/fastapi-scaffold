TEMPLATE = {
    "app": {
        "api": {
            "__init__.py": "",
            "users.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/')\ndef get_users():\n    return {'message': 'List of users'}",
            "items.py": "from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get('/')\ndef get_items():\n    return {'items': ['item1', 'item2', 'item3']}",
            "admin.py": "from fastapi import APIRouter, Depends\nfrom app.auth import get_current_user\n\nrouter = APIRouter()\n\n@router.get('/dashboard')\ndef dashboard(user: dict = Depends(get_current_user)):\n    return {'message': f'Admin dashboard for {user}'}",
            "ml.py": "from fastapi import APIRouter\nimport pickle\nimport numpy as np\n\nrouter = APIRouter()\n\nwith open('app/models/model.pkl', 'rb') as f:\n    model = pickle.load(f)\n\n@router.post('/predict/')\ndef predict(data: list):\n    prediction = model.predict(np.array(data))\n    return {'prediction': prediction.tolist()}",
        },
        "models": {"__init__.py": "", "model.pkl": ""},
        "services": {
            "__init__.py": "",
            "tasks.py": "from fastapi import BackgroundTasks\n\ndef send_email(email: str):\n    print(f'Sending email to {email}')\n\ndef process_background_task(bg_tasks: BackgroundTasks, email: str):\n    bg_tasks.add_task(send_email, email)",
        },
        "utils": {
            "__init__.py": "",
            "dependencies.py": "from fastapi import Depends\nfrom sqlalchemy.orm import Session\nfrom app.database import SessionLocal\n\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n    finally:\n        db.close()",
        },
        "middleware.py": "from fastapi.middleware.cors import CORSMiddleware\n\ndef add_middlewares(app):\n    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])",
        "database.py": "from sqlalchemy import create_engine\nfrom sqlalchemy.orm import sessionmaker\nfrom app.config import settings\n\ndb_engine = create_engine(settings.database_url)\nSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)",
        "auth.py": "from fastapi.security import OAuth2PasswordBearer\nfrom fastapi import Depends\n\noauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')\n\ndef get_current_user(token: str = Depends(oauth2_scheme)):\n    return {'user': 'demo'}",
        "logger.py": "import logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)",
        "config.py": "from pydantic import BaseSettings\nclass Settings(BaseSettings):\n    database_url: str = 'sqlite:///./test.db'\nsettings = Settings()",
        "main.py": "from fastapi import FastAPI\nfrom app.api.users import router as users_router\nfrom app.api.items import router as items_router\nfrom app.api.ml import router as ml_router\nfrom app.middleware import add_middlewares\n\napp = FastAPI()\nadd_middlewares(app)\napp.include_router(users_router, prefix='/users')\napp.include_router(items_router, prefix='/items')\napp.include_router(ml_router, prefix='/ml')\n\n@app.get('/')\ndef root():\n    return {'message': 'FastAPI App'}",
    },
    "tests": {
        "test_main.py": "from fastapi.testclient import TestClient\nfrom app.main import app\n\nclient = TestClient(app)\n\ndef test_root():\n    response = client.get('/')\n    assert response.status_code == 200\n    assert response.json() == {'message': 'FastAPI App'}",
        "test_users.py": "from fastapi.testclient import TestClient\nfrom app.main import app\n\nclient = TestClient(app)\n\ndef test_get_users():\n    response = client.get('/users')\n    assert response.status_code == 200\n    assert 'message' in response.json()",
    },
    ".env": "DATABASE_URL=postgresql://user:password@localhost/dbname",
    "requirements.txt": "fastapi\nuvicorn\nsqlalchemy\npydantic\npytest\nhttpx\npandas\nnumpy\nscikit-learn",
    "Dockerfile": "FROM python:3.10\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ['uvicorn', 'app.main:app', '--host', '0.0.0.0', '--port', '8000']",
    "docker-compose.yml": "version: '3.8'\nservices:\n  fastapi:\n    build: .\n    ports:\n      - '8000:8000'\n    environment:\n      - DATABASE_URL=postgresql://user:password@db/dbname\n  db:\n    image: postgres:13\n    environment:\n      POSTGRES_USER: user\n      POSTGRES_PASSWORD: password\n      POSTGRES_DB: dbname",
    "README.md": "# FastAPI Boilerplate\n\nA scalable FastAPI project template with authentication, ML, background tasks, database, and middleware support.",
}
