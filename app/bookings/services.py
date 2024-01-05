from sqlalchemy import select

from app.bookings.models import Bookings
from app.services.base import BaseServices


class BookingService(BaseServices):
    model = Bookings
