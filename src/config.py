from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import ClassVar

class Settings(BaseSettings):
    DB_HOST: ClassVar[str] = "192.168.1.37"
    DB_PORT: ClassVar[int] = 5000
    DB_USER: ClassVar[str] = "mainroot"
    DB_PASS: ClassVar[str] = "LFF7VF1sm"
    DB_NAME: ClassVar[str] = "max"
    
    @property
    def DATABASE_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def DATABASE_URL_syncopg(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    #model_conf= SettingsConfigDict(env_file=".env")

class path_data:
    path_save_FPM_POO:str = "example_FPM_POO.xlsx"
    path_save_employment:str = "example_employment.xlsx"
    path_load_FPM_POO:str = ""
    path_load_employment:str = ""

# Load settings from .env file
settings = Settings()