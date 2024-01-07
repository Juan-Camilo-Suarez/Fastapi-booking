from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.services import BookingService
from app.exceptions import RoomCannotBeBookedException
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


@router.post('')
async def add_bookings(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingService.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBookedException
