import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('.env'))

class Settings(BaseSettings):
    # Настройки бота
    json2video_api_key: str = Field(
        default=os.getenv("JSON2VIDEO_API_KEY", ""),
        description="API ключ для доступа к сервису JSON2VIDEO"
    )
    json2video_base_url: str = Field(
        default=os.getenv("JSON2VIDEO_BASE_URL", "https://api.json2video.com"),
        description="Базовый URL для API JSON2VIDEO"
    )

    # Конфигурация загрузки из .env
    model_config = SettingsConfigDict(extra="ignore", env_file=".env", env_file_encoding="utf-8")
    

settings = Settings()