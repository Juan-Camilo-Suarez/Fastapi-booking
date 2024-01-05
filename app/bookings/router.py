from fastapi import APIRouter

from app.bookings.services import BookingService

router = APIRouter(
    prefix='/bookings',
    tags=['Endpoints for Bookings'],
)


@router.get('/')
async def get_bookings():
    result = BookingService.find_all()
    return await result
