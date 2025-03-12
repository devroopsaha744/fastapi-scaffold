from fastapi.middleware.cors import CORSMiddleware

def add_middlewares(app):
    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
