from datetime import date

from pydantic import BaseModel, ConfigDict


class HotelsDTO(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int

    # orm_mode поменял название во 2 версии Pydantic
    # this used to convert the atributes to dict
    model_config = ConfigDict(from_attributes=True)
