from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

engine = create_async_engine(settings.DATABASE_URL)

# session es la traccion(transccion es el conjunto de acciones que hacemos en la bd)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# to compare status migrations
class Base(DeclarativeBase):
    pass
