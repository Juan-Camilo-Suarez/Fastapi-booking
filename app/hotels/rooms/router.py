from fastapi import APIRouter

router = APIRouter(
    prefix='/hotels',
    tags=['Endpoints for Hotels and Rooms'],
)


@router.get("/{hotel_id}/rooms")
def get_rooms():
    pass
