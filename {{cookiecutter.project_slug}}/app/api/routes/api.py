from fastapi import APIRouter

from app.api.routes import user_route

app = APIRouter()

app.include_router(user_route.router, tags=["User"], prefix="/admin/user")
