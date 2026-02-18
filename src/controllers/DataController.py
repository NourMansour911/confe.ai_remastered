from .BaseController import BaseController
from fastapi import UploadFile,HTTPException


class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    def validate_file(self,file:UploadFile):
        
        
        if file.content_type not in self.settings.FILE_ALLOWED_EXT:
            raise HTTPException(status_code=400, detail="Invalid File Format")
            
        if file.size > self.settings.FILE_MAX_SIZE * self.size_scale:
            raise HTTPException(status_code=400, detail="File Too Large")
        
        return True
        
    