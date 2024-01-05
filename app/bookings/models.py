from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


# -------- new style ---------:
class Bookings(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[datetime] = mapped_column(Date, nullable=False)
    date_to: Mapped[datetime] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

# ----------------old style for tables ----------------
# class Bookings(Base):
#     __tablename__ = 'bookings'
#
#     id = Column(Integer, primary_key=True)
#     room_id = Column(Integer, ForeignKey("rooms.id"))
#     user_id = Column(Integer, ForeignKey("users.id"))
#     date_from = Column(Date, nullable=False)
#     date_to = Column(Date, nullable=False)
#     price = Column(Integer, nullable=False)
#     total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
#     total_days = Column(Integer, Computed("date_to - date_from"))
