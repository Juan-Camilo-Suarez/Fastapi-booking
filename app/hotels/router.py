from datetime import date

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


@router.get("/{location}")
async def get_hotels_by_name(location: str, date_from: date, date_to: date):
    return location

"""
with roomsbyhotel as (select *
                      from hotels
                               right join rooms on hotels.id = rooms.hotel_id
                      where location like '%Алтай%'),
     booked as (select room_id, count(room_id)
                from bookings
                where (date_from >= '2023-06-28' and date_from <= '2023-07-15')
                   or (date_from <= '2023-07-10' and date_to > '2023-07-25')
                group by room_id)
select *
from roomsbyhotel
         LEFT JOIN booked ON roomsbyhotel.id = booked.room_id;
-- booked as (select *
--                 from bookings
--                 where (date_from >= '2023-06-28' and date_from <= '2023-07-15')
--                    or (date_from <= '2023-07-10' and date_to > '2023-07-25'))
-- select *
-- from roomsbyhotel right join booked on booked.room_id = booked.room_id;
-- select room_id, count(room_id)
--                 from bookings
--                 where (date_from >= '2023-06-28' and date_from <= '2023-07-15')
--                    or (date_from <= '2023-07-10' and date_to > '2023-07-25')
-- group by room_id
"""