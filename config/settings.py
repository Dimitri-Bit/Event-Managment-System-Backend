from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_url: str = "sqlite:///db.db"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
