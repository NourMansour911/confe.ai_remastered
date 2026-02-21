from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str 
    GITHUB_TOKEN: str
    OPENROUTER_API_KEY: str
    
    FILE_MAX_SIZE: int
    FILE_ALLOWED_EXT:list
    
    FILE_DEFAULT_CHUNK_SIZE: int
    class Config:
        env_file = ".env"
        
        
def get_settings():
    return Settings()