from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVER_HOST: str 
    SERVER_PORT: int

settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)