from sqlalchemy import select

from app.database import async_session_maker


class BaseServices:
    # this value can be redefined by implementing in other classes
    model = None

    # classmehtod para no tener que crear una instacia cada vez que se quiera usar el metodo
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
