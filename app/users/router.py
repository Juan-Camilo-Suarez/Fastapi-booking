from fastapi import APIRouter, HTTPException, status, Response

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.services import UserServices
from app.users.userDTO import UserAuthDTO

router = APIRouter(
    prefix="/auth",
    tags=["Auth and users"],
    # this for to add information to code responces in documentation
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Response for not authorized user",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Response for user that not authorized",
        },
    }
)


@router.post("/register")
async def register_user(user_data: UserAuthDTO):
    existing_user = await UserServices.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserServices.add_user(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: UserAuthDTO):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
