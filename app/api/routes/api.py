from fastapi import APIRouter

from app.api.routes.predict import router as PredictRouter

app = APIRouter()
app.include_router(PredictRouter, tags=["predict"], prefix="/predict")
