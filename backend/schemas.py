from typing import Any, Optional

from pydantic import BaseModel


class Model(BaseModel):
    uid: int
    links: dict[str, Any] = {}

    class Config:
        orm_mode = True


class Individual(Model):
    name: str
    place_uid: int
    year_of_excavation: Optional[int]
    sex: Optional[str]
    age: Optional[str]
    individual_type: Optional[str]
    preservation: Optional[str]
    epoch: Optional[str]
    comments: Optional[str]


class Place(Model):
    name: str
    head_of_excavations: Optional[str]
    type_of_burial_site: Optional[str]
    coordinates: Optional[str]
    comments: Optional[str]
