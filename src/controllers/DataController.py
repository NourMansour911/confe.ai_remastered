from .BaseController import BaseController
from fastapi import UploadFile,status,HTTPException
from fastapi.responses import JSONResponse
from models import ResponseEnum

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    def validate_file(self,file:UploadFile):
        
        if file.size > self.settings.FILE_MAX_SIZE * self.size_scale:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=
            {"signal":ResponseEnum.FILE_SIZE_EXCEEDED.value})
            
        if file.content_type not in self.settings.FILE_ALLOWED_EXT:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content= {"signal": ResponseEnum.FILE_TYPE_NOT_ALLOWED.value } )  
           
        return JSONResponse(status_code=status.HTTP_200_OK, content={"signal":ResponseEnum.FILE_VALID.value})
        
    