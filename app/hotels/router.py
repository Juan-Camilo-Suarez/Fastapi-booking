from fastapi import APIRouter

router = APIRouter(
    prefix='/hotels',
    tags=['Endpoints for Hotels and Rooms'],
)


@router.get("")
def get_hotels():
    pass
