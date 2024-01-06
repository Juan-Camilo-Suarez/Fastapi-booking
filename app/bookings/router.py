from fastapi import APIRouter

from app.bookings.booking_dto import BookingDTO
from app.bookings.services import BookingService

router = APIRouter(
    prefix='/bookings',
    tags=['Endpoints for Bookings'],
)


@router.get('/')
async def get_bookings() -> list[BookingDTO]:
    result = BookingService.find_all()
    return await result
