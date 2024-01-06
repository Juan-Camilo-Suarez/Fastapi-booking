from fastapi import APIRouter, Depends

from app.bookings.booking_dto import BookingDTO
from app.bookings.services import BookingService
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Endpoints for Bookings'],
)


# get bookings by user
@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all(user_id=user.id)
