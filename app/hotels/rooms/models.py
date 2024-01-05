from sqlalchemy import Column, Integer, ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


# -------- new style ---------
class Rooms(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]

# ----------------old style for tables ----------------
# class Rooms(Base):
#     __tablename__ = 'rooms'
#
#     id = Column(Integer, primary_key=True, nullable=False)
#     hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Integer, nullable=False)
#     services = Column(JSON, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     image_id = Column(Integer)
