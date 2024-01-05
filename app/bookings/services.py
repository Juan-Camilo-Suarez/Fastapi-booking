from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker


class BookingService:
    # classmehtod para no tener que crear una instacia cada vez que se quiera usar el metodo
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Bookings.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
