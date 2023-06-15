from datetime import date
from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from .enum import StukTypeEnum
from .misc import NEN3610ID
from .misc import Waardelijst


class FieldStuk(BaseModel):
    identificatie: Optional[NEN3610ID] = None
    type: Optional[StukTypeEnum] = None
    toelichting_bewaarder: Optional[str] = Field(None, alias="toelichtingBewaarder")
    omvat: Optional[List[NEN3610ID]] = None


class PortefeuilleId(BaseModel):
    akr_registercode: Optional[Waardelijst] = Field(None, alias="akrRegistercode")
    akr_stukdeel1: Optional[str] = Field(None, alias="akrStukdeel1")
    akr_stukdeel2: Optional[str] = Field(None, alias="akrStukdeel2")
    akr_stukdeel3: Optional[str] = Field(None, alias="akrStukdeel3")
    volgnummer_staat75: Optional[int] = Field(None, alias="volgnummerStaat75")


class Kadasterstuk(FieldStuk):
    portefeuillenummer: Optional[PortefeuilleId] = None


class TypeDeelEnNummer(BaseModel):
    deel: Optional[str] = None
    nummer: Optional[str] = None
    reeks: Optional[Waardelijst] = None
    registercode: Optional[Waardelijst] = None
    soort_register: Optional[Waardelijst] = Field(None, alias="soortRegister")


class Tijdstip(BaseModel):
    datum: date
    tijd: datetime


class TerInschrijvingAangebodenStuk(FieldStuk):
    aard: Optional[Waardelijst] = None
    deel_en_nummer: Optional[TypeDeelEnNummer] = Field(None, alias="deelEnNummer")
    heeft_kadaster_verzoek: Optional[bool] = Field(None, alias="heeftKadasterVerzoek")
    status_stuk_or: Optional[Waardelijst] = Field(None, alias="statusStukOR")
    tekening_ingeschreven: Optional[bool] = Field(None, alias="tekeningIngeschreven")
    tijdstip_aanbieding: Optional[Tijdstip] = Field(None, alias="tijdstipAanbieding")
    tijdstip_ondertekening: Optional[Tijdstip] = Field(
        None, alias="tijdstipOndertekening"
    )
