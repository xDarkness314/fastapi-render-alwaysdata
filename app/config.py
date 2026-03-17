from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings loaded directly from environment variables.
    Render provides these values from the dashboard.
    """

    environment: str = "production"
    database_url: str

    class Config:
        case_sensitive = False


settings = Settings()