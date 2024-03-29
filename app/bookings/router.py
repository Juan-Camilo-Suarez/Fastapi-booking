from datetime import date

from fastapi import APIRouter, Depends
from pydantic import parse_obj_as

from app.bookings.booking_dto import BookingDTO
from app.bookings.services import BookingService
from app.exceptions import RoomCannotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Endpoints for Bookings'],
)


# get bookings by user
@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingService.find_all_filters(user_id=user.id)


@router.post('')
async def add_bookings(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingService.add(user.id, room_id, date_from, date_to)
    booking_dict = {'date_from': date_from}
    send_booking_confirmation_email.delay(booking_dict, user.email)
    if not booking:
        raise RoomCannotBeBookedException
