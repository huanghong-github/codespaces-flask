from fastapi import APIRouter

from app.controller import user, item


api_router = APIRouter()
api_router.include_router(user.router, tags=["login"])
api_router.include_router(item.router, prefix="/item", tags=["item"])


def regist_router(app):
    app.include_router(api_router)
