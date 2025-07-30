
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_HOST:str
    POSTGRES_PORT:int
    POSTGRES_DB:str

    @property
    def DATABASE_URL(self) -> str:
        """Build PostgreSQL DSN string dynamically"""
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # auto loads .env file
    class Config:
        env_file = ".env"


# create settings instance
settings = Settings()

