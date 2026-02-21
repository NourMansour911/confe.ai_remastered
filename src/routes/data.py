from fastapi import APIRouter,FastAPI,Depends,File,UploadFile
from helpers.config import get_settings,Settings
from controllers import DataController,ProjectController
import os
import aiofiles
from models import ResponseEnum


data_router = APIRouter(
    prefix="/data/upload",
    tags=["data"],
)

@data_router.post("/file/{project_id}",tags=["base"])
async def upload_file(project_id: str ,file: UploadFile,settings: Settings = Depends(get_settings)):
    
    is_valid,signal = DataController().validate_file(file=file)
    
    if not is_valid:
        return signal
    
    project_dir = ProjectController().get_project_path(project_id=project_id)
    file_path = os.path.join(project_dir,file.filename)
    
    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(settings.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)
        
    return {"signal":ResponseEnum.FILE_UPLOAD_SUCCESS.value}
    
    