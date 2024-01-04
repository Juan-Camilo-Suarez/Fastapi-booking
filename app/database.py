from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'booking'
DB_PASSWORD = 'booking'
DB_NAME = 'booking'

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

engine = create_async_engine(DATABASE_URL)

# session es la traccion(transccion es el conjunto de acciones que hacemos en la bd)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# to compare status migrations
class Base(DeclarativeBase):
    pass
