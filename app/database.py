from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)

# session es la traccion(transccion es el conjunto de acciones que hacemos en la bd)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# to compare status migrations
class Base(DeclarativeBase):
    pass
