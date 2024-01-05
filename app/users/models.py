from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


# -------- new style ---------
class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

# ----------------old style for tables ----------------
# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, nullable=False)
#     email = Column(String, nullable=False)
#     hashed_password = Column(String, nullable=False)
