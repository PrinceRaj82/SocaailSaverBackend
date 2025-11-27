from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 10

    class Config:
        env_file = ".env"

settings = Settings()
