from fastapi import APIRouter

router = APIRouter(
    prefix='/bookings',
    tags=['Endpoints for Bookings'],
)


@router.get('/')
def get_bookings():
    pass


@router.get('/{bookig_id}')
def get_bookings2(bookig_id):
    pass
