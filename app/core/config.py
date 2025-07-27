
from pydantic_settings import BaseSettings


class settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_HOST:str
    POSTGRES_PORT:int
    POSTGRES_DB:str

    @property
    def DATABASE_URL(self) ->str:

        '''build postgres DNS string dynamically'''
        return(
            postgres + psycopg2 :// {self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}
            @{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}
        )
    
    # load env vars from .env
    class Config:
        env_file: '.env'  # automatically load envs


# create settings instance
settings = Settings()

