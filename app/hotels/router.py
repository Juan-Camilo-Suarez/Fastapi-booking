from fastapi import APIRouter

from app.hotels.hotels_dto import HotelsDTO
from app.hotels.services import HotelServices

router = APIRouter(
    prefix='/hotels',
    tags=['Endpoints for Hotels and Rooms'],
)


@router.get("")
async def get_hotels() -> list[HotelsDTO]:
    list_hotels = await HotelServices.find_all()
    return list_hotels
