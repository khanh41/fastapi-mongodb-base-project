from fastapi import APIRouter

from app.api.routes import user_route, authentication

app = APIRouter()
app.include_router(authentication.router, tags=["Authentication"], prefix="/authentication")

app.include_router(user_route.router, tags=["User"], prefix="/admin/user")
