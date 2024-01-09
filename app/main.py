from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_hotels_rooms
from app.pages.router import router as router_pages

app = FastAPI()
# endpoint to get avaliable pictures(this create independent app)
app.mount('/static', StaticFiles(directory='app/static'), 'static')

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_hotels_rooms)

# this routeres for frontend
app.include_router(router_pages)
