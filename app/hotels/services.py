from app.hotels.models import Hotels
from app.services.base import BaseServices


class HotelServices(BaseServices):
    model = Hotels
