from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from app.bookings.router import router as router_bookings
from app.config import settings
from app.users.router import router as router_users
from app.hotels.router import router as router_hotels
from app.hotels.rooms.router import router as router_hotels_rooms
from app.pages.router import router as router_pages
from app.images.router import router as router_images

app = FastAPI()
# endpoint to get avaliable pictures(this create independent app)
app.mount('/static', StaticFiles(directory='app/static'), 'static')
# endpoint to upload pictures and files
app.include_router(router_images)

# common endpoint
app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_hotels_rooms)

# this routeres for frontend
app.include_router(router_pages)


# CORS config way to give access one domain work with our api and what permissions
# origins = [
#     # 3000 - порт, на котором работает фронтенд на React.js
#     "http://localhost:3000",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
#                    "Access-Control-Allow-Origin", "Authorization"],
# )

@app.get("/cat")
@cache(expire=60)
async def index():
    return dict(hello="world")


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
