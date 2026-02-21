from fastapi import APIRouter,FastAPI,Depends,File,UploadFile
from helpers.config import get_settings,Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/data/upload",
    tags=["data"],
)

@data_router.post("/file/{project_id}",tags=["base"])
async def upload_file(project_id: str ,file: UploadFile):
    
    response = DataController().validate_file(file=file)

    
    return response
    
    