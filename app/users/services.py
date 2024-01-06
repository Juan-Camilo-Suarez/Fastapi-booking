from app.services.base import BaseServices
from app.users.models import Users


class UserServices(BaseServices):
    model = Users
