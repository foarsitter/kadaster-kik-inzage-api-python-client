from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from kikinzage.models.enum import Type


class NEN3610ID(BaseModel):
    lokaal_id: str = Field(..., alias="lokaalID")
    namespace: str


class Waardelijst(BaseModel):
    code: str
    waarde: Optional[str] = None


class PointGeoJSON(BaseModel):
    type: Type
    coordinates: List[float] = Field(..., min_length=2)


class TypeBreuk(BaseModel):
    noemer: Optional[int] = None
    teller: Optional[int] = None


class Bedrag(BaseModel):
    som: Optional[float] = None
    valuta: Optional[Waardelijst] = None
