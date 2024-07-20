from fastapi import FastAPI
from app.middleware import regist_middleware
from app.urls import regist_router
from app.core.database import init_db


def create_app():
    app = FastAPI()

    init_db()
    regist_middleware(app)
    regist_router(app)
    return app
