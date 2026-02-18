from fastapi import APIRouter,FastAPI
import os

base_router = APIRouter()

@base_router.get("/",tags=["base"])
async def root():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
            "message": "Welcome to Confe.AI!",
            "app_name": app_name,
            "app_version": app_version,
            }