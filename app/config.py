from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_VERSION: str = "0.1.1"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"


settings = Settings()
