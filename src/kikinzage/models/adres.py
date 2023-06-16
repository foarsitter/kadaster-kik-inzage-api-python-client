from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from pydantic import RootModel
from typing_extensions import Annotated

from .enum import AdresLocatieTypeEnum
from .misc import NEN3610ID
from .misc import Waardelijst


class Adresnummer(RootModel[str]):
    root: str = Field(..., title="Adresnummer")


class OpenbareRuimte(BaseModel):
    openbare_ruimte_naam: Optional[str] = Field(
        None, alias="openbareRuimteNaam", max_length=80, min_length=1
    )
    gerelateerde_woonplaats_naam: Optional[str] = Field(
        None, alias="gerelateerdeWoonplaatsNaam", max_length=80, min_length=1
    )


class TypePostcode(RootModel[str]):
    root: str = Field(..., title="TypePostcode")


class AdresBuitenland(BaseModel):
    adres: Optional[str] = Field(None, max_length=50, min_length=1)
    identificatie: Optional[Adresnummer] = None
    land: Optional[Waardelijst] = None
    regio: Optional[str] = Field(None, max_length=39, min_length=1)
    woonplaats: Optional[str] = Field(None, max_length=80, min_length=1)


class Nummeraanduiding(BaseModel):
    huisletter: Optional[str] = Field(None, max_length=1, pattern="[a-zA-Z]")
    huisnummer: Optional[int] = None
    huisnummertoevoeging: Optional[str] = Field(
        None, max_length=4, min_length=1, pattern="([a-z,A-Z,0-9])+"
    )
    identificatie: Optional[str] = None
    postcode: Optional[str] = Field(
        None, max_length=6, pattern="[1-9][0-9][0-9][0-9][A-Z][A-Z]"
    )
    gerelateerde_openbare_ruimte: Optional[OpenbareRuimte] = Field(
        None, alias="gerelateerdeOpenbareRuimte"
    )
    gerelateerde_woonplaats_naam: Optional[str] = Field(
        None, alias="gerelateerdeWoonplaatsNaam", max_length=80, min_length=1
    )


class FieldAdresLocatie(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    type: Optional[AdresLocatieTypeEnum] = None


class ObjectlocatieBinnenland(FieldAdresLocatie):
    type: Literal[
        AdresLocatieTypeEnum.OBJECTLOCATIE_BINNENLAND
    ] = AdresLocatieTypeEnum.OBJECTLOCATIE_BINNENLAND
    nummeraanduiding: Optional[Nummeraanduiding] = None


class ObjectlocatieBuitenland(FieldAdresLocatie):
    type: Literal[
        AdresLocatieTypeEnum.OBJECTLOCATIE_BUITENLAND
    ] = AdresLocatieTypeEnum.OBJECTLOCATIE_BUITENLAND
    adres_buitenland: Optional[AdresBuitenland] = Field(None, alias="adresBuitenland")


class PostbusLocatie(FieldAdresLocatie):
    type: Literal[
        AdresLocatieTypeEnum.POSTBUS_LOCATIE
    ] = AdresLocatieTypeEnum.POSTBUS_LOCATIE
    postbusnummer: Optional[int] = None
    postcode: Optional[TypePostcode] = None
    woonplaats_naam: Optional[str] = Field(
        None, alias="woonplaatsNaam", max_length=80, min_length=1
    )


AdresType = Annotated[
    Union[ObjectlocatieBinnenland, ObjectlocatieBuitenland, PostbusLocatie],
    Field(discriminator="type"),
]
