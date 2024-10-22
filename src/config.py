#from pydantic import BaseSettings
from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "192.168.1.37"  
    DB_PORT: int = 5000 
    DB_USER: str = "mainroot"
    DB_PASS: str = "LFF7VF1sm"
    DB_NAME: str = "max"

    @property 
    def DATABASE_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property 
    def DATABASE_URL_syncpg(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
class Config:
    env_file = "venv"  # Укажите файл окружения

# Загрузка настроек из .env файла
settings = Settings()
