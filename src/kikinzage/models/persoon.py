from datetime import date
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field
from typing_extensions import Annotated

from kikinzage.models.enum import PersoonTypeEnum
from kikinzage.models.misc import NEN3610ID
from kikinzage.models.misc import Waardelijst


class TypeOnvolledigeDatum(BaseModel):
    dag: Optional[int] = Field(None, ge=1, le=31)
    datum: Optional[date] = None
    jaar: Optional[int] = Field(None, le=9999)
    maand: Optional[int] = Field(None, ge=1, le=12)


class Overlijden(BaseModel):
    datum_overlijden: Optional[TypeOnvolledigeDatum] = Field(
        None, alias="datumOverlijden"
    )


class Geboorte(BaseModel):
    geboortedatum: Optional[TypeOnvolledigeDatum] = None
    geboorteland: Optional[Waardelijst] = None
    geboorteplaats: Optional[str] = Field(None, max_length=80, min_length=1)


class Rechtspersoon(BaseModel):
    kvk_nummer: Optional[str] = Field(None, alias="kvkNummer", max_length=8)


class Naam(BaseModel):
    geslachtsnaam: Optional[str] = Field(None, max_length=200, min_length=1)
    voornamen: Optional[str] = Field(None, max_length=200, min_length=1)
    voorvoegselsgeslachtsnaam: Optional[str] = Field(None, max_length=10, min_length=1)


class Geslacht(BaseModel):
    geslachtsaanduiding: Optional[Waardelijst] = None


class GeregistreerdPersoon(BaseModel):
    adellijke_titel_of_predikaat: Optional[Waardelijst] = Field(
        None, alias="adellijkeTitelOfPredikaat"
    )
    bsn: Optional[str] = Field(
        ..., max_length=9, pattern="([0][0-9]{8})|([1-9][0-9]{7,8})"
    )
    geboorte: Optional[Geboorte] = None
    geslacht: Optional[Geslacht] = None
    in_onderzoek: Optional[bool] = Field(None, alias="inOnderzoek")
    naam: Optional[Naam] = None
    overlijden: Optional[Overlijden] = None


class FieldPersoon(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    type: Optional[PersoonTypeEnum] = None
    beschikkingsbevoegdheid: Optional[Waardelijst] = None
    indicatie_niet_toonbare_diakriet: Optional[bool] = Field(
        None, alias="indicatieNietToonbareDiakriet"
    )
    postlocatie: Optional[NEN3610ID] = None
    woonlocatie: Optional[NEN3610ID] = None
    is_vermeld_in: Optional[List[NEN3610ID]] = Field(
        None, alias="isVermeldIn", min_length=0
    )
    is_rechthebbende_van: Optional[List[NEN3610ID]] = Field(
        None, alias="isRechthebbendeVan", min_length=0
    )
    is_betrokkene_bij: Optional[List[NEN3610ID]] = Field(
        None, alias="isBetrokkeneBij", min_length=0
    )


class NietNatuurlijkPersoon(FieldPersoon):
    type: Literal[
        PersoonTypeEnum.NIET_NATUURLIJK_PERSOON
    ] = PersoonTypeEnum.NIET_NATUURLIJK_PERSOON
    rechtsvorm: Optional[Waardelijst] = None
    statutaire_naam: Optional[str] = Field(
        None, alias="statutaireNaam", max_length=200, min_length=1
    )
    statutaire_zetel: Optional[str] = Field(
        None, alias="statutaireZetel", max_length=40, min_length=1
    )
    betreft: Optional[Rechtspersoon] = None


class NatuurlijkPersoon(FieldPersoon):
    type: Literal[
        PersoonTypeEnum.NATUURLIJK_PERSOON
    ] = PersoonTypeEnum.NATUURLIJK_PERSOON
    indicatie_overleden: Optional[bool] = Field(None, alias="indicatieOverleden")
    betreft: Optional[GeregistreerdPersoon] = None


PersoonType = Annotated[
    Union[NietNatuurlijkPersoon, NatuurlijkPersoon],
    Field(discriminator="type"),
]
