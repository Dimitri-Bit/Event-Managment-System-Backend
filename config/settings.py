from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str = "sqlite:///db.db"
    DB_URL_SYNC: str = "sqlite:///db.db"
    SECRET_KEY: str = "test"
    HASH_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
